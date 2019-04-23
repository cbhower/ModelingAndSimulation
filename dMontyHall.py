# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:36:01 2019

@author: User
"""

import numpy as np

class dMontyHall:
    def __init__(self, doors = 3):
        self.doors = doors
        self.prize = np.random.randint(0, doors)
        self.game = np.zeros(3)
        self.game[self.prize] = 1
        self.history = []
        
        
    def first_guess(self):
        # player chooses one of the doors
        guess = np.random.randint(0, self.doors)
        
        return guess
    
    def reveal_goat(self):
        guess = self.first_guess()
        for door in range(self.doors):
            if door != guess:
                if door !=  self.prize:
                    reveal = door
                    break
                
        return reveal, guess

    
    def second_guess(self):
        # keep or change guess
        reveal = self.reveal_goat()




mh = dMontyHall()
mh.game
mh.reveal_goat()