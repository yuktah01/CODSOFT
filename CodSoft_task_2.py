while True:
    print("USER MANUAL")
    print("select the mathematical operation you would like to perform:")
    print("1, Addition\n2, Subtraction\n3, Multiplication\n4, Division")
    print("type your choice (1/2/3/4)")
    
    choice1 = input("enter your choice: ")
    
    try:
        choice1 = int(choice1)
        
        if choice1 == 1:

            print("type '=' to stop giving input")
            sum = 0
            while True:
                number0 = input("enter number: ")
                if number0 != '=':
                    sum += float(number0)
                else:
                    break
            print("sum is: ", sum)
        
        elif choice1 == 2:

            print("type '=' to stop giving input")
            first_number = float(input("enter number: "))
            while True:
                number0 = input("enter next number: ")
                if number0 != '=':
                    first_number -= float(number0)
                else:
                    break
            print("difference is: ", first_number)
        
        elif choice1 == 3:
            
            print("type '=' to stop giving input")
            product = 1
            while True:
                number0 = input("enter number: ")
                if number0 != '=':
                    product *= float(number0)
                else:
                    break
            print("product is: ", product)
        
        elif choice1 == 4:

            try:
                print("type '=' to stop giving input")
                first_number = float(input("enter number: "))
                while True:
                    number0 = input("enter next number(cannot be 0): ")
                    if number0 != '=':
                        number0 = float(number0)
                        first_number /= number0
                    else:
                        break
                print("answer is:", first_number)
            
            except:
                print("number cannot be divided by zero")
        
        else:
            print("Invalid choice. Please select a valid operation.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")