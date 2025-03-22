num = 20

user = int(input("Enter the number(1 to 100): "))
while True:
    if user in range(1, 101):
        if user > num:
            print('lower')
        elif user < num:
            print('higher')
        elif user == num:
            print('you got it!')
    else:
        print('Invalid')                