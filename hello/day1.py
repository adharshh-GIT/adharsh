from flask import Flask



app=Flask(__name__)
@app.route('/')
def hai():
    return"<h1>HELLO</h1>"


@app.route('/H')
def hai1():
    return"<h1>HELLO</h1>"

@app.route('/H/<name>')
def hai2(name):
    return"<h1>HELLO "+ name +"</h1>"


@app.route('/H/<int:name>')
def hai3(name):
    return"num --> %d"%name


def welcome():
    return 'welcome'

app.add_url_rule("/W","welcome",welcome)


if __name__=="__main__":
    app.run(debug=True)