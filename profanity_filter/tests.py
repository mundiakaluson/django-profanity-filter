from django.test import TestCase
from .profanity_tags.profanity_check import word_filter
from .profanity_tags.profanity_check import pf_check
from dataclasses import dataclass
from profanity_filter import Config
from profanity_filter.types_ import AnalysesTypes, Language
from typing import Tuple
from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

@dataclass
class Config:
    analyses: AnalysesTypes = frozenset()
    censor_whole_words: bool = True
    deep_copy: bool = False
    dill: bool = False
    languages: Tuple[Language, ...] = ('en', )



class ProfanityTest(TestCase):

    def test_profanity_words(self):
        test_words = "Fuck, Bitch, Kids, Turd, Cock, Home, Come, Cum, Drop, Dog"
        test_words_check = word_filter(test_words)
        original_profanity = pf.censor(test_words)
        print(test_words_check); print(original_profanity)
        self.assertEquals(test_words_check, original_profanity)
