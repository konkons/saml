from flask import Flask,request
import random
app = Flask(__name__)



tokens={}

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/catchassert',methods=['POST'])
def catchassert():
    data=request.get_data()
    tokname=randomgen()
    global tokens
    tokens[tokname]=data.decode("utf-8", "strict")
    print(tokname)
    print(tokens)
    return tokname


@app.route('/askinfo/<tok>',methods=['GET'])
def askinfo(tok):
    tokstr=tok
    print(tokstr)
    global tokens
    if tokstr in tokens:
       body=tokens[tokstr]
       print(body)
       del tokens[tok]
    else:
        return "sorry does not exist"
    return body







def randomgen():
    randomString=""
    for i in range(10):
           randomString += (str(chr(random.randint(97,122))))
    return randomString


if __name__ == '__main__':
    app.run()

