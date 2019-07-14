password = 1234
balance = 2000

chance = 3

code = int(input("Enter the password "))
while chance > 0:
    if password == code:
        print("Press 1 to check the Balance ")
        print('Press 2 to change the Password')
        print("Press 3 to Withdraw ")
        print("Press 4 to Deposit ")
        print("Press 5 to Exit ")

        option = int(input("Enter your choice "))
        if option == 1:
            print("Your balance is ", balance)
            resume = input('Press 0 to exit and 1 to continue banking ')
            if resume == '0':
                break

        if option == 2:
            new_password = int(input("Enter the new Password"))
            confirm = int(input("Enter the password again"))
            if new_password == password:
                print('Old pin & New pin Must not be same')
                resume = input('Press 0 to exit and 1 to continue banking ')
                if resume == '0':
                    break

            elif new_password == confirm:
                print("Your password has been changed")
                resume = input('Press 0 to exit and 1 to continue banking ')
                if resume == '0':
                    break

            else:
                print("password does not match. Please Try again")
                resume = input('Press 0 to exit and 1 to continue banking ')
                if resume == '0':
                    break

        elif option == 3:
            amt = int(input('Enter the amount you want to withdraw '))
            if amt > balance:
                print("Insufficient amount")

                resume = input('Press 0 to exit and 1 to continue banking ')
                if resume == '0':
                    break

            else:
                balance_new = balance - amt
                print("Amount withdraw ", amt)
                print("Balance ", balance_new)

                resume = input('Press 0 to exit and 1 to continue banking ')
                if resume == '0':
                    break

        elif option == 4:
            amt = int(input('Enter the amount you want to Deposit'))
            balance_new = balance_new + amt
            print("Amount Deposited ", amt)
            print("Balance is ", balance_new)

            resume = input('Press 0 to exit and 1 to continue banking ')
            if resume == '0':
                break

        elif option == 5:
            print('Thankyou for Banking With us. Please take your card and Cash Before leaving the ATM')
            break

    else:
        chance = chance - 1
        print("Incorrect code. Try again. You have {} attempts left".format(chance))
        if chance == 0:
            print("Your account has been Blocked")
