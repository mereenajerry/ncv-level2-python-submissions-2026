marks=[]
i=0
mark=int(input("Enter Mark(or -1 to stop)"))

while mark !=-1:
    marks.append(mark)
    i += 1
    mark=int(input("Enter Mark(or -1 to stop)"))
    
    
    
print(f'Our list has {len(marks)} elements')


total=0
for x in range(len(marks)):
    mark=marks[x]
    total=total+mark
avg=total/len(marks)
print(f'The average of all marks = {avg}') 
    