import  wikipedia



#todo define : loading model
#todo define : loading model



class Wiki_Q_R:
    def _init_(self):
        pass

    # todo define : loading model = methode that get answer from wikipedia when send a question
    def question_answer(self,question):
        wikipedia.set_lang("fr")
        answer = wikipedia.summary(question)
        print(answer)
        return answer

    # todo define : loading model = methode that get page content text from wikipedia when lance a question
    def question_answer1(self ,question, lang):
        # wikipedia.set_lang("fr")
        wikipedia.set_lang(lang)
        print(f"Question: {question}")
        results = wikipedia.search(question)

        page = wikipedia.page(results[0],auto_suggest=False)
        print(f"Top wiki result: {page}")

        text = page.content

        # reader.tokenize(question, text)  #
        # print(f"Answer: {reader.get_answer()}")

        print()
        return text

    def qeustion_answer_paragraph(self,question,lang):
        # wikipedia.set_lang("fr")
        # try:
        wikipedia.set_lang(lang)
        print(f"Question: {question}")
        results = wikipedia.search(question)

        summary = wikipedia.summary(results[0], auto_suggest=False,sentences=6)
        print(f"Top wiki paragraph: {summary}")

        # text = page.content

        # reader.tokenize(question, text)  #
        # print(f"Answer: {reader.get_answer()}")

        # print()
        return summary
        # except:
        #     # e='False'
        #     return "False"
