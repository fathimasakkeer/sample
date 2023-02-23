import datetime
class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,obj):
        return datetime.timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)+ datetime.timedelta(hours=obj.hour,minutes=obj.minute,seconds=obj.second)
h1=int(input("Enter 1st time hour: "))
h2=int(input("Enter 2nd time hour: "))
m1=int(input("Enter 1st time minute: "))
m2=int(input("Enter 2nd time minute: "))
s1=int(input("Enter 1st time second: "))
s2=int(input("Enter 2nd time second: "))
obj1=time(h1,m1,s1)
obj2=time(h2,m2,s2)
print(obj1+obj2)
