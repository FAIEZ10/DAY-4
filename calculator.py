num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number :"))
choice = int(input("CHOSE AN OPERATOR : 1.+  |  2.-  |  3./  |  4.*  "))
if choice == 1 :
    print(num1 + num2)
elif choice == 2 :
    print(num1 - num2)
elif choice == 3 :
    print(num1 / num2)
else :
    print(num1 * num2)