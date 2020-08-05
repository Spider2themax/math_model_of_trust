# Copyright MaxAndMitchCorp 2020

import random


class Person:
    def __init__(self):
        # Initiate person model fields.
        self._trust = random.random() - random.random()
        # Make sure that trust score remains in the interval [0,1] 
        if self._trust < 0:
            self._trust = 0
        if self._trust > 1:
            self._trust = 1

    def get_trust(self):
        return self._trust

    def update_trust(self, update):
        self._trust = self._trust + update
        # Make sure that trust score remains in the interval [0,1] 
        if self._trust < 0:
            self._trust = 0
        if self._trust > 1:
            self._trust = 1
