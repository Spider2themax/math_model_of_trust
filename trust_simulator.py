# Copyright MaxAndMitchCorp 2020

import numpy as np
import random
from society import Society
from person import Person


class TrustSimulator:
    """
    This class will perform the trust simulations of a given society.
    """
    def __init__(self):
        pass

    def simulate_society(self, society, institution, iterations, K=1, J=1, alpha=1, affiliation_prob = 0.5, mean = 0, stdev = 0.5, law_type = 'G', number_of_laws = 1, beta = 0):
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
            # Note: In order to replicate Twitter paper, forcing laws to be 
            # zero each iteration.
            laws = institution._generate_laws(society=society, mean = mean, stdev = stdev, law_type = law_type, number_of_laws = 0)
            for person_id in range(society.population_size):
                trust_updates.append(self._calculate_trust_update(society=society,
                                                                  institution=institution,
                                                                  person_id=person_id,
                                                                  laws = laws,
                                                                  K=K,
                                                                  J=J,
                                                                  alpha=alpha))
            #print(trust_updates)
            # Update societal trust.
            society = self._update_societal_trust(society=society,
                                                  trust_updates=trust_updates)
            # Save current overall societal trust.
            societal_trust.append(np.mean([society.person_vector[person_id].get_trust() for person_id in range(society.population_size)]))
            
            # Reset trust_updates each iteration
            trust_updates = []
            # Update edge matrix
            society = self._update_edge_matrix(society = society, affiliation_prob = affiliation_prob, beta = beta)
            # Update society's party affiliations
            society = self._update_society_party(society = society, J=J, alpha=alpha)
            # Update institution composition
            institution._update_party_comp(society = society)
        return societal_trust

    def _calculate_trust_update(self, society, institution, person_id, laws, K=1, J=1, alpha=1):
        """
        This function calculates updates for a particular person in the society.
        """
        update = 0.0
        for j in range(society.population_size):
            if person_id != j:
                # Using update equation for now from Baumann 2020.
                update = update + K * society.edge_matrix[person_id][j] * np.tanh(alpha * society.person_vector[j].get_trust())
        # Have the laws positively update those who share the affiliation of the 
        # institution, and negatively affect the opposite.
        for law in laws:
            update = update + J * law.affected_persons[person_id] * np.tanh(alpha * law.actual_value)
                
        return update - society.person_vector[person_id].get_trust()

    def _update_societal_trust(self, society, trust_updates):
        for person_id in range(society.population_size):
            society.person_vector[person_id].update_trust(update=trust_updates[person_id])
        return society
    
    def _update_edge_matrix(self, society, affiliation_prob = 0.2, beta = 0):
        # Loop through each entry in the edge matrix. On diagonal elements 
        # always remain 1 since all nodes are connected with themselves. For
        # all other connections, if the nodes are further in affiliation, have
        # the edge update be more likely to not connect. 
        for person_id_first in range(society.population_size):
            for person_id_second in range(society.population_size):
                if person_id_first == person_id_second:
                    society.edge_matrix[person_id_first][person_id_second] = 1
                else:
                    # This is not the way the transition probabilities were 
                    # done in the paper, but another way. Uncommented section
                    # is the one for the paper.
                    
                    # Compute party affiliation difference
                    #party_delta = np.tanh(society.person_vector[person_id_first]._party_affiliation) - np.tanh(society.person_vector[person_id_second]._party_affiliation)
                    #party_delta = abs(party_delta)
                    
                    # Further apart affiliation, less likely to connect.
                    # party_delta maximum of 2, so divided by 2 and taking
                    # the complement gives a reasonable discount.
                    #adjusted_connectivity_probability = (1 - (party_delta)/2) * affiliation_prob
                    
                    # Compute total sum of denominator in paper
                    sum_for_prob = 0
                    for person_id_third in range(society.population_size):
                        if person_id_third != person_id_first:
                            sum_for_prob += abs(society.person_vector[person_id_first].get_trust() - society.person_vector[person_id_third].get_trust()) ** (-beta)
                    
                    numerator_for_prob = abs(society.person_vector[person_id_first].get_trust() - society.person_vector[person_id_second].get_trust()) ** (-beta)
                    adjusted_connectivity_probability = numerator_for_prob/sum_for_prob
                    connect = random.random()
                    
                    if connect <= adjusted_connectivity_probability:
                        society.edge_matrix[person_id_first][person_id_second] = 1
                    else:
                        society.edge_matrix[person_id_first][person_id_second] = 0
        return society
    
    def _update_society_party(self, society, J = 1, alpha = 1):
        # Loop through the society, updating party affiliations by drifting
        # towards connected nodes affiliation.
        update = 0
        for person_id in range(society.population_size):
            society.person_vector[person_id].update_party_affiliation(self._calculate_affiliation_update(person_id, J, society, alpha))
        return society
    
    def _calculate_affiliation_update(self, person_id, K, society, alpha):
        # Calculate using tanh method based off of connections.
        update = 0
        for person_id_new in range(society.population_size):
            if person_id != person_id_new:
                update = update + K * society.edge_matrix[person_id][person_id_new] * np.tanh(alpha * society.person_vector[person_id_new].get_affiliation())
        return update - society.person_vector[person_id].get_affiliation()                             
