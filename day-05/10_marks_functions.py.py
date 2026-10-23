# List and Functions
def getMarks():
    marks=[]
    mark=int(input("Enter Mark(or -1 to stop)"))

    while mark !=-1:
        marks.append(mark)
        i += 1
        mark=int(input("Enter Mark(or -1 to stop)"))
    return marks
def print_list_size(marks):
    print(f'Our list has {len(marks)} elements')

def print_marks(marks):
    for x in range(len(marks)):
        print(f'mark{x+1} is {marks[x]}')
        

def determine_highest(marks):
    highest=0
    for i in range(len(mark)):
         current_mark=marks[i]
         if(current_mark > highest):
             highest=current_mark
    print('The highest mark is:', highest)
    
    
menu= 'press 1: Capturing Marks\n'
menu+= 'press 2: Capturing Marks\n'
menu+= 'press 3: Calculating average\n'
menu+= 'press 4: To find highest mark\n'
menu+= 'press -1: To exit\n'

print(menu)
choice=int(input(':Make your choice'))
Entered_marks=[]
while choice !=-1:

    if choice==1:
        Entered_marks=get_marks()
        print(entered_marks)
    elif choice==2:
        print_list_size(entered_marks)
    elif choice==3:
        cal_sum=get_sum_of_marks(entered_marks)
        print('sum of all marks=',cal_sum)
    elif choice==4:
        determine_highest(entered_marks)
    else: print('not on the menu')
print(menu)
choice=int(input(':make your (-1 to exit)'))
    
    
    




    
         