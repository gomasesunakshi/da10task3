class secondclass:
    a1 = 0
    b2 = 0

    def __init__(self,a1,b2):
        print('this is my constructor')
        self.a1 = a1
        self.b2 = b2
    def subvalue(self):
        print(f'substract ={self.a1 - self.b2}')


f1 = secondclass(4,5) 

f1.subvalue

print('f1.a1 = ',f1.a1 )
print('f1.b2 = ',f1.b2 )

f2  = secondclass(20,10)
f2.subvalue()
