print("welcome to adventure with hashar")
conformation=input('press y if you want to play')
if conformation=='y':
    next_step=input(('you are in front of the deep dark game press w to go forward and Q to quit'))
    if next_step=='w':
        step2=input(('two seprate ways ahead press E to chose right and Q to choose left'))
        if step2=='e':
            step2_1=input(('going right.....\n bear is ahead \n what you want to do \n press r to run back or press f to fight '))
            if step2_1=='f':
                print('nice you have killed the bear \nmission compleated')
            else:
                print('bear attcked you fram the back \n you dumb fuck you cant out run the bear')
        else:
            print('going left...\n whaaaaaaa\n....iam falling .........\n\n you died')
    else:
        print('quiting ...')