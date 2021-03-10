from flask import Flask, render_template, request
import transactionSplitLogic

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("transactionSplitFrontEnd.html")

@app.route("/enterMoneygroup", methods=['POST'])
def enterMoneyGroup():
    if request.method=='POST':
        groupName=request.form["group_name"]
        password=request.form["password"]
        transactionSplitLogic.create_transaction_group_table()
        group = transactionSplitLogic.select_transaction_group(groupName, password)
        print(group)
        if len(group)==0:
            transactionSplitLogic.insert_transaction_group(groupName, password)
        print(password)
    return render_template("enterMoneyGroup.html")

@app.route("/insertTransactionRecord", methods=['POST'])
def insertTransactionRecord():
    if request.method=='POST':
        personName=request.form["person_name"]
        moneyAmount=request.form["money_amount"]
        groupName = ""
        password = ""
        transactionSplitLogic.create_transaction_record_table()
        transactionSplitLogic.insert_transaction_record(groupName, password, personName, moneyAmount)
        transactions = transactionSplitLogic.select_transactions_records(personName, moneyAmount)
        # finalMap = transactionSplitLogic.splitMoney(transactions)
        print(personName)
        print(moneyAmount)
    return render_template("enterMoneyGroup.html")

if __name__ =="__main__":
    app.run(debug=True)
