from flask import render_template,url_for,request,flash,current_app,abort,redirect,url_for
from flask.globals import session
from zooshicovid import app,db,search
from .models import Register
import pdfkit as pdf
import os
import random 
from twilio.rest import Client



@app.route("/")
def index():  
    data = Register.query.all()
    return render_template("index.html",person = data)

@app.route("/search")
def search():
    keyword = request.args.get('taq')
    # datasearch = Register.query.order_by(Register.RequestDate.asc()).msearch(keyword,fields=['CardID'],limit=20)  
    # datasearch = Register.query.msearch(keyword,fields=['CardID']).order_by(Register.RequestDate.desc()).all()
    datasearch = Register.query.msearch(keyword,fields=['CardID']).order_by(Register.RequestDate.desc()).limit(10) 

    return render_template("covid_data.html",person = datasearch)
# @app.route("/search",methods = ['GET','POST'],defaults={"page":1})
# @app.route("/search",methods = ['GET','POST'])
# def search():
     
#     if request.method == 'POST' and 'taq' in request.form:
#         taq = request.form["taq"]
#         search = "%{}%".format(taq)
#         data = Register.query.filter(Register.CardID.like(search)).paginate()

#         return url_for("covid_data.html",person = data,taq=taq) 
#     else:  

#         data = Register.query.order_by(Register.RequestDate.desc()).paginate()    
#     return render_template("covid_data.html",person = data)

# @app.route("/search",methods = ['GET','POST'])
# def search():
#     data = Register.query.order_by(Register.RequestDate.asc())

#     if request.method == 'POST':
#         taq = request.form['taq']     
#         data = Register.query.filter(Register.CardID.like(taq)).order_by(Register.RequestDate.asc())
#         # return render_template("covid_data.html",person = data)  
#     else:
#         return redirect('/') 
#     return render_template("covid_data.html",person = data)  




@app.route("/getOTP",methods = ['GET','POST'])
def getOTP():
      cid = request.form['cid']
      number = request.form['number']
      var = getOTPApi(number)
           
      if var:
          return render_template("confirmotp.html",data=cid)

def generateOTP():
    return random.randrange(100000,999999)

def getOTPApi(number):
    account_sid = 'AC9624802f24fef430caeac3e765dd9fbe'
    auth_token = 'b9b1cc4d3db87943317f88e3c2d119e6'
    client = Client(account_sid, auth_token)
    otp = generateOTP()
    body = 'ทดสอบส่ง You OTP is '+str(otp)
    message = client.messages.create(
        from_='+18647148495',
        body=body,
        to=["+66"+number]
    )
    if message.sid:
        return True
    else:
        False
  
