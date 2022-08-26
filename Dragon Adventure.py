import random
from time import sleep

# Create a list of Items to be given as Loot
loot_table = ["A Wood Sword","A Silver Cup","A Great Shield",
              "500 Gold","Gold Armor","A Golden Sword","1000 Gold",
              "A King's Crown","A Large Ruby"]

# Create a list of Dragon Names to pull from
dragon_names = ["Askook","Apophis","Belinda","Leviathan","Thorn","Drakon","Fred","Fafnir"]

# Create a class for the Player that has the attributes name and health
class Player:
    def _init_(self,name,hp):
        self.name = name
        self.hp = hp

# Create a base class for Dragons that has the attributes level and name
class Dragon:
    def _init_(self,level,name):
        self.level = level
        self.name = name
    
    # Create a method for calculating the dragons total HP based on its level
    def calc_health(self):
        return self.level*20
    
    # Create a method that returns a random item from out loot table
    def calc_loot(self):
        return loot_table[random.randint(0,8)]

    # Create a method that returns the amount and type of damage the dragon does with its attack
    def attack(self):
        return str(random.randint(1,20)*self.level)

    # Create a method that returns the dragon's name and title
    def title(self):
        return self.name +  " the mighty!"

# Create a child class for a Fire Dragon that makes use of our Dragon Class\Dan
# but has a different type of damage and title
class Fire_Dragon(Dragon):
    def _init_(self,level,name):
        super()._init_(level,name)
        
    def attack(self):
        return super().attack() + " Fire"
    
    def title(self):
        return self.name + ", Lord of the Flames!"

#These other child classes are almost identical to Fire_Dragon
class Ice_Dragon(Dragon):
    def _init_(self,level,name):
        super()._init_(level,name)
        
    def attack(self):
        return super().attack() + " Ice"
    
    def title(self):
        return self.name + ", Lord of the Ice!"

class Lightning_Dragon(Dragon):
    def _init_(self,level,name):
        super()._init_(level,name)
        
    def attack(self):
        return super().attack() + " Lightning"
    
    def title(self):
        return self.name + ", Lord of the Storms!"

#//You can ignore this function//
def onlyNumeric(string):
    '''
    # This function is just being used to convert our attack methods back to the
    # damage value by substituting all non-number characters for blank spaces the 
    # converting the type to int.
    '''
    damage = ''.join(ch for ch in string if ch.isdigit())
    return int(damage)

#Create a variable to track if the user wants to keep playing
continueGame = "Y"

#This is our main game loop
while(continueGame == "Y" or continueGame == "y"):

    # Create a list of dragon types to choose from
    dragon_types = [Dragon,Ice_Dragon,Fire_Dragon,Lightning_Dragon]

    # Choose a random index of that list
    enemy = dragon_types[random.randint(0,3)]()

    # Set the enemy level as a random level from 1-10
    enemy.level = random.randint(1,10)

    # Set the enemy name as a random name
    enemy.name = random.choice(dragon_names)

    # Set the enemy health by calculating it
    enemy.health = enemy.calc_health()
                                        

    print("Welcome to Dragon Adventure!")
    sleep(0.5)

    #Ask for the players name and save it to an instance of the Player Class
    name = input("What is your name Hero?: ")
    print("Hello " + name +"!")
    player = Player()
    player.name = name

    #Set Player hp to 100
    player.hp = 100

    print("HP: "+ str(player.hp))
    sleep(0.5)
    print("You begin your journey across far reaching fields and mountains but your peaceful adventure is interrupted by a great roar!")
    sleep(0.5)
    print("Before you stands the Great Dragon " + enemy.title())

    # Seeing a bunch of '\n' in the print statement might be strange but remember it just tells python we want to go to the next line
    choice = input("Will you:\n A: Fight the Dragon\n or\n B: Run Away\n")
    
        #Use a loop to continue the fight until one side loses or flees
    while( choice == "A" or choice == "a"):

        #Calculate the players damage as a random int from 1-100
        my_damage = random.randint(1,100)

        #Save the enemy damage calculated from the attack method to a variable
        enemy_damage = enemy.attack()

        #Print out the player attack on the Dragon
        print("You attack the Dragon and deal " + str(my_damage)  + " Damage!")

        #Calculate the enemy's new HP
        enemy.health = enemy.health - my_damage

        #Check if the dragon has been defeated
        if enemy.health <= 0:
            print("You have defeated " + enemy.title()+ "!")
            sleep(0.5)
            print("You find his treasure filled cave nearby and it contains " + enemy.calc_loot())
            sleep(0.5)
            print("You win!")
            break
        else:
            sleep(1)
            #Print out the Dragon's attack on the player
            print(enemy.name + " retaliates and deals " + enemy_damage + " Damage!")
            #Set the player's new HP
            player.hp = player.hp - onlyNumeric(enemy_damage)
        
        #Check if the Player has been defeated
        if player.hp <= 0:
            sleep(0.5)
            print("You have been defeated and your journey has come to an end,\n Game Over")
            break
        else:

            #Print out the new HP and ask if they want to keep fighting
            sleep(0.5)
            print("HP: "+ str(player.hp))
            sleep(0.5)
            choice = input("Will you:\n A: Keep Fighting the Dragon\n or\n B: Run Away\n")
    if choice == "B" or choice == "b" :
        #Check if the player gets away with a random 70% chance
        if random.randint(1,10)> 3:
            sleep(0.5)
            print("You escape and continue your journey empty handed.")
        else:
            sleep(0.5)
            print("The dragon caught you as you tried to escape.\nGame Over")
    #Ask if they want to keep playing
    sleep(0.5)
    continueGame = input('Play Again? Y/N \n')

