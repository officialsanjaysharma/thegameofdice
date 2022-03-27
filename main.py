# Author: Sanjay Sharma
# In this program we will see how to define a class
import random
import copy
from players import Players


class Game:

    def __init__(self):
        self.main()

    def generatePlayersList(self, number):
        playerList = [];
        playerName = "player_{}"
        for player in range(number):
            playerList.append(Players(playerName.format(player), 0));

        # To create a random player list
        random.shuffle(playerList)

        print("\nHere is the turn sequence\n")

        for player in playerList:
            txt = "Player Name: {}\n"
            print(txt.format(player.name))

        return playerList

    def showDashBoard(self, players_list):
        sortedList = sorted(
            players_list, key=lambda player: player.points, reverse=True);

        print('================Points Table================\n')

        for i in sortedList:
            print("Name: ", i.name, "\tPoints: ", i.points)

        while True:

            key = input("Please press r to continue: ")

            if key == "r":
                break
            else:
                print("Wrong key")
                
        return players_list;

    def turn(self, player, WinningNumber):
        if player.flag == False:
            sum = 0
            turnMessage = "\n -----------{} turn-----------\n"
            print(turnMessage.format(player.name))

            while True:
                key = input("Please press d to roll the dice\n")
                if key == "d":
                    break;
                print("Wrong input!");

            while True:
                dice = random.randint(1, 6);
                if dice != 6:
                    sum = dice;
                    player.prevDice = dice;
                    break
                elif(player.prevDice ==1 and dice == 1):
                    print(
                        "Oh no! You got 1 two consecutive time, you will miss you next turn\n")
                    player.flag = True
                    player.prevDice = 0;
                    break
                else:
                    print("Amazing! You got 6, you got one more change to roll dice\n")
                    sum = sum + 6
                    player.prevDice = "6";
            msg = "\nYou got {}\n"
            print(msg.format(dice))
            points = player.points

            if WinningNumber >= (points + sum):
                player.points = points + sum
            else:
                msg = "You need to get {} to win"
                print(msg.format(WinningNumber - player.points))

        else:
            player.flag = False
        return player

    def main(self):
        while True:
            try:
                playersNumber = int(input("Enter no of players: "));
                if playersNumber <= 1:
                    print("\nPlease enter players more than 1\n")
                else:
                    break
            except:
                print("\nPlease enter a valid input\n")
        WinningNumber = 10
        playersList = self.generatePlayersList(playersNumber)
        pointsTableplayersList = copy.copy(playersList)

        while True:
            if len(playersList) > 1:
                player = playersList.pop(0);
                pointsTableplayersList.pop(0); # This will be utilised for Points Table

                playerAfterTurn = self.turn(player, WinningNumber);
                pointsTableplayersList.append(playerAfterTurn);

                if playerAfterTurn.points != WinningNumber:
                    playersList.append(playerAfterTurn);

                self.showDashBoard(pointsTableplayersList);
            else:
                print("Congratulations to the winners. Game Over!");
                break;
