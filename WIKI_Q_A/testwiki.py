import wikipedia

def question_answer(question):
    answer = wikipedia.summary(question)
    print(answer)
    return answer



wikipedia.set_lang("fr")
answer = wikipedia.summary('kais said')
print(answer)



