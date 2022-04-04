import os
import openai


api="****************************************"




class GPT3:


    def __init__(self):
        pass


    #todo define :method that use GPT3 for questin responce in CLASS named GPT3
    def get_gpt3aq(self,text):
        openai.api_key="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"

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
