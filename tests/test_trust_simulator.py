# Copyright MaxAndMitchCorp 2020

from trust_simulator import TrustSimulator
from society import Society
from institution import Institution
import pytest


@pytest.mark.parametrize("alpha", [(1), (0.05)])
def test_societal_convergence(alpha):
    society = Society(population_size=100, connectivity_probability=0.1)
    institution = Institution(society = society)
    trust_simulator = TrustSimulator()
    societal_trust = trust_simulator.simulate_society(society=society,
                                                      institution = institution,
                                                      iterations=10,
                                                      alpha=alpha)
    assert sum(societal_trust) < 1000

def test_edges_dynamic():
    # Test to make sure that given a fairly low affiliation probability, that
    # is, one less than the starting connectivity probability, then the number
    # of edges decreases over the course of a simulation.
    
    # Instantiate the society
    society = Society(population_size=100, connectivity_probability=0.3)
    
    # Count the number of edges to start
    count1 = 0
    for person_id_first in range(society.population_size):
        for person_id_second in range(society.population_size):
            if society.edge_matrix[person_id_first][person_id_second]==1:
                count1 = count1 + 1
            else:
                pass
    # Simulate the society through with an affiliation probability half that
    # of what it started with.
    trust_simulator = TrustSimulator()
    societal_trust = trust_simulator.simulate_society(society=society,
                                     iterations = 30,
                                     alpha = 0.1,
                                     affiliation_prob = 0.15)
    # Count the edges again with the simulated society.
    count2 = 0
    for person_id_first in range(society.population_size):
        for person_id_second in range(society.population_size):
            if society.edge_matrix[person_id_first][person_id_second]==1:
                count2 = count2 + 1
            else:
                pass
    # Assert that count1 should be greater than count2
    assert count1 > count2
