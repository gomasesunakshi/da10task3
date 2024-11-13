class firstclass:
    val1 =0
    val2 =0
    
    def __init__(self,value1,value2):
        print('this is constructor')
        self.val1 = value1
        self.val2 = value2

    def addvalue(self):
        print(f'addition ={self.val1+self.val2}')


f1 = firstclass(2,3)

f1.addvalue()

print('f1.val1 =',f1.val1)
print(f'f1.val2 ={f1.val2}')


f2=firstclass(10,20)
f2.addvalue()

