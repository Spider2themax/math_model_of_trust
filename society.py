# Copyright MaxAndMitchCorp 2020

import matplotlib.pyplot as plt
from person import Person
import numpy as np
import random


class Society:
    """
    Upon instantiation, data fields are:
    population_size:double
    connectivity_probability:double
    edge_matrix:(population_sizexpopulation_size)double
    person_vector:(population_size)double
    Interpretation of the edge_matrix:
    Entry in row i, column j, represents the presence of an edge from node
    i+1 to node j+1 (since indices start at 0).
    """
    def __init__(self, population_size=25, connectivity_probability=0.1):

        self.population_size = population_size
        self.connectivity_probability = connectivity_probability
        self.edge_matrix = self._generate_edge_matrix()
        self.person_vector = self._generate_society_constituents()

    def _generate_society_constituents(self):
        return [Person() for x in range(self.population_size)]

    def _generate_edge_matrix(self):
        edge_matrix = np.zeros((self.population_size, self.population_size)).tolist()
        for x in range(self.population_size):
            for y in range(self.population_size):
                # Diagonal elements should all be 1, as each node is connected
                # to itself.
                if x == y:
                    edge_matrix[x][y] = 1
                else:
                    if float(random.random()) <= self.connectivity_probability:
                        edge_matrix[x][y] = 1
        return edge_matrix

    def plot_society_trust_histories(self):
        for person in self.person_vector:
            signal = np.array(person._trust_history)
            pos_signal = signal.copy()
            neg_signal = signal.copy()
            
            pos_signal[pos_signal <= 0] = np.nan
            neg_signal[neg_signal > 0] = np.nan
            
            #plotting
            plt.style.use('fivethirtyeight')
            plt.plot(pos_signal, color='r')
            plt.plot(neg_signal, color='b')