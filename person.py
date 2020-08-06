# Copyright MaxAndMitchCorp 2020

import random


class Person:
    def __init__(self):
        # Initiate person model fields.
        self._trust = random.random() - random.random()

    def get_trust(self):
        return self._trust

    def update_trust(self, update):
        self._trust = self._trust + update
