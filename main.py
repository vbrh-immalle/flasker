from flask import Flask, redirect

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

@app.route('/redirect-me')
def redirectme():
    return redirect('/hello')

app.run(host='127.0.0.2', port='8080', debug=True)