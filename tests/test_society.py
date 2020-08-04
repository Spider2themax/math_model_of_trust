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
    # First, go through the matrix and test to make sure all edges are an 
    # appropriate value.
    
    # Instantiate constants
    population_size = 50
    connectivity_probability = 0.15
    # Create society object.
    society = Society(population_size=population_size,
                      connectivity_probability=connectivity_probability)
    society.generate_edge_matrix()
    # Loop through each entry and assert either 0 or 1.
    for x in range(population_size):
        for y in range(population_size):
            assert (society.edge_matrix[x][y]==0) or (society.edge_matrix[x][y]==1)
    
    # Next, create two society classes, one with connectivity probability 0.99
    # and another with probability 0.01. Both will have larger population 
    # sizes to avoid fluke statistical generation. Assert sums of the two
    # edge matrices.
    
    # Set up constants
    population_size = 1000
    connectivity_probability_first = 0.99
    connectivity_probability_second = 0.01
    # Create both society objects
    society_first = Society(population_size=population_size,
                    connectivity_probability=connectivity_probability_first)
    society_second = Society(population_size=population_size,
                    connectivity_probability=connectivity_probability_second)
    society_first.generate_edge_matrix()
    society_second.generate_edge_matrix()
    # Sum edges, and assert that the first has more than the second.
    count_first = 0
    count_second = 0
    for x in range(population_size):
        for y in range(population_size):
            if society_first.edge_matrix[x][y] == 1:
                count_first += 1
            if society_second.edge_matrix[x][y] == 1:
                count_second += 1
    assert (count_first > count_second)
    
