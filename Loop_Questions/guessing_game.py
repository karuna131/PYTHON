number=11
i=1
print()
print('You have 5 🖐 chances for guess the Number ')
print('You have to guess that number between 1 to 20 ')
print()
while (i<=5):
    print('This is your ',i,' chance 👍')
    num=int(input(' 🤔 guess number : '))
    print()
    if (number==num):
        print('Great!🥳🥳 you guess right number')
        break
    else:
        print('wrong guess😟 please try again 👇')
        print()
    i+=1