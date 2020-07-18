# Copyright MaxAndMitchCorp 2020

import random


class Person():

    def __init__(self):
        # Initiate person model fields - randomly selects from 0 and 1.
        self._trust = random.random()
