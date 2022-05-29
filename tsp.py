import time
import itertools
from charles.charles import Travel
from charles.selection import fps, tournament, ranking
from charles.mutation import swap_mutation, inversion_mutation, insert_mutation
from charles.crossover import cycle_co, single_point_co, two_points_co, new_pmx_co
from charles.directory import Directory
import os
import pandas as pd
import plotly.express as px
import glob

# Removing any result.txt file
fileList = glob.glob('result/*.txt')
for filePath in fileList:
        os.remove(filePath)

# Declaire directory list
directory = []

# Lists of data saved in data folder
d1 = "data/lin318.tsp" # Best solution 42029
d2 = "data/kroB100.tsp" # Best solution 22141
d3 = "data/pr152.tsp" # Best solution 73682
d4 = "data/kroA100.tsp" # Best solution 21282
d5 = "data/d1291.tsp" # Best solution 21282

def read_location(filename):
    """
     Stores City objects. Upon initiation, automatically appends itself to list_of_cities
     """
    f = open(filename)
    for line in f:
        decoded_line = line.strip('\n')
        if decoded_line.split(' ')[0].isnumeric():
            loc_line = decoded_line.split(' ')
            name = loc_line[0]
            x = loc_line[1]
            y = loc_line[2]
            directory.append(Directory(name, x, y))

def evaluate():
    # setting the path for joining multiple files
    # list of merged files returned
    files = glob.glob("result/result_*.txt")

    df = pd.DataFrame()

    for filename in files:
        file = pd.read_csv(filename, names=['algorithm', 'run', 'generation', 'fitness'], sep=',')
        df = df.append(file)

    # Group result by generation
    result = df.groupby(['algorithm', 'generation'])['fitness'].mean().reset_index()

    # Show result in plot
    fig = px.line(result, x='generation', y='fitness', color='algorithm')
    fig.show(renderer="browser")

if __name__ == '__main__':
    try:
        # Read TSP file to generate the city list
        start_time = time.time()
        # read the tsp dataset here
        read_location(d3)

        # Creating a combination of algorithms to run
        list_algorithms = [[fps, tournament, ranking],
                           [inversion_mutation, insert_mutation, swap_mutation],
                           [single_point_co, two_points_co, cycle_co, new_pmx_co]]

        # Initializing a combination of algorithms to run
        algorithms = list(itertools.product(*list_algorithms))

        # Initializing number of runs
        number_of_runs = 50

        # From here starts the running of the combination of algorithms and run it <number_of_runs> times
        for idx, a in enumerate(algorithms):

            print(f"Running algorithm combination: Selection={a[0].__name__} : Crossover={a[2].__name__} : Mutation={a[1].__name__}")
            # Running each algorithm at i number of runs
            for i in range(number_of_runs):

                # Calculate the distance of each city in the cityList with the other cities
                travel = Travel(
                    size=50,
                    sol_size=len(directory),
                    valid_set=directory,
                    replacement=False,
                    optim="min",
                )

                travel.evolve(
                    gens=100,
                    select=a[0], # fps, tournament, ranking
                    crossover=a[2], # pmx_co, single_point_co, two_points_co
                    mutate=a[1], # swap_mutation, inversion_mutation, insert_mutation
                    co_p=0.9,
                    mu_p=0.15,
                    elitism=True,
                    algorithms=idx,
                    run=i,
                )

        evaluate()
        print("---Time Calculating distances: %s seconds ---\n" % str(time.time() - start_time))
        band = True
    except Exception as e:
        print(e)
        band = False
