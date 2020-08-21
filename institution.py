# Copyright MaxAndMitchCorp 2020

# Create a class to model the institution. It should have a party composition
# attribute, a method to randomly generate a law to pass (normal distribution)
# and have its party composition update based off of the affiliations of the
# society.

import numpy as np
import random
import matplotlib.pyplot as plt
from society import Society
from person import Person
from law import Law

class Institution:
    
    def __init__(self, society):
        """
        The instiution class primarily generates laws and also has an affiliation
        which will effect partisan trust.

        Fields
        -------
        party_composition:
            The current average party_affilitation of the institution
        law_history:
            A list of lists. Each entry in the law_history is a list of Law objects.
        party_composition_history:
            A list of the party_composition at every simulation step.
        """
        # Initialize fields
        self.party_composition = self._calculate_society_comp(society)
        self.law_history = []
        self.party_composition_history = [self.party_composition]

    def get_affiliation(self):
        return self.party_composition
        
    def _calculate_society_comp(self, society):
        # Loop through the inputed society and calculate the average party
        # affiliation, setting party_compostion to this.
        total_affiliation = 0
        count = 0
        for person_id in range(society.population_size):
            total_affiliation = total_affiliation + society.person_vector[person_id]._party_affiliation
            count = count + 1
        
        if count == 0:
            return 0
        else:
            return total_affiliation/count

    def _generate_laws(self, mean = 0, stdev = 0.5, law_type = 0, number_of_laws = 1):
        # Generate a law(s) to be transformed using tanh, returned as an array.
        # Default params: mean = 0, stdev = 0.5, number_of_laws = 1
        laws = []
        for i in range(number_of_laws):
            law = Law(mean, stdev, law_type)
            laws.append(law)
        if number_of_laws == 0:
            self.law_history.append([])
            return 0
        else:
            self.law_history.append(laws)
            return laws
        
    def _update_party_comp(self, society):
        # No dynamic aspect to affiliation yet in society, but once there is,
        # just _calculate_society_comp
        self._calculate_society_comp(society)
        self.party_composition_history.append(self.party_composition)

    def plot_institution_affiliation_history(self):
        # Similar to society class, plot the affiliation history for the 
        # institution.
        plt.plot(self.party_composition_history, color = 'r')

    def plot_institution_law_history(self):
        # Plot the institution's history of law making
        plt.plot(self.law_history, color = 'r')
