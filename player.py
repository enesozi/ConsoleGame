import random

class Player:
    """Represents a player."""

    # A class variable, counting the number of players
    population = 0
    # A class variable, representing the player who is going to make the first move
    turn = 1
    # A class variable, representing the min damage a player can make
    min_attack_magnitude = 1
    # A class variable, representing the max damage a player can make
    max_attack_magnitude = 50

    def __init__(self, name):
        """Initializes the data."""
        self.__name = name
        self.__health = 100
        Player.population += 1
        self.__id = Player.population
        self.say_hi()

    @property
    def get_name(self):  
        return self.__name

    def set_name(self,name):  
        self.__name = name

    @property
    def get_health(self):  
        return self.__health

    @property
    def get_id(self):  
        return self.__id        

    def attack_to(self, opponent, value):
        opponent.__health -= value

    def say_hi(self):
        """Greeting by the player."""
        print("Greetings, I am {} and my Id is {:d}.".format(self.__name,self.__id))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} players.".format(cls.population))

    @staticmethod
    def coin_toss_for_players():
        return random.randint(1, 2)

    @staticmethod
    def coin_toss_for_attack_chance(damage):
        chance_list = [1] * (100-damage) + [0] * damage
        return random.choice(chance_list)      
          
    def reset_health(self):
        self.__health = 100

    def create_health_bar(self):       
        healths = "HP["+str(self.__health)+"]:"
        for i in range(0,self.__health//2):
            healths += "|"

        return healths