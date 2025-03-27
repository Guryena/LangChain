import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(source_language, target_language, sentence) :
    prompt = [
        {
        "role" : "system",
        "content" : f"You're a translator bot. Translate sentence from {source_language} to {target_language}.",
        },
        {
        "role" : "user",
        "content" : f"Translate this : {sentence}",
        }
    ]
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = prompt,
        temperature = 0.1
    )

    translated_text = response["choices"][0]["message"]["content"].strip()

    return translated_text

#input user
source_language = input("Enter the Source Language : ")
target_language = input("Enter the Target Language : ")
origin_sentence = input("Please enter the contents to be translated \n")

#run translate
translate_sentence = translate_text(source_language, target_language, origin_sentence)

#result translate
print(f"Translated sentence \n {translate_sentence}")