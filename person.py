# Copyright MaxAndMitchCorp 2020

import random


class Person:
    def __init__(self):
        # Initiate person model fields.
        self._trust = random.random() - random.random()
        self._party_affiliation = random.random() - random.random()
        self._trust_history = [self._trust]

    def get_trust(self):
        return self._trust

    def update_trust(self, update):
        self._trust = self._trust + update
        self._trust_history.append(self._trust)
