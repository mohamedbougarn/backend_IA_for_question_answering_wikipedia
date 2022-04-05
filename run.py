#importation les méthode dans la page test1
from API_Context_q_r.camombert_q_r__init__ import Q_R
from GPT3_Q_A.gpt3 import GPT3
# import main Flask class and request object
from flask import Flask, request, jsonify

#import flaskrestful

#from flask_restful import reqparse


q_r = Q_R()
q_r.loadModel()


#get gpt3 q
gpt3 = GPT3()
#gpt3.get_gpt3aq()


# create the Flask app
app = Flask(__name__)

# allow both GET and POST requests
@app.route('/get/response', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        data = request.json
        context = data['context']
        question = data['question']
        #context = request.args.get('context')
        #question = request.args.get('question')
        response = q_r.predict(context, question)
        print(' context = ', context, ' question=', question, 'response', response )
        return jsonify({'message_text': data['question'], 'response': response})
    else:
        return jsonify({'message_text': data['question'], 'response': "eurreur"})




"""test avec du score et sentiment"""

# allow both GET and POST requests
@app.route('/get/response+Answer', methods=['GET', 'POST'])
def form_example1():
    # handle the POST request
    if request.method == 'POST':
        context = request.form.get('context')
        question = request.form.get('question')
        answer = request.form.get('answer')
        response = q_r.predict(context,question)
        score = q_r.compute_f1(response,answer)

        return jsonify({'message_text': question,
                        'true_answer' : answer,
                        'response': response,
                        'score':score})
    else:
        return jsonify({'message_text': request.form.get('question'),
                        'true_answer' : request.form.get('answer '),
                        'response': 0,
                        'score':0})



#todo define : a root /get/gpt3 with method post
# that send a ansewer respence and get a question request in gpt3

# allow both GET and POST requests
@app.route('/get/gpt3', methods=['GET', 'POST'])
def getgpt3():
    # handle the POST request
    if request.method == 'POST':
        #context = request.form.get('context')
        question = request.form.get('question')
        answer = gpt3.get_gpt3aq(question)
        #response = q_r.predict(context,question)
        #score = q_r.compute_f1(response,answer)

        return jsonify({'message': question,
                        'response': answer
                        })
    else:
        return jsonify({'message_text': question,
                        'response': 0
                        })



#todo define : a root /translate/gpt3 with method post
# that send a ansewer respence and get a question request in gpt3

# allow both GET and POST requests
@app.route('/translate/gpt3', methods=['GET', 'POST'])
def getgpt3_translate():
    # handle the POST request
    if request.method == 'POST':
        #context = request.form.get('context')
        text = request.form.get('text')
        language = request.form.get('language')
        translated = gpt3.get_gpt3_translate(text,language)
        #response = q_r.predict(context,question)
        #score = q_r.compute_f1(response,answer)

        return jsonify({'text': text,
                        'language': language,
                        'translated': translated
                        })
    else:
        return jsonify({'text': text,
                        'language': language,
                        'translated': 0
                        })




@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)