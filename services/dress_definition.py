import json


def dress_definition(word_json):
    dressed = []
    for meaning in word_json["meanings"]:
        dressed.append(f"\n*Definition* : {meaning['definitions'][0]['definition']}")

    return dressed[0]
