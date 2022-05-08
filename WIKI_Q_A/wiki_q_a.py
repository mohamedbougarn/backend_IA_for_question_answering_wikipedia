import  wikipedia



#todo define : loading model
#todo define : loading model
#todo define : loading model
class Wiki_Q_R:
    def _init_(self):
        pass

    def question_answer(self,question):
        wikipedia.set_lang("fr")
        answer = wikipedia.summary(question)
        print(answer)
        return answer

    def question_answer1(self ,question, lang):
        # wikipedia.set_lang("fr")
        wikipedia.set_lang(lang)
        print(f"Question: {question}")
        results = wikipedia.search(question)

        page = wikipedia.page(results[0])
        print(f"Top wiki result: {page}")

        text = page.content

        # reader.tokenize(question, text)  #
        # print(f"Answer: {reader.get_answer()}")

        print()