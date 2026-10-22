name = ""

while name.lower() != "stop":
    name = input("Enter a name (or type 'stop' to quit): ").strip()
    
    
    if name.lower() == "stop":
        print("Loop stopped.")
    else:
        print(f"Hello, {name}!")