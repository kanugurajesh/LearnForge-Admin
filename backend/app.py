from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload():
    return 'Upload'

if __name__ == '__main__':
    app.run()
