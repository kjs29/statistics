import random
import matplotlib.pyplot as plt

def simulate_sample_proportion(population, population_proportion, sample_size, number_of_simulation):
    # Objective: To test how sample proportions behave when we already know what population proportion is.
    # Scenario: Company A conducted a survey with a question to an entire population, "Is one's effort more important than the talent?"
    #           People could either say yes or no to the question.
    #           Now We'd like to know how sample proportions behave.
    
    entire_sample_set = ['yes'] * int(population_proportion * population) + ['no'] * int((1 - population_proportion) * population)
    
    def conduct_sample():
        # returns a sample proportion (p hat)        
        sample = random.sample(entire_sample_set, sample_size)
        return sample.count('yes') / sample_size
    
    # A list of sample proportions from each simulation.
    result = [0] * number_of_simulation

    for i in range(number_of_simulation):
        result[i] = conduct_sample()

    print(result)

simulate_sample_proportion(10000, 0.72, 1000, 5)
