import flask
from flask import Flask

from summary import summarize

app = Flask(__name__)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print("Starting Summary....")
    processed_text = summarize(text)
    return render_template('summary.html', processed_text=summarize(text))

if __name__ == '__main__':
    app.run(debug=True)