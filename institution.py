# Copyright MaxAndMitchCorp 2020

# Create a class to model the institution. It should have a party composition
# attribute, a method to randomly generate a law to pass (normal distribution)
# and have its party composition update based off of the affiliations of the
# society.

import numpy as np
import random
from society import Society
from person import Person

class Institution:
    
    def _init_(self, society):
        self.party_compostion = 0
        self._calculate_society_comp(society)
        
    def _calculate_society_comp(self, society):
        # Loop through the inputed society and calculate the average party
        # affiliation, setting party_compostion to this.
        total_affiliation = 0
        count = 0
        for person_id in range(society.population_size):
            total_affiliation = total_affiliation + society.person_vector[person_id]._party_affiliation
            count = count + 1
        
        if count == 0:
            self.party_compostion = 0
        else:
            self.party_composition = total_affiliation/count
    
    def _generate_law(self, mean = 0, stdev = 0.5):
        # Generate a law to be transformed using tanh based on a normal distribution.
        # Default params: mean = 0, stdev = 0.5
        # Note: already returns the tanh value
        law = np.random.normal(loc = mean, scale = stdev)
        return np.tanh(law)
        
    def _update_party_comp(self, society):
        # No dynamic aspect to affiliation yet in society, but once there is,
        # just _calculate_society_comp
        self._calculate_society_comp(society)


