from random import choice
from operator import attrgetter
import numpy as np


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """
    if population.optim == "max":
        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        selection_probs = [c.fitness / total_fitness for c in population]
        for c in population:
            print(c.fitness / total_fitness)
        # Get the index of the choice
        indx = np.random.choice(len(population), 1, p=selection_probs)
        return population[int(indx)]

    elif population.optim == "min":
        max_fitness = max([i.fitness for i in population]) + 1
        # Get a 'position' on the wheel
        # Updated sum total fitness
        total_fitness = sum([max_fitness - i.fitness for i in population])

        # Get probability from updated probs
        selection_probs = [(int(max_fitness) - int(i.fitness)) / int(total_fitness) for i in population]
        # Get the index of the choice
        indx = np.random.choice(len(population), 1, p=selection_probs)
        return population[int(indx)]

    else:
        raise Exception("No optimization specified (min or max).")


def tournament(population, size=10):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select route based on tournament size
    tournament = [choice(population.route) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")


def ranking(population):
    """Linear Ranking Selection algorithm Computes and generates rank and selection_probability
      for each individual's fitness

      Args:
        population (Population): The population we want to select from.

      Returns:
        Individual: Best individual ranked .

     Inspired ULR: https://gist.github.com/kburnik/3fe766b65f7f7427d3423d233d02cd39
    """
    # Get the number of individuals in the population.
    n = len(population)

    # Use the gauss formula to get the sum of all ranks (sum of integers 1 to N).
    rank_sum = n * (n + 1) / 2

    # Sort and go through all individual fitnesses; enumerate ranks from 1.
    seq = sorted(population, key=attrgetter("fitness"))
    # Create list of ranked index
    index = [seq.index(v) + 1 for v in population]
    # Calculate prob of rank
    rank = [(i / rank_sum) * 100 for i in index]

    if population.optim == 'max':
        max_value = max(rank)
        i = rank.index(max_value)
        return population[i]
    elif population.optim == 'min':
        min_value = min(rank)
        i = rank.index(min_value)
        return population[i]
    else:
        raise Exception("No optimization specified (min or max).")



