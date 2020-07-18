# Copyright MaxAndMitchCorp 2020

from society import Society
from person import Person


def test_population():
    """
    This test will simply ensure that a created Society object has a list of
    Person objects, that is of length population_size.
    """
    # Set up constants
    population_size = 50
    connectivity_probability = 0.15
    # Create Society object.
    society = Society(population_size=population_size,
                      connectivity_probability=connectivity_probability)
    # Assert the correct population.
    assert len(society.person_vector) == population_size
    # Assert each object in society.person_vector is a Person object
    for person in society.person_vector:
        assert type(person) == Person


def test_connectivity_matrix():
    """
    This test will ensure two things:
        1. That all values of the connectivity matrix are 0 or 1, representing
           nodes that are connected (1) or disconnected (0).
        2. That the number of connections in a society using a very high
           connectivity_probability is greater then a society using a very
           low connectivity_probability.
    """
    # TO DO FOR MITCHMAN
    pass
