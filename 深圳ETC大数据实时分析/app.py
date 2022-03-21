from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify

import string
import utils

app = Flask(__name__)


@app.route('/')
def start_html():

    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify(data)

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    return jsonify(data)

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    return jsonify(data)

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()

    return jsonify(data)


@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data()
    return jsonify(data)

@app.route("/time")
def get_time():
    return utils.get_time()

@app.route('/ajax',methods=["get","post"])
def hello_world4():
    name = request.values.get("name")
    score =  request.values.get("score")


    return '10000'



@app.route("/abc")
def hello_world1():
    id = request.values.get("id")
    return f"""
    <form action="/login">
        账号：<input name="name" value="{id}"><br>
        密码：<input name="pwd">
        <input type="submit">
    </form>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
