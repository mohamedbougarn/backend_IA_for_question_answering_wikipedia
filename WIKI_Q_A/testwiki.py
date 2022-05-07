import wikipedia

def question_answer(question):
    wikipedia.set_lang("fr")
    answer = wikipedia.summary(question)
    print(answer)
    return answer

def question_answer1(question,lang):
    #wikipedia.set_lang("fr")
    wikipedia.set_lang(lang)
    print(f"Question: {question}")
    results = wikipedia.search(question)

    page = wikipedia.page(results[0])
    print(f"Top wiki result: {page}")

    text = page.content

    #reader.tokenize(question, text)  #
    #print(f"Answer: {reader.get_answer()}")

    print()

wikipedia.set_lang("fr")
#answer = wikipedia.summary(' la tunise')
answer = wikipedia.search('la tunise')
page = wikipedia.page(answer[0])
print(f"Top wiki result: {page}")

text = page.content

# reader.tokenize(question, text)
print(f"Answer: {reader.get_answer()}")

print(answer)



