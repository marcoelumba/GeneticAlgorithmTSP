from random import randint, sample, choice


def binary_mutation(individual):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary.")

    return individual


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual

def insert_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 1)
    # Select insertion point
    valid_points = [i for i in range(len(individual)) if i != mut_points[0]]
    insert_point = choice(valid_points)

    # Create list of index
    indexes = [i for i in range(len(individual))]
    # Delete the selected mutating point
    indexes.pop(mut_points[0])
    # Insert mutating point to the insertion point
    indexes.insert(insert_point, mut_points[0])

    # Create the individual based on the new sequence
    individual = [individual[i] for i in indexes]

    return individual