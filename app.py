from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>You've Entered My Website</h1><p>What a mistake you've made.</p>"

if __name__ == '__main__':
    app.run(debug=True)