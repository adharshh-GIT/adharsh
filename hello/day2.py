from flask import *

app=Flask(__name__)

@app.route('/admin')
def Admin():
    return"WELCOME ADMIN"

@app.route('/teacher')
def Teacher():
    return"WELCOME TEACHER"

@app.route('/student')
def Student():
    return"WELCOME STUDENT"

@app.route('/user/<uname>')
def user(uname):
    if uname=="admin":
        return redirect(url_for('Admin'))
    
    elif uname=="teacher":
        return redirect(url_for('Teacher'))
    
    elif uname=="student":
        return redirect(url_for('Student'))
    
    else:
        return('invalied')
    

    
@app.route('/k/<job>')
def mypage(job):
    name="ammu"
    return render_template('d1.html',uname=name,j=job)




@app.route('/<int:num>')
def mult(num):
    return render_template('mul.html',na=num)




if __name__ =="__main__":
    app.run(debug=True)