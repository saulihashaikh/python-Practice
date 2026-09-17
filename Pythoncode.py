# print('Hi i am learning python')



# MAKING A CALCULATOR
print("a is for +")
print("b is for -")
print("c is for *")
print("d is for /")
print("e is for %")
print("f is for //")
print("j is for **")
n1=int(input())
n2=int(input())
opr=input("operator:")
if(opr=='a'):
    print(n1+n2)
elif(opr=='b'):
    print(n1-n2)
elif(opr=='c'):
    print(n1*n2)
elif(opr=='d'):
    print(n1/n2)
elif(opr=='e'):
    print(n1%n2)
elif(opr=='f'):
    print(n1//n2)
elif(opr=='j'):
    print(n1**n2)    