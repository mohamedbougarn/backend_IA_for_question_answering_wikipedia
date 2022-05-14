import os
import openai
import json






class GPT3:


    def __init__(self):
        pass


    #todo define 1 : method for connecting api
    def connect(self):
        with open('./API_KEY.json') as file:
            data = json.load(file)

        openai.api_key = data["API"]

    #todo define 2: method that use GPT3 for questin responce in CLASS named GPT3
    def get_gpt3aq(self,text):
        #openai.api_key=api

        start_sequence = "\nA:"
        restart_sequence = "\n\nQ: "
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=text,
            temperature=0.7,
            max_tokens=170,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        content = response.choices[0].text.split('.')
        # print(content)
        return response.choices[0].text



    #todo define 3:method that use GPT3 for for transtalte in language  to laguage     in CLASS named GPT3
    def get_gpt3_translate(self, text, lang):
        #openai.api_key = api

        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="Translate this into 1." + lang + " \n " + text + " \n 1.",
            temperature=0.3,
            max_tokens=170,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        content = response.choices[0].text.split('.')
        # print(content)
        return response.choices[0].text



    #todo define : methode for translate with google

    #todo define :  methode for detection language
