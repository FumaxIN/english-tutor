from core import settings
from django.urls import path, include
from rest_framework_nested import routers

from tutor.views.users import UserViewSet
from tutor.views.errors import ErrorViewSet, TopErrorsView

app_name = "monitoring"

router = routers.SimpleRouter(trailing_slash=False)
if settings.DEBUG:
    router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", UserViewSet)
router.register(r"errors", ErrorViewSet)

tutor_urls = [
    path("", TopErrorsView.as_view(), name="top_errors")
]
urlpatterns = [
    path("generate-exercise", include(tutor_urls)),
    path("", include(router.urls)),
]