import numpy as np
import random


class standard_spaceship:
  #    3 def __init__(self):
    #    self.standard_spaceship = []
    
    # Constructor
    def __init__(self, shields, hull_strength, lasers, name):
        self.standard_spaceship = []
        if (shields < 0): # much better!
            shields = 0
        if (hull_strength < 0): # much better!
            hull_strength = 0       
        self.shields = shields
        self.hull = hull_strength
        self.lasers = lasers
        self.balance = shields, hull_strength, lasers, name
        self.historyType = [] # the type of transaction
        self.historyAmount = []
     
           
    def beingHit(self, amount):
        self.balance = self.shields - amount
        if (self.shields < 0):
            self.hull_strength = self.hull_strength - 0.5*amount
        self.historyType.append("beingHit") # record a new transaction of type deposit 
     
           
    def Hit(self, amount):
        return self.lasers
        self.balance = self.lasers - amount
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
        self.balance = self.shields - amount
        if (self.shields < 0):
            self.hull_strength = self.hull_strength - 0.5*amount
        self.historyType.append("beingHit") # record a new transaction of type deposit
    


# main part of your code

standard_spaceship_info = {'name':'a', 'lasers':100, 'shields': 100, 'hull strength':100}

warship_info = {'name':'b', 'lasers':130, 'shields': 100, 'hull strength':100}

speeder_info = {'name':'c', 'lasers':100, 'shields': 100, 'hull strength':100}


a = standard_spaceship(100, 100, 100, "a")
b = warship(130, 100, 100, "b")
c = speeder(100, 100, 100, "c")
d = standard_spaceship(100, 100, 100, "d")
e = standard_spaceship(100, 100, 100, "e")


##while( ) # the battle is not over


a.beingHit(100)
a.Hit(50)

b.beingHit(130)
b.Hit(50)


c.beingHit(50)
c.Hit(50)


d.beingHit(100)
d.Hit(50)


e.beingHit(100)
e.Hit(50)


print a.getBalance()
print b.getBalance()
print c.getBalance()
print d.getBalance()
print e.getBalance()

list1, list2 = ['standard_spaceship a', 'warship b', 'speeder c', 'standard_spaceship d', 'standard_spaceship e'], [a.getBalance(), b.getBalance(), c.getBalance(), d.getBalance(), e.getBalance()]

print "Max value element : ", max(list1)
print "Max value element : ", max(list2)


## in my example the victor is warship b




