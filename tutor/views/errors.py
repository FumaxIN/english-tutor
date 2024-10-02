from datetime import timedelta
from django.utils import timezone
from django.utils.timezone import now
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.openapi import OpenApiParameter

from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from tutor.models import User, Error, SuperBucket, SubBucket
from tutor.serializers import UserSerializer, ErrorSerializer, ErrorFilterSerializer, TopErrorSerializer, TopErrorResponseSerializer


class ErrorViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
    serializer_action_classes = {
        'generate_exercise': TopErrorResponseSerializer
    }

class TopErrorsView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name="user_id", type=str, location=OpenApiParameter.QUERY, required=True, description="UUID of the User"),
            OpenApiParameter(name="last_n_days", type=int, location=OpenApiParameter.QUERY, required=False, description="Optional, filter by last N days"),
            OpenApiParameter(name="top_n_errors", type=int, location=OpenApiParameter.QUERY, required=False, description="Optional, get top N errors")
        ],
        responses={200: TopErrorResponseSerializer(many=True)},
    )
    def get(self, request):
        serializer = ErrorFilterSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        user_id = serializer.validated_data['user_id']
        last_n_days = serializer.validated_data.get('last_n_days')
        top_n_errors = serializer.validated_data.get('top_n_errors')

        user = User.objects.filter(id=user_id).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        filtered_errors = Error.objects.filter(user=user)

        if last_n_days:
            since = now() - timedelta(days=last_n_days)
            filtered_errors = filtered_errors.filter(timestamp_utc__gte=since)

        error_stats = filtered_errors.values('errorCategory', 'errorSubCategory').annotate(
            errorFrequency=Count('id')
        ).order_by('-errorFrequency')

        if top_n_errors:
            error_stats = error_stats[:top_n_errors]

        top_errors = []
        for error_stat in error_stats:
            error = {
                'errorCategory': SuperBucket(error_stat['errorCategory']).label,
                'errorSubCategory': SubBucket(error_stat['errorSubCategory']).label,
                'errorFrequency': error_stat['errorFrequency']
            }
            top_errors.append(error)

        return Response({"top_errors": top_errors})