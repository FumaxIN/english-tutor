from django.db.models import IntegerChoices

class SuperBucket(IntegerChoices):
    GRAMMAR = 1, "Grammar"
    VOCABULARY = 2, "Vocabulary"
    PRONUNCIATION = 3, "Pronunciation"
    FLUENCY = 4, "Fluency/Content"

class SubBucket(IntegerChoices):
    PRONOUN_ERROR = 1, "Pronoun"
    ADVERB_ERROR = 2, "Adverb"
    TENSE_ERROR = 3, "Tense"
    SUBJECT_VERB_AGREEMENT_ERROR = 4, "Subject_Verb_Agreement"

    WRONG_WORD_ERROR = 5, "Wrong_Word"
    APOSTROPHE_ERROR = 6, "Apostrophe"
    PLURAL_ERROR = 7, "Plural"

    MISPRONOUNCED_SYLLABLE_ERROR = 8, "Mispronounced_Syllable"
    MISPRONOUNCED_WORD_ERROR = 9, "Mispronounced_Word"

    INCOHERENT_ERROR = 10, "Incoherent"
    REPETITION_ERROR = 11, "Repetition"
    LACK_OF_CONTENT_ERROR = 12, "Lack_of_Content"