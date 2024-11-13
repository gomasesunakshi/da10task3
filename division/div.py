class secondclass:
    val1 = 0
    val2 = 0


    def __init__(self,value1,value2):
        print('this is constructor')
        self.val1 = value1
        self.val2 = value2
    
    def dividevalue(self):
        print(f'division={self.val1 /self.val2}')

f1 = secondclass(8,9)


f1.dividevalue()
print('f1.val1 = ',f1.val1)
print(f'f1.val2 = {f1.val2}')

f2 = secondclass(20,4)
f2.dividevalue()