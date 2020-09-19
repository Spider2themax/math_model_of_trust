# Copyright MaxAndMitchCorp 2020

import random


class Person:
    def __init__(self):
        # Initiate person model fields.
        self._trust = random.random() - random.random()
        self._party_affiliation = random.random() - random.random()
        self._trust_history = [self._trust]
        self._affiliation_history = [self._party_affiliation]

    def get_trust(self):
        return self._trust

    def get_affiliation(self):
        return self._party_affiliation

    def update_trust(self, update):
        self._trust = self._trust + update
        self._trust_history.append(self._trust)

    def update_party_affiliation(self, update):
        self._party_affiliation = self._party_affiliation + update
        self._affiliation_history.append(self._party_affiliation)
