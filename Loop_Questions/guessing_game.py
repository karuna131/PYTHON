number=11
i=1
print()
print('You have 5 π chances for guess the Number ')
print('You have to guess that number between 1 to 20 ')
print()
while (i<=5):
    print('This is your ',i,' chance π')
    num=int(input(' π€ guess number : '))
    print()
    if (number==num):
        print('Great!π₯³π₯³ you guess right number')
        break
    else:
        print('wrong guessπ please try again π')
        print()
    i+=1