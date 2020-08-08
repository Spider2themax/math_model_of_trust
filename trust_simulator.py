# Copyright MaxAndMitchCorp 2020

import numpy as np
import random


class TrustSimulator:
    """
    This class will perform the trust simulations of a given society.
    """
    def __init__(self):
        pass

    def simulate_society(self, society, iterations, affiliation_prob = 0.5):
        """
        This is the main function for simulating the institutional trust of an
        entire society. The simulation will be ran by updating each invididual
        person in the society according to an udpate rule for a number of
        iterations.
        """
        # Initialize list for saving societal trust at each iteration.
        societal_trust = []
        for iteration in range(iterations):
            # Determine an update in trust based on 
            trust_updates = []
            for person_id in range(society.population_size):
                trust_updates.append(self._calculate_trust_update(society=society,
                                                                  person_id=person_id))
            #print(trust_updates)
            # Update societal trust.
            society = self._update_societal_trust(society=society,
                                                  trust_updates=trust_updates)
            # Save current overall societal trust.
            societal_trust.append(np.mean([society.person_vector[person_id].get_trust() for person_id in range(society.population_size)]))
            
            # Reset trust_updates each iteration
            trust_updates = []
            # Update edge matrix
            society = self._update_edge_matrix(society = society, affiliation_prob = affiliation_prob)
        return societal_trust

    def _calculate_trust_update(self, society, person_id, K=1, alpha=1):
        """
        This function calculates updates for a particular person in the society.
        """
        update = 0.0
        for j in range(society.population_size):
            if person_id != j:
                # Using update equation for now from Baumann 2020.
                update = update + K * society.edge_matrix[person_id][j] * np.tanh(alpha * society.person_vector[j].get_trust())
        return -update + society.person_vector[person_id].get_trust()

    def _update_societal_trust(self, society, trust_updates):
        for person_id in range(society.population_size):
            society.person_vector[person_id].update_trust(update=trust_updates[person_id])
        return society
    
    def _update_edge_matrix(self, society, affiliation_prob = 0.5):
        # Loop through each entry in the edge matrix. On diagonal elements 
        # always remain 1 since all nodes are connected with themselves. For
        # all other connections, if the nodes are further in affiliation, have
        # the edge update be more likely to not connect. 
        for person_id_first in range(society.population_size):
            for person_id_second in range(society.population_size):
                if person_id_first == person_id_second:
                    society.edge_matrix[person_id_first][person_id_second] = 1
                else:
                     # Compute party affiliation difference
                    party_delta = society.person_vector[person_id_first]._party_affiliation - society.person_vector[person_id_second]._party_affiliation
                    party_delta = abs(party_delta)
                    
                    # Further apart affiliation, less likely to connect.
                    # party_delta maximum of 2, so divided by 2 and taking
                    # the complement gives a reasonable discount.
                    adjusted_connectivity_probability = (1 - (party_delta)/2) * affiliation_prob
                    
                    connect = random.random()
                    
                    if connect <= adjusted_connectivity_probability:
                        society.edge_matrix[person_id_first][person_id_second] = 1
                    else:
                        society.edge_matrix[person_id_first][person_id_second] = 0
        return society
               
