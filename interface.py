from flask import Flask, jsonify, render_template, request 
import config
import numpy as np
from project_app.utils import MedicalInsurance

#########
app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

    # return "home page"


@app.route("/charge")
def get_charge():
    # when to read data from html
    age1 = request.args.get('age')
    sex1=request.args.get("sex")
    bmi1=request.args.get("bmi")
    children1 = request.args.get("children")
    smoker1=request.args.get("smoker")
    region1=request.args.get("region")
    print(age1,sex1,bmi1,children1,smoker1,region1)
    med_ins = MedicalInsurance(age1,sex1,bmi1,children1,smoker1,region1)
    
    # when to read hard coded input
    # age = 19
    # sex ='male'
    # bmi=27.9
    # children = 1
    # smoker='yes'
    # region='southwest'
    # med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)


    charges= med_ins.get_charges_insurance()
    return jsonify({"Return" : f"Predicted medical isurance charges are :{charges}"})


if __name__=="__main__":
    app.run()

