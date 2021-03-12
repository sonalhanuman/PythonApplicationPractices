from itertools import groupby
from pprint import pprint
from collections import ChainMap

def paymentSplitting(transRecordList):
    finalList = []
    filteredList = []
    accumulateSum=0.00
    NameList = []
    filteredList = []
    for transRecord in transRecordList:
        print("Hello hi hi" + str(transRecord))
        NameList.append(transRecord.get("personName"))
        uniqueNameList = list(set(NameList))
        print(uniqueNameList)

    for name in uniqueNameList:
        personMoney = 0.00
        for transRecord in transRecordList:
            if name == transRecord.get("personName"):
                personMoney = personMoney + transRecord.get("moneyAmount")
        dict = {"personName": name, "amountPaid": personMoney}
        filteredList.append(dict)
    print("this is filtered list hello" + str(filteredList))
    for transRecord in filteredList:
        print("this is how much money per payment" + str(transRecord.get("amountPaid")))
        accumulateSum = accumulateSum + transRecord.get("amountPaid")
    averagePerPerson = accumulateSum/(len(filteredList))

    for transRecord in filteredList:
        balance = transRecord.get("amountPaid") - averagePerPerson
        finalList.append({"personName": transRecord.get("personName"), "amountPaid": transRecord.get("amountPaid"), "balance": balance})

    print("the final list ever" + str(finalList))
    return finalList