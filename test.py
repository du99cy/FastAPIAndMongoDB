from pydantic import BaseModel

class B:
    x=1
    def sum(self,a,b):
        print(a-b)

class C:
    def sum(self,a,b):
        print(a+b)

class A(B,C):
    a1:int = "string"
    x="2"
    def __init__(self):
        self.a  = 0



a=A()
print(dir(a))
