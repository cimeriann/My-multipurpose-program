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
        1) Play rock-paper-scissors-game
        2) Quit program
        enter 1 or 2
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
        
            choices = ['rock', 'paper','scissors']
            # gameon = True
            playerscore = 0
            computerscore = 0
            # this keeps track of the number of rounds
            times = 1 
            # while gameon:    
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
                        # print('you chose rock')
                        
                        if computerchoice == 'paper':
                            print('computer chose paper')
                            print('Paper beats rock so computer gets one point')
                            computerscore += 1
                            times += 1
                            # continue
                            
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
                        # print('you chose paper')
                        
                        if computerchoice == 'rock':
                            print('computer chose rock')
                            print('Paper beats rock so player gets one point')
                            playerscore += 1
                            times += 1
                            # continue
                        elif computerchoice == 'scissors':
                            print('computer chose scissors')
                            print('scissors beats paper so computer gets one point')
                            computerscore += 1
                            times += 1
                        continue
                    elif playerinput == 'scissors':
                        # print('you chose scissors')
                        
                        if computerchoice == 'paper':
                            print('computer chose paper')
                            print('scissors beats paper so computer gets one point')
                            playerscore += 1
                            times += 1
                            # continue
                        elif computerchoice == 'rock':
                            print('computer chose rock')
                            print('Rock beats scissors so computer gets one point')
                            computerscore += 1
                            times += 1
                        continue
            if playerscore >= 2:
                print('Player has won')
                
            elif computerscore >= 2:
                print('Computer has won')               
        elif response == '2':
            break
myProgram()


