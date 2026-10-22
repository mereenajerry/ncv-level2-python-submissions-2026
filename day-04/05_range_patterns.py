secretnumber=12
attempts=0
guess_correctly=False
while attempts<5 and guess_correctly=false:
    guess=input("Guess a number")
    if guess.isdigit():
        guess_value=int(guess)
        if guess_value<1 and guess_value>20:
            print("The correct range is 1 to 20")
        else:
            attempts+=1
            if guess_value==secretnumber:
                print("Hao, correct!")
                guess_correctly=True
                elif guess_value<secretnumber:
                    print('Too low")
If guessed_correctly==False:
    print(f'failed to guess.secret number is {secret_number}')
                    
                    
                    
                
            
        
    
        
        
    
    
    

