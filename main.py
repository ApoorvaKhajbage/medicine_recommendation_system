from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# python main
if __name__ == '__main__':
    app.run(debug=True)
