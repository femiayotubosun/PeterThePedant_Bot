from unittest import TestCase
from dictionary_api import make_url


class ApiFuncTest(TestCase):
    def test_make_correct_url(self):
        url = make_url("hello")
        self.assertEqual(url, "https://api.dictionaryapi.dev/api/v2/entries/en/hello")
