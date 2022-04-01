import random
def computerguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high(H), too low(L) or correct(C)?').lower()
        if feedback == 'h':
            high = guess-1
            
        elif feedback =='l':
            low = guess +1
    print(f'Your number has been guessed by the computer.')
computerguess(1000)