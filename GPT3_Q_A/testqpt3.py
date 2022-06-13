import os
import openai
from googletrans import Translator
#from googletrans.models import Translator


# openai.api_key = "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"
#
#
# openai.Answer.create(
#     search_model="ada",#beta type in openai
#     model="curie",
#     question="which puppy is happy?",
#     file="file-2ksWL61f0Q5c5vCYOLwUuhPk",
#     examples_context="In 2017, U.S. life expectancy was 78.6 years.",
#     examples=[["What is human life expectancy in the United States?", "78 years."]],
#     max_rerank=10,
#     max_tokens=5,
#     stop=["\n", "<|endoftext|>"]
# ).answers


def trans(message, src, dest):
    trans = Translator()
    t = trans.translate(
        message, src=src, dest=dest
    )

    print(f'Source: {t.src}')
    print(f'Destination: {t.dest}')
    print(f'{t.text}')
    print()
    result = f'{t.text}'
    return result


def get_gpt3aq_with_translate(question, lang):
    openai.api_key = "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"
    # text1_1 = MyMemoryTranslator(source=lang, target="en").translate(text=text)
    translator = Translator()
    text1_1 = translator.translate(question, src=lang, dest="en")
    print(text1_1.text)
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text1_1.text,
        temperature=0.7,
        max_tokens=170,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    content = response.choices[0].text
    print(content)
    translated = translator.translate(content,src="en",dest=lang)
    return translated.text



text=" ماهي أفريقيا ?"
lang ="ar"
#dest = "en"
result=get_gpt3aq_with_translate(text,lang)
print(result)