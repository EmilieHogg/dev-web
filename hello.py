from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route ("/")
def hello_world(name = None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
