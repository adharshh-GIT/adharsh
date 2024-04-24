from flask import *
import sqlite3


app=Flask(__name__)



@app.route('/sc',methods=['GET','POST'])
def stud_create():
    if request.method=="POST":
        n=request.form['fname']
        p=request.form['nm']
        e=request.form['em']
        with sqlite3.connect("stud.db") as con:
            cur=con.cursor()
            cur.execute(""" insert into student (name,email,number)values(?,?,?)""",(n,p,e))
            con.commit()



        return 'succes'
    else:
        return render_template('register.html')




@app.route('/sv')
def stud_view():
    con=sqlite3.connect('stud.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    return render_template('stud_view.html',data=rows)



@app.route('/sd/<int:id>')
def stud_del(id):
    print(id)
    with sqlite3.connect('stud.db')as con:
        cur=con.cursor()
        cur.execute("""delete from student where id=?""",(id,))
        con.commit()
        return redirect(url_for('stud_view'))
    

@app.route('/su/<int:id>')
def stud_edit(id):
    print(id)
    with sqlite3.connect('stud.db') as con:
        cur=con.cursor()
        cur.execute("""select * from student where id=?""",(id,))
        rows=cur.fetchall()
         
        return render_template('update.html',data=rows)












if __name__ =="__main__":
    app.run(debug=True)