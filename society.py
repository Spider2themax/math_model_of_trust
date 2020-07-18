# Copyright MaxAndMitchCorp 2020
from person import Person
import random

class Society():
    """
    TO DO: Mitchell to code up Society class so that it:
        (1) Create population_size Person objects
        (2) Create connections between Person objects, defined by unique Person IDs
    """
    #Upon instantiation, data fields are:
    #population_size:double
    #connectivity_probability:double
    #edge_matrix:(population_sizexpopulation_size)double
    #person_vector:(population_size)double
    
    #Interpretation of the edge_matrix:
    #Entry in row i, column j, represents the presence of an edge from node
    #i to node j. 
    def __init__(self,
                 population_size=25,
                 connectivity_probability=0.1):
        
        self.population_size=population_size
        self.connectivity_probability=connectivity_probability
        self.edge_matrix=[[0 for x in range(self.population_size)]
                          for y in range(self.population_size)] 
        self.person_vector=[Person() for x in range(self.population_size)]
        
    #Note: Separating out the method from the constructor which instantiates
    #the vector of persons in the society may make more sense to group with
    #the _init_ method.
    """
    def generate_society_constituents(self):
        #Create a person node at each index.
        for i in range(self.population_size):
            person_vector[i] = Person()
    """
    def generate_edge_matrix(self):
        for x in range(self.population_size):
            for y in range(self.population_size):
                connection = random.random()
                if float(connection)<=self.connectivity_probability:
                    self.edge_matrix[x][y]=1
        
            
