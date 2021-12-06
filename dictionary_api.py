import requests
import json

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def make_url(word):
    return f"{URL}{word}"


def define_word(word):
    url = make_url(word)
    r = requests.get(url)
    return r.json()
