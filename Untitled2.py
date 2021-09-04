#!/usr/bin/env python
# coding: utf-8

# In[63]:


import random

class player():
    def __init__(self, name, exp, level, hp, gold, cweapon, currentworld):
        self.name = name
        self.exp = exp
        self.level = 0
        self.hp = hp
        self.gold = gold
        self.cweapon = cweapon
    def leveup(self):
        if player.exp == 100 :
            print("level up")
            player.level + 1
            player.exp = 0

class world():
    def __init__(self, id, name, temp, terrain):
        self.id = id
        self.name = name
        self.temp = temp
        self.terrain = terrain
    def rtemp(self):
        self.temp = (random.randrange(0, 1000, 3))
    def rname(self):
            length = 10
            your_letters='abcdefghizxfh'
            self.name = "" .join((random.choice(your_letters) for i in range(length)))
    def rterrain(self): 
            list  = ["ocean", "rocky", "high resources", "decaying", "poisonous"]
            self.terrain = (random.choice(list))
#temp = (random.randrange(0, 1000, 3))
w1 = world(1, "name", temp, "terrain")
w2 = world(2, "name", temp, "terrain")
w2.rtemp()
w2.rterrain()
w1.rterrain()
w2.rname()
w1.rname()
w1.rtemp()

name = input("player name: ")
list = [w1, w2]
currentworld = (random.choice(list))
print(currentworld)

player1 = player(name, 0, 0, 10, 0, "none", cworld) 
print(player1.name)
print(currentworld)
#print (w2.terrain)
#print(w2.name)
#print(w2.temp)
#print(w2)
        
        
  
# using choice() to generate a random number from a  
# given list of numbers. 
#print ("A random number from list is : ",end="") 
#print (random.choice([1, 4, 8, 10, 3])) 
  
# using randrange() to generate in range from 20 
# to 50. The last parameter 3 is step size to skip 
# three numbers when selecting. 
#print ("A random number from range is : ",end="") 
#print (random.randrange(0, 1000, 3)) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




