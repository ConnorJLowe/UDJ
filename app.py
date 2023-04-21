from flask import Flask, render_template
import json
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key :)'


url = "https://theaudiodb.p.rapidapi.com/523532/searchalbum.php"

# creating a variable to set up methods as GET and POST
methods = ['GET', 'POST']


@app.route('/')
@app.route('/index', methods=methods)
def index():
    # req = requests.get(url)
    # source = req.text
    # data = json.loads(source)
    # print(type(source))
    # print(type(data))
    # print(data)
    # print(data.keys())
    # print(type(data['track']))
    # # print(type(data['track'].keys()))
    # print((data['track']))
    # mydata = data['track']
    # return render_template('index.html', data=mydata)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
