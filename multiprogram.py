#Define a class that creates players and keeps track of their scores
class CreatePlayer:
    def __init__(self,playername):
        self.name = playername
        self.score = f'{self.name}\'s score is: '

import random
def myProgram():
    while True:
        menu = '''
        What would you like to do?
        1) Play rock-paper-scissors game
        2) Do some weight conversions
        3) Quit program
        enter 1, 2 or 3
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
            break
        else:
            print('Please enter a valid option from the menu.')
myProgram()

