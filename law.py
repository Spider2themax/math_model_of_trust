# Copyright MaxAndMitchCorp 2020

# This class' aim is to construct an object which allows for varying distributions
# for law scores, as well as the population with which it impacts.
import numpy as np
from society import Society
from person import Person
import random

class Law:
    
    def __init__(self, mean = 0, stdev = 0.5, law_type = 0):
        """ 
        The fields for the class should be the mean and standard deviation
        of the law value, regardless of distribution.
        
        FIELDS
        ---------
        mean:
            The expected value of the law's magnitude, independent of distribution.
        law_type:
            Takes on an integer value representing which law type is desired.
            
            Types and assignments
            ----------------------
            0 = Standard Gaussian centered around 0 with standard deviation 
            equal to that of what is taken by the __init__ method.
        
        actual_value:
            The actual value which is generated based off of the law type and
            mean, and is the true law's magnitude.
        """
        self.mean = mean
        self.law_type = law_type
        self.actual_value = self._calculate_law_magnitude(mean,stdev,law_type)
    
    def _calculate_law_magnitude(mean, stdev, law_type):
        # This method is where the actual value gets calculated, and is split
        # according to the desired calculation method.
        if law_type == 0:
            # Generate a value from a gaussian with loc=mean and scale=stdev.
            return np.random.normal(loc = mean, scale = stdev)
        else:
            # Note: here is where further methods would be placed, forming 
            # a nested-if structure.
            return 0
            
