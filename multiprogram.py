#Define a class that creates players and keeps track of their scores
class CreatePlayer:
    def __init__(self,playername):
        self.name = playername
        self.score = f'{self.name}\'s score is: '
import pywhatkit

def send_whatsapp_message():
    cell_phone_number = input('Enter receipient\'s number')
    print()
    message = input('Enter message: ')
    print()
    time = input('Enter time of delivery in format(e.g.13,43)')
    
    splitted_time = time.split(',')
    
    hour = int(splitted_time[0])
    
    minute = int(splitted_time[1])
    
    pywhatkit.sendwhatmsg(f'+234{cell_phone_number}', message, hour, minute)

    import pywhatkit as kit
def seach_song_on_youtube():
    search = input('What do you want to search for on youtube?')
            
    kit.playonyt(search)

def search_on_google():
    search_google = input('What do you want to search for on google')
    kit.search(search_google)
def get_info():
    enquiry = input('What do you need more info on?')
    kit.info(enquiry)


import random
def myProgram():
    while True:
        menu = '''
        What would you like to do?
        1) Play rock-paper-scissors game
        2) Do some weight conversions
        3) Play a game where the computer tries to guess the number you choose
        4) Send a whatsapp message
        5) Play a song on youtube
        6) Do a google-search
        7) Get some info without opening a web browser
        8) Quit program
        Enter the integer that comes before an option to select that option
        '''
        print(menu)
        response = str(input())
        if response == '1':
        # ask the player for their name and save it to a variable
            print('Welcome to the rock-paper-scissors game.')
            print('Player, please enter your name below: ')
            name = input()

        # Use the entered name to instantiate our CreatePlayer class
            user1 = CreatePlayer(name)
            Computer = CreatePlayer('Computer')
        
        # create a list of the possible choices that could be made
            choices = ['rock', 'paper','scissors']
        # define variables that keep track of the player and computer's scores
            playerscore = 0
            computerscore = 0
            # this keeps track of the number of rounds
            times = 1    
            while times < 4:
                # print a menu that asks the user what they want to do
                print('''
                1) Check current scores
                2) End game
                3)Continue playing
                enter 1, 2 or 3
                ''')
                # collect the user's reply
                reply = input()
                if reply == '1':
                    print(user1.score + str(playerscore))
                    print(Computer.score + str(computerscore))
                elif reply == '2':
                    break
                elif reply == '3':
                    playerinput = input('rock, paper or scissors?: ').lower()
                    computerchoice = choices[random.randint(0, 2)]
                
                    if playerinput == 'rock':
                        if computerchoice == 'paper':
                            print('computer chose paper')
                            print('Paper beats rock so computer gets one point')
                            computerscore += 1
                            times += 1
                        
                        elif computerchoice == 'scissors':
                            print('computer chose scissors')
                            print('Rock beats scissors so player gets one point')
                            playerscore += 1
                            times += 1
                        continue
                    elif computerchoice == playerinput:
                        print('computer chose ' + computerchoice)
                        print('This is a draw so zero points are rewarded.')
                        continue
                    elif playerinput == 'paper':
                        
                        if computerchoice == 'rock':
                            print('computer chose rock')
                            print('Paper beats rock so player gets one point')
                            playerscore += 1
                            times += 1
                            
                        elif computerchoice == 'scissors':
                            print('computer chose scissors')
                            print('scissors beats paper so computer gets one point')
                            computerscore += 1
                            times += 1
                        continue
                    elif playerinput == 'scissors':

                        if computerchoice == 'paper':
                            print('computer chose paper')
                            print('scissors beats paper so computer gets one point')
                            playerscore += 1
                            times += 1
                            
                        elif computerchoice == 'rock':
                            print('computer chose rock')
                            print('Rock beats scissors so computer gets one point')
                            computerscore += 1
                            times += 1
                        continue
            if playerscore >= 2:
                print(f'{user1.name} has won')
                
            elif computerscore >= 2:
                print('Computer has won')               
        elif response == '2':
            user_weight = float(input('weight:'))
            while True:
                setunit = input('''what is the unit of the weight you entered?
                                 pounds(l) or kilos(k)? ''')

                if setunit.lower() == 'k': 
                    weight = user_weight * 2.20462
                    print(f'your weight in pounds is {weight}')
                    break

                elif setunit.lower() == 'l':
                    weight = user_weight * 0.4535
                    print(f'your weight in kilos is {weight}')
                    break

                else:
                    print('wrong input!!! Please input l or k')
            continue
        elif response == '3':
            print('''In this game, the user chooses a number in their head, and they set 
            the highest possible value the computer can look through and the computer tries to narrow 
            down and eventually get the user\'s number. ''')
            print('\n')
            print('\n')
            # set the lowest value in the range of the numbers the computer will look through to zero
            lowestnum  = 0
            # collect the highest possible number in the range of values
            highestnum = int(input('''What\'s the highest possible number in a your range of
            values you want the computer to look through? '''))
            # feedback will store the replies of the user
            feedback = ''
            while feedback != 'c':
                if lowestnum != highestnum:
                    computerguess = random.randint(lowestnum, highestnum)
                else:
                    computerguess = lowestnum #could also be highestnum because lowestnum=highestnum
                feedback = input(f'Is {computerguess} too high(H), too low(L) or correct(C)?').lower()
                if feedback == 'h':
                    highestnum = computerguess - 1
            
                elif feedback =='l':
                    lowestnum = computerguess + 1
            print(f'Your number, {computerguess}, has been guessed by the computer.')
        elif response == '4':
            send_whatsapp_message()
            continue
        elif response == '5':
            seach_song_on_youtube()
            continue

        elif response == '6':
            search_on_google()
            continue

        elif response == '7':
            get_info()
            continue
        elif response == '8':
            break
        else:
            print('Please enter a valid option from the menu.')
myProgram()


