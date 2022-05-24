from random import shuffle, choice, sample, random
from operator import attrgetter
from copy import deepcopy


class Route:
    def __init__(
            self,
            representation=None,
            sol_size=None,
            replacement=True,
            valid_set=None,
    ):
        if representation is None:
            if replacement == True:
                self.representation = [choice(list([r.name for i, r in enumerate(valid_set)]) for i in range(sol_size))]
            elif replacement == False:
                self.representation = sample(list([r.name for i, r in enumerate(valid_set)]), sol_size)
        else:
            self.representation = representation

        self.fitness = self.get_fitness(valid_set)

    def get_fitness(self, directory):
        """
                self --> None
                Calculates the distances of the
                city to all other cities in the global
                list list_of_cities, and places these values
                in a dictionary called self.distance_to
                with city name keys and float values
                """
        fitness = 0

        for i, r in enumerate(self.representation):
            city1 = directory[int(self.representation[i-1])-1]
            city2 = directory[int(self.representation[i])-1]
            fitness += self.eu_dist(float(city1.x), float(city1.y), float(city2.x), float(city2.y))

        return int(fitness)

    # Calculates the distance between two cartesian points..
    def eu_dist(self, x1,y1,x2,y2):
        """
        Compute the L2-norm (Euclidean) distance between two points.

        The two points are located on coordinates (x1,y1) and (x2,y2),
        sent as parameters
        """
        return ((x2-x1)**2 + (y2-y1)**2)**(0.5)

    # calculate manhattan distance
    def manhattan_distance(self, x1,y1,x2,y2):
        return abs(x2 - x1) + abs(y2 - y1)

    # calculate minkowski distance
    def minkowski_distance(self, x1,y1,x2,y2,p):
        return abs(x2 - x1)** p + abs(y2 - y1)** p

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Route(size={len(self.representation)}); Fitness: {self.fitness}"

class Travel:
    def __init__(self, size, optim, **kwargs):
        self.route = []
        self.size = size
        self.optim = optim
        self.replacement = kwargs["replacement"]
        self.valid_set = kwargs["valid_set"]
        self.sol_size = kwargs["sol_size"]

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism, algorithms, run=0):

        for _ in range(self.size):
            self.route.append(
                Route(
                    sol_size=self.sol_size,
                    replacement=self.replacement,
                    valid_set=self.valid_set,
                )
            )

        results = []
        for gen in range(gens):
            new_pop = []

            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.route, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.route, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Route(representation=offspring1, valid_set=self.valid_set))
                if len(new_pop) < self.size:
                    new_pop.append(Route(representation=offspring2, valid_set=self.valid_set))

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.route = new_pop

            if self.optim == "max":
                BestFitness=str(max(self, key=attrgetter("fitness"))).split(' ')[-1]
                result = f"{select.__name__}|{crossover.__name__}|{mutate.__name__}, {run}, {gen}, {BestFitness}"
                #print(f'Algorithm:{algorithms} Gen:{gen} of Run:{run} Best Route: {max(self, key=attrgetter("fitness"))}')
                results.append(result)
            elif self.optim == "min":
                BestFitness=str(max(self, key=attrgetter("fitness"))).split(' ')[-1]
                result = f"{select.__name__}|{crossover.__name__}|{mutate.__name__}, {run}, {gen}, {BestFitness}"
                #print(f'Algorithm:{algorithms} Gen:{gen} of Run:{run} Best Route: {min(self, key=attrgetter("fitness"))}')
                results.append(result)

        self.write_result(results, algorithms, run)

    def write_result(self, results, algorithms, run):
        with open(rf'result/result_{algorithms}_{run}.txt', 'a') as fp:
            for item in results:
                # write each item on a new line
                fp.write("%s\n" % item)

    def __len__(self):
        return len(self.route)

    def __getitem__(self, position):
        return self.route[position]

    def __repr__(self):
        return f"Routes(size={len(self.route)}, route_size={len(self.route[0])})"
