import PasswordHolderFunc

Function = input("What function do you want to use?: ")

if Function == "Add" or Function == "add":
    PasswordHolderFunc.add()
elif Function == "Find" or Function == "find":
    PasswordHolderFunc.find()
