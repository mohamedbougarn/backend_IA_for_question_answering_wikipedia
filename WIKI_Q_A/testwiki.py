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

#
wikipedia.set_lang("ar")
#answer = wikipedia.summary('la tunise démographie')
answer = wikipedia.search('ما هي سلبيات الإنترنت')
page = wikipedia.page(answer[0],auto_suggest=False)
print(f"Top wiki result: {page}")

text = page.content
print(text)
#reader.tokenize(question, text)
#print(f"Answer: {reader.get_answer()}")

print(answer)


#
# wikipedia.set_lang("fr")
# #answer = wikipedia.summary('elon musk')
# answer = wikipedia.search('qui elon musk')
# print(answer)
#
# page = wikipedia.page(answer[0],auto_suggest=False)
#
# print(f"Top wiki result: {page}")
#
# text = page.content
# print(text)
# #reader.tokenize(question, text)
# #print(f"Answer: {reader.get_answer()}")
#
# print(answer)

