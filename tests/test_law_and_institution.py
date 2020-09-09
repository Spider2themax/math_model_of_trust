# Copyright MaxAndMitchCorp 2020

from trust_simulator import TrustSimulator
from society import Society
from institution import Institution
from law import Law
import pytest

def test_lawInstitution_fields():
    # Verify, upon instantiation, that all fields of the law and institution
    # classes are of the type they should be.
    society = Society(population_size = 10)
    institution = Institution(society)
    laws = institution._generate_laws(society)
    
    assert isinstance(institution.get_affiliation(), float)
    
    for law in laws:
        for person_id in range(society.population_size):
            assert isinstance(law.affected_persons[person_id], int)
        assert isinstance(law.mean, float)
        assert isinstance(law.law_type, int)
        assert isinstance(law.actual_value, float)
    
        


