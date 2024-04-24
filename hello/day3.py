from flask import *


app=Flask(__name__)
app.secret_key="a"

@app.route('/Gstu',methods=['GET'])
def getmeth():
    name=request.args.get('fname')
    email=request.args.get('em')
    phone=request.args.get('nm')
    place=request.args.get('pl')
    print(name,email,phone,place)

    return"succes Get method"





@app.route('/Pstu',methods=['POST'])
def postmeth():
    name=request.form['fname']
    email=request.form['em']
    phone=request.form['nm']
    place=request.form['pl']

    print(name,email,phone,place)

    return"succes Post method"



@app.route('/n')
def reg():
    return render_template('post_mth.html')



@app.route('/suc',methods=['POST','GET'])
def getdata():
    if request.method=='POST':
        data=request.form
        return data
    
    else:
        return render_template('post_mth.html')
    




@app.route('/sc')
def set_cookie():
    res=make_response('<h1> cookie is set</h1>')
    res.set_cookie('fname','shukur')
    return res


@app.route('/gc')
def get_cook():
    name=request.cookies.get('fname')
    return name




@app.route('/ss')
def set_session():
    res=make_response('session is set')
    session['phone']=97448358585
    return res



@app.route('/gs')
def get_session():
    if "phone" in session:
        return str(session['phone'])
    

@app.route('/pf')
def prfl():
    return render_template('login.html')






@app.route('/log',methods=['POST'])
def login():
    email=request.form['em']
    password=request.form['pas']
    print( email,password)
    if password=='admin':
        session['email']=email
        return render_template('viewprof.html')
    else:
        return render_template('login.html')

 

@app.route('/gp')
def pas():
    password=request.cookies.get('pass')
    if password=="admin":
        return password





if __name__ =="__main__":
    app.run(debug=True)



