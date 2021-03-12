from flask import Flask, render_template, request
import transactionSplitLogic
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from itertools import groupby
from pprint import pprint
from collections import ChainMap

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/countryInfoDatabaseTest'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://vjuglmvvkywfyy:a6f2f08524e252210b1f0dfb18eca781ccb53e6a9c3c81d8588cdb6c223567c3@ec2-18-214-208-89.compute-1.amazonaws.com:5432/df4006fs7og0ff?sslmode=require'
db=SQLAlchemy(app)

class DataGroup(db.Model):
    __tablename__="testdata"
    id=db.Column(db.Integer, primary_key=True)
    groupname=db.Column(db.String(120), unique=True)
    password=db.Column(db.String(20))

    def __init__(self, groupname, password):
        self.groupname = groupname
        self.password = password

class DataTrans(db.Model):
    __tablename__="testtrans"
    id=db.Column(db.Integer, primary_key=True)
    groupName=db.Column(db.String(120), unique=False)
    personName=db.Column(db.String(120), unique=False)
    moneyAmount=db.Column(db.Float(), nullable=True)

    def __init__(self, personName, moneyAmount, groupName):
        self.personName = personName
        self.moneyAmount = moneyAmount
        self.groupName = groupName

@app.route('/')
def home():
    return render_template("transactionSplitFrontEnd.html")

@app.route("/enterMoneygroup", methods=['POST'])
def enterMoneyGroup():
    if request.method=='POST':
        groupName=request.form["group_name"]
        password=request.form["password"]
        # transactionSplitLogic.create_transaction_group_table()
        # group = transactionSplitLogic.select_transaction_group(groupName, password)
        # print(group)
        # if len(group)==0:
        #     transactionSplitLogic.insert_transaction_group(groupName, password)
        print(groupName, password)
        if db.session.query(DataGroup).filter(DataGroup.groupname==groupName).count() == 0:
            data=DataGroup(groupName, password)
            db.session.add(data)
            db.session.commit()
            return render_template("enterMoneyGroup.html", textGroup="You successfully created the group.", group_name=groupName)
        elif db.session.query(DataGroup).filter(DataGroup.groupname==groupName, DataGroup.password==password).count() == 0:
            return render_template("transactionSplitFrontEnd.html", textGroup="Your password did not match.")
        else:
            return render_template("enterMoneyGroup.html", textGroup="You successfully entered the group.", group_name=groupName)

@app.route("/insertTransactionRecord", methods=['POST'])
def insertTransactionRecord():
    if request.method=='POST':
        personName=request.form["person_name"]
        moneyAmount=float(request.form["money_amount"])
        groupName = request.form["group_name"]

        password = ""
        # transactionSplitLogic.create_transaction_record_table()
        # transactionSplitLogic.insert_transaction_record(groupName, password, personName, moneyAmount)
        # transactions = transactionSplitLogic.select_transactions_records(personName, moneyAmount)
        # finalMap = transactionSplitLogic.splitMoney(transactions)
        data=DataTrans(personName, moneyAmount, groupName)
        db.session.add(data)
        db.session.commit()
        transRecordList = db.session.query(DataTrans).filter(DataTrans.groupName==groupName).all()
        inputList = []
        for transRecord in transRecordList:
            transRecordObj = {
                'personName': transRecord.personName,
                'moneyAmount': transRecord.moneyAmount,
                'groupName': transRecord.groupName
            }
            inputList.append(transRecordObj)
            print(inputList)
            print(type(inputList))
        finalResult = transactionSplitLogic.paymentSplitting(inputList)
        toPrint = ""
        for dict in finalResult:
            toPrint = toPrint + str(dict)
        return render_template("enterMoneyGroup.html", transactionSplitResult=toPrint)


if __name__ =="__main__":
    app.run(debug=True)
