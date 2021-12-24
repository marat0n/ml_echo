from flask import Flask, render_template, request
import neuro

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    neuro_result = 0

    if request.method == 'POST':
        data = request.form.get('input1')
        neuro_result = neuro.neuro(neuro)

    return render_template('home.html', neuro_result=neuro_result)