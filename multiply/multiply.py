class firstclass:
    value1 =0
    value2 =0

    def __init__(self,a,b):
        print('this is constructor')
        self.value1 = a
        self.value2 = b
        

    def mulvalue(self):
        print(f'multiply={self.value1*self.value2}')

f1 =firstclass(4,6)

f1.mulvalue()

print('f1.val1  =', f1.value1)
print(f'f1.val2 = {f1.value2}')

f2 =firstclass(6,1)
f2.mulvalue()