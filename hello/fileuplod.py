from flask import *
from flask_mail import *

app=Flask(__name__)
app.secret_key="k"
@app.route('/',methods=['GET','POST'])
def file_up():
    if request.method=="GET":
        return render_template("file_upload.html")
    else:
        f=request.files['dp']
        f.save(f.filename)
        flash("succesfully uploaded")
        return render_template("file_upload.html")
                # return "succes"



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="adharsh585800@gmail.com"
app.config['MAIL_PASSWORD']="okvw hgzq wyvr codv"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
@app.route('/ms')
def mail_send():
    msg=Message('subject',sender='adharsh585800@gmail.com',recipients=['adharshadhi45@gmail.com'])
    msg.body="HAI ITS A MAIL FROM FLASK"
    mail.send(msg)
    return 'successfully send a email'




if __name__=="__main__":
    app.run(debug=True)