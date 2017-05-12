import numpy as np
import random


class standard_spaceship:
    
    # Constructor
    def __init__(self, shields, hull_strength, lasers, name):
        if (shields < 0): # much better!
            shields = 0
        if (hull_strength < 0): # much better!
            hull_strength = 0
                
        self.shields = shields
        self.hull = hull_strength
        self.lasers = lasers
        self.historyType = [] # the type of transaction
        
    def beingHit(self, amount):
        self.shields = self.shields - amount
        if (self.shields < 0):
            self.hull_strength = self.hull_strength - 0.5*amount
        self.historyType.append("beingHit") # record a new transaction of type deposit 
        
    def Hit(self, amount):
        return self.lasers
        self.balance = self.balance - amount
        self.historyType.append("Hit") # record a new transaction of type deposi
        
        
    def getBalance(self):
        return self.balance



class warship(standard_spaceship):

    def Hit(self, amount):
        return self.lasers
        a = random.uniform(0, 10)
        if a<7:
            self.balance = self.balance - amount
        self.balance = self.balance - amount*2
        self.historyType.append("Hit") # record a new transaction of type deposi
        
    
        
                
class speeder(standard_spaceship):
    
    def beingHit(self, amount):
        self.shields = self.shields - amount
        if (self.shields < 0):
            self.hull_strength = self.hull_strength - 0.5*amount
        self.historyType.append("beingHit") # record a new transaction of type deposit
    


# main part of your code

standard_spaceship_info = {'name':'a', 'lasers':100, 'shields': 100, 'hull strength':100}

warship_info = {'name':'b', 'lasers':130, 'shields': 100, 'hull strength':100}

speeder_info = {'name':'c', 'lasers':100, 'shields': 100, 'hull strength':100}

'''
a = standard_spaceship
b = standard_spaceship
c = standard_spaceship
d = warship
e = warship
'''

a = standard_spaceship(100, 100, 100, "a")
b = warship(100, 100, 100, "a")
c = speeder(100, 100, 100, "a")
d = standard_spaceship(100, 100, 100, "a")
e = standard_spaceship(100, 100, 100, "a")


##while( ) # the battle is not over


a.beingHit(50)
a.Hit(50)

b.beingHit(50)
b.Hit(50)


c.beingHit(50)
c.Hit(50)


d.beingHit(50)
d.Hit(50)


e.beingHit(50)
e.Hit(50)
















