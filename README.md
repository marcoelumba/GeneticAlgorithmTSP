# GeneticAlgorithm Travelling Sales Person
An implementation of travelling sales person using eugenic algorithm

This project is an adaption of a Genetic Algorithm (GA) for computer optimization. There are many optimizations problems that can be solved using GA. In this code uses TSP data from http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html.  

# What is TSP:

The TSP problem asks the following question: “Given a list of cities and the distance between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?” There are many other similar implementations and use cases that a TSP optimization can be applied to. Various operations in GA can be used in solving TSP problems but not all GA operations would apply in TSP optimisation. I have used only the following operations: 

•	in selection - fitness proportion, tournament and ranking; 
•	in crossover - partially matched crossover, single point crossover and two-points crossover;
•	in mutation - swap mutation, inversion mutation, and insert mutation. 

# Code Workflow
<img width="713" alt="workflow" src="https://user-images.githubusercontent.com/1595062/170859491-394ae557-b4ae-4a6a-8e20-6ab0d307e7bb.png">
