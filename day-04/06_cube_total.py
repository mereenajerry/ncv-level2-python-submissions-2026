import math
num=int(input("Enter a positive whole number:"))
Total=0

for num in range(1,num+1):
    cube=math.pow(num,3)
    print("The cube is:", cube)
    Total=Total+cube
print("total:",Total)