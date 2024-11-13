class firstclass:
    value1 =0
    value2 =0

    def __init__(self,a,b):
        print (' this is constructor')
        self.value1 = a
        self.value2 = b
    def divvalue(self):
        print(f'division ={self.value1 * self.value2}')

f1 = firstclass(4,8)

f1.divvalue()
print('f1.value1 =', f1.value1)
print(f'f1.value2 = {f1.value2}')

f2 = firstclass(20,3)
f2.divvalue()