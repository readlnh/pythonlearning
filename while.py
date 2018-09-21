number = 23
running = True

while running:
    guess = int(input('Enter a integer :'))

    if guess == number:
        print('Congratuations, you guessed it.')
        running = False
        #break
    elif guess < number:
        print('No, it is a little higer than that.')
    else:
        print('No, it is a little lower than that')
#随便干什么,如果while里面有break的话，就不会执行这个else
else:
    print('The while loop is over.')

print('Done')