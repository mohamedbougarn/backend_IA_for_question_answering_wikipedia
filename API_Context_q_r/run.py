#importation les méthode dans la page test1
from API_Context_q_r.camombert_q_r__init__ import Q_R
# import main Flask class and request object
from flask import Flask, request, jsonify

#import flaskrestful

#from flask_restful import reqparse


q_r = Q_R()
q_r.loadModel()



# create the Flask app
app = Flask(__name__)

# allow both GET and POST requests
@app.route('/Get/Response', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        context = request.form.get('context')
        question = request.form.get('question')
        return jsonify({'message_text': request.form.get('question'), 'response': q_r.predict(context, question)})
    else:
        return jsonify({'message_text': request.form.get('question') , 'response': "eurreur"})




"""test avec du score et sentiment"""

# allow both GET and POST requests
@app.route('/Get/Response+Answer', methods=['GET', 'POST'])
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




@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)