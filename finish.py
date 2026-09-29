class Paitents:
    def __init__(self,paitentid,name,age,disease,amount):
        self.__id=paitentid
        self.__name=name
        self.__age=age
        self.__disease=disease
        self.__amount=amount

    def agee(self):
        if self.__age>0:
            print("Paitent age:",self.__age)
        else:
            print("age limit is wrong")
    def amounts(self):
        if self.__amount>0:
            print("amount:",self.__amount)
        else:
            print("your amount is invalid")
    def displays(self):
        print("paitent id:",self.__id )
        print("paitent name:",self.__name)
        print("paitent age:",self.__age)
        print("paitent disease:",self.__disease)
        print("remaining amount:",self.__amount)
    def update(self):
        new_amount=int(input("enter a new bill amount"))
        self.__amount+=new_amount
        print("current amount:",self.__amount)

paitentid=int(input("enter a id:"))
name=input("enter a paitent name:")
age=int(input("enter a age:"))
disease=input("enter a disease:")
amount=int(input("enter a amount:"))
obj=Paitents(paitentid,name,age,disease,amount)
while True:
     def main():
        print("1.check age:")
        print("2.enter the amount:")
        print("3.display detials:")
        print("4.update bill amount:")
        check = int(input("enter a check:"))
        if check == 1:
          obj.agee ()
        elif check == 2:
          obj.amounts()
        elif check == 3:
          obj.displays()
        elif check ==4:
          obj.update()
        else:
            print("invalid------------retry")
     main()
