# Copyright MaxAndMitchCorp 2020

from trust_simulator import TrustSimulator
from society import Society
import pytest


@pytest.mark.parametrize("alpha", [(1), (0.05)])
def test_societal_convergence(alpha):
    society = Society(population_size=100, connectivity_probability=0.1)
    trust_simulator = TrustSimulator()
    societal_trust = trust_simulator.simulate_society(society=society,
                                                      iterations=10,
                                                      alpha=alpha)
    assert sum(societal_trust) < 1000
