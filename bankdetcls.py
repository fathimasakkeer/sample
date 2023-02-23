class bankac:
    def custdet(self,acname,acno,actype,bal):
        self.acname=acname
        self.acno=acno
        self.actype=actype
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal<amt:
            return false
        else:
            self.bal=self.bal-amt
    def dispcustdet(self):
        print("customer name: ",self.acname)
        print("account number: ",self.acno)
        print("account type: ",self.actype)
        print("balanced amount: ",self.bal)
obj=bankac()
ch=0
while(ch!=5):
    print("**BANK DETAILS**")
    print("1.store customer details")
    print("2.deposit")
    print("3.withdrawal")
    print("4.show customer details: ")
    ch=int(input("enter ur choice: "))
    if ch==1:
        acname=input("enter ur name: ")
        acno=int(input("Enter account number: "))
        actype=input("Enetr account type: ")
        bal=int(input("enter the opening amount: "))
        obj.custdet(acname,acno,actype,bal)
    elif ch==2:
        amt=int(input("Enter deposit amount: "))
        obj.deposit(amt)
    elif ch==3:
        amt=int(input("Enter withdrawal amount: "))
        obj.withdraw(amt)
    elif ch==4:
        obj.dispcustdet()
    else:
        print("Invalid option")
                      
          

        
