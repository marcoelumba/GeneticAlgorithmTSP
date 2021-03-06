# GeneticAlgorithm Travelling Sales Person (TSP)
An implementation of travelling sales person using eugenic algorithm

This is an adaption of a Genetic Algorithm (GA) for computer optimization. There are many optimizations problems that can be solved using GA. In this code uses TSP data from http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html.  

### The TSP problem

The TSP problem asks the following question: “Given a list of cities and the distance between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?” There are many other similar implementations and use cases that a TSP optimization can be applied to. Various operations in GA can be used in solving TSP problems but not all GA operations would apply in TSP optimisation. In this code, the following operations are implemented for TSP: 

*	in fitness *distance* -  euclidean distance and manhattan distance 
*	in selection - fitness proportion, tournament and ranking 
*	in crossover - partially matched crossover, single point crossover, cycle crossover and two-points crossover
*	in mutation - swap mutation, inversion mutation, and insert mutation

# Code Workflow
<img width="713" alt="workflow" src="https://user-images.githubusercontent.com/1595062/170859491-394ae557-b4ae-4a6a-8e20-6ab0d307e7bb.png">

# An example result

##### Initial run (50 runs by 100 generations) with 0.9 crossover probablity and 0.15 mutation probability using Euclidean distance formula to calculate fitness

![Eucledian Distance](https://user-images.githubusercontent.com/1595062/170859837-1b55cf7b-9534-4960-b796-09d9b7f536e6.png)

##### Initial run (50 runs by 100 generations) with 0.9 crossover probablity and 0.15 mutation probability using Manhattan distance formula to calculate fitness

![Manhattan Distance](https://user-images.githubusercontent.com/1595062/170859859-cbea1ca5-15a2-44df-8682-727f03ff5cf5.png)
