# Calculator

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")

    a = int(input("Enter between 1 to 5: "))

    if a == 5 :
        print("Thankyou for using calculator.")
        break
    elif a >= 6 or a <= 0:
        print("Invalid")
        break

    b = float(input("Enter the first number: "))
    c = float(input("Enter the second number: "))

    if a == 1:
        print("Addition : ", sum([b,c]))

    elif a == 2:
        print("Subtraction : ", b - c)

    elif a == 3:
        print("Division : ", b/c)
        
    else:
        print("Multiply : ", b*c)