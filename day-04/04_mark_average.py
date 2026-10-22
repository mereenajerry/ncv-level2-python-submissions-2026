# Grade average calculator
total = 0
count = 0

while True:
    try:
        mark = float(input("Enter mark (0-100, -1 to stop): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if mark == -1:
        break
    elif 0 <= mark <= 100:
        total += mark
        count += 1
    else:
        print("Mark out of range. Please enter between 0 and 100.")

if count > 0:
    average = total / count
    print(f"Average mark: {average:.2f}")
else:
    print("No valid marks entered.")