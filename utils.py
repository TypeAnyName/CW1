
import requests
import random
import basic_word


questions = []


def load_random_word():
    response = requests.get("https://jsonkeeper.com/b/N7D4")
    response_json = response.json()
    for i in response_json:
        questions.append(basic_word.BasicWord(i['word'], i['subwords']))
    return random.choice(questions)


