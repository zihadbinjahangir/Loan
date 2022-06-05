from distutils.log import debug
from flask import Flask, render_template,request
import os
from machine_learning import train,test

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    y_pred=""
    yp=""
    if request.method=="POST":
        gender = 1 if request.form["gender"]=="Male" else 0
        marride = 1 if request.form["marride"] == "Yes" else 0
        dependents = 4 if request.form["dependents"] == "3+" else int(request.form["dependents"])
        education1 = 0 if request.form["education1"] == "Graduate" else 1
        self_Employed = 1 if request.form["self_Employed"] == "Yes" else 0
        applicantIncome= int(request.form["applicantIncome"])
        coapplicantIncome=int(request.form["coapplicantIncome"])
        loanAmount =int(request.form["loanAmount"])
        loan_Amount_Term= int(request.form["loan_Amount_Term"])
        credit_History =int(request.form["credit_History"])
        urban = 1 if request.form["property_Area"] == "Urban" else 0
        semiurban = 1 if request.form["property_Area"] == "Semiurban" else 0
        if os.path.exists("File/SVM.pickle"):
            y_pred = test(dependents,applicantIncome,coapplicantIncome,loanAmount,loan_Amount_Term,credit_History,gender,education1,semiurban,urban,marride,self_Employed)
        else:
            train()
            y_pred = test(dependents,applicantIncome,coapplicantIncome,loanAmount,loan_Amount_Term,credit_History,gender,education1,semiurban,urban,marride,self_Employed)
        y_pred = y_pred[0]
        yp = str(y_pred)
    return render_template("index.html",x=yp)

if __name__ == "__main__":
    app.run(debug=True)