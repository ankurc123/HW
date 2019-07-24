password = [1234]
balance = [2000]
chance = 3

while chance > 0:
    code = input('Enter your ATM Pin: ')
    assert (len(code) == 4), 'Please Try Again and Give 4 Only Digits'
    code = int(code)
    if code == password[-1]:
        print('Please select from the following options: ')
        print('1. Press 1 to check the Balance  ')
        print('2. Press 2 to change the Password')
        print('3. Press 3 to Deposit Money')
        print('4. Press 4 to Withdraw Money')
        print('5. Press 5 to Exit')
        opt = input('Please enter the desired choice: ')
        assert (len(opt) == 1), 'Please Try Again and Give 1 Only Digits'
        opt = int(opt)

        if opt == 1:
            print('Your current balance is', balance[-1])
            resume = input('Press 0 to exit and 1 to continue banking ')
            assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
            resume = int(resume)
            if resume == 0 or resume > 1:
                break

        elif opt == 2:
            code1 = int(input('Please enter new pin: '))
            code2 = int(input('Please confirm new pin: '))

            if code1 == code:
                print('Old Pin and New Pin must not be same')
                resume = input('Press 0 to exit and 1 to continue banking ')
                assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
                resume = int(resume)
                if resume == 0 or resume > 1:
                    break

            elif code1 == code2:
                print('Your pin is changed')
                password[-1] = code2
                resume = input('Press 0 to exit and 1 to continue banking ')
                assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
                resume = int(resume)
                if resume == 0 or resume > 1:
                    break

            else:
                print('Pin and confirm Pin Must be same')
                resume = input('Press 0 to exit and 1 to continue banking ')
                assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
                resume = int(resume)
                if resume == 0 or resume > 1:
                    break

        elif opt == 3:
            amt = int(input('Please enter the amount you want to deposit: '))
            balance[-1] = amt + balance[-1]
            print('your new balance is: ', balance[-1])
            resume = input('Press 0 to exit and 1 to continue banking ')
            assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
            resume = int(resume)
            if resume == 0 or resume > 1:
                break

        elif opt == 4:
            amt = int(input('Please enter the amount you want to withdraw: '))
            if amt > balance[-1]:
                print('insufficient balance')
                resume = input('Press 0 to exit and 1 to continue banking ')
                assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
                resume = int(resume)
                if resume == 0 or resume > 1:
                    break

            else:
                balance[-1] = balance[-1] - amt
                print('Your new balance is: ', balance[-1])
                print('Please collect your card and cash before leaving the ATM')
                resume = input('Press 0 to exit and 1 to continue banking ')
                assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
                resume = int(resume)
                if resume == 0 or resume > 1:
                    break

        elif opt == 5:
            print('Thankyou for banking with us. Have a nice day')
            break

        else:
            print('Please give proper input')
            resume = input('Press 0 to exit and 1 to continue banking ')
            assert (len(resume) == 1), 'Please Try Again and Give 1 Only Digits'
            resume = int(resume)
            if resume == 0 or resume > 1:
                break

    else:
        chance -= 1
        print('Wrong Pin. Please try again.', chance, 'is left')
        if chance == 0:
            print('Your card is blocked. Please try after 24 hrs')
            break
