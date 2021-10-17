# BINARY SERCH
low = 1
high = 1000
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess was {} should is guess higher or lower or is it correct ".format(guess)).casefold()
    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print("i got it correct in {} tries".format(guesses))
        break
    guesses += 1
