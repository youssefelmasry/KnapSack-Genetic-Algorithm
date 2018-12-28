'''
Problem: KnapSack Problem using Genetic algorithm

work cited: the origin code from Pantzan link (https://github.com/Pantzan/KnapsackGA), i did some changes and optimization

'''

# Oultine of Genetic Algorithm:

# Start: Randomly generate a population of N chromosomes
# Fitness: Calculate the fitness of all chromosomes
# Create a new population:
	# 1. Selection: Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
	# 2. Crossover: # Crossover is the process of combining the bits of one chromosome with those of another.
					# This is to create an offspring for the next generation that inherits traits of both parents.
	# 3. Mutation: Mutation is performed after crossover to prevent falling all solutions in the population into a local optimal of solved problem
# Replace: Replace the current population with the new population.
# Test: Test whether the end condition is satisfied. If so, stop. If not, return the best solution in current population and go to Step 2

import random
import operator

class Knapsack:	

	#initialize variables and lists
	def __init__(self):		
		self.MaxWeight = 0
		self.weights = []
		self.values = []
		self.optimal = 0
		self.parents = []
		self.newparents = []
		self.bests = []
		self.best_population = [] 
		self.iterated = 1
		self.PopulationSize = 0
		self.NumIterations = 0

	# create the initial Population 
	def initialize(self):
		for i in range(self.PopulationSize):
			parent = []
			num_objects = len(weights)
			for k in range(num_objects):
				k = random.randint(0, 1)
				parent.append(k)
			self.parents.append(parent)

	# set the details of this problem
	def details(self, weights, values, MaxWeight, PopulationSize, NumIterations):
		self.weights = weights
		self.values = values
		self.NumIterations = NumIterations
		self.MaxWeight = MaxWeight
		self.PopulationSize = PopulationSize
		self.initialize()

	# calculate the fitness function
	def fitness(self, item):
		sum_w = 0
		sum_v = 0
		for index, i in enumerate(item):
			sum_w += self.weights[index] * i
			sum_v += self.values[index] * i

		# if greater than the optimal return 0 or the number otherwise
		if sum_w > self.MaxWeight:
			return 0
		else: 
			return sum_v	
	
	# Get the best chromosomes by the best fitness value
	def evaluation(self):
		# loop through parents and calculate fitness
		best_pop = self.PopulationSize // 2
		
		for i in range(0, len(self.parents)):
			parent = self.parents[i]
			ft = self.fitness(parent)
			#put the calculated parent's fitness in bests
			self.bests.append((ft, parent))

		# sort the fitness list by fitness in descending 
		self.bests.sort(key=operator.itemgetter(0), reverse=True)
		# put the top half parents in best population
		self.best_population = self.bests[:best_pop]

	# mutate children
	def mutation(self, ch):
		for i in range(0, len(ch)):		
			k = random.uniform(0, 1)
			if k > 0.6:
				#if random float number greater that 0.5 flip 0 with 1 and vice versa
				if ch[i] == 1:
					ch[i] = 0
				else: ch[i] = 1
		return ch

	# crossover two parents to produce two children by mixing them under random ration each time
	def crossover(self, ch1, ch2):
		# One-Point CrossOver
		One_Point = random.randint(1, len(ch1)-1)

		tmp1 = ch1[One_Point:]
		tmp2 = ch2[One_Point:]
		ch1 = ch1[:One_Point]
		ch2 = ch2[:One_Point]
		ch1.extend(tmp2)
		ch2.extend(tmp1)
		return ch1, ch2

	def run(self):
		for i in range(self.NumIterations):

			self.evaluation()
			if self.best_population[0][0] > self.optimal:
				self.optimal = self.best_population[0][0]
			newparents = []
			self.best_population = [x[1] for x in self.best_population]
			pop = len(self.best_population)

			for i in range(0, pop):
				# select the random index of best children to randomize the process
				if i < pop-1:
					ch1 = self.best_population[i]
					ch2 = self.best_population[i+1]
					child_1, child_2 = self.crossover(ch1, ch2)
					newparents.append(child_1)
					newparents.append(child_2)
				else:
					ch1 = self.best_population[i]
					ch2 = self.best_population[0]
					child_1, child_2 = self.crossover(ch1, ch2)
					newparents.append(child_1)
					newparents.append(child_2)

			# mutate the new children and potential parents to ensure global optimal found
			for i in range(0, len(newparents)):
				newparents[i] = self.mutation(newparents[i])

			print("Generation number: {}" .format(self.iterated))
			print ("	optimal is {} " .format(self.optimal))

			self.iterated += 1
			self.parents = newparents
			self.bests = []
			self.best_population = []

# details for this particular problem
weights = [56, 59, 80, 64, 75, 17]
values = [50, 50, 64, 46, 50, 5]

MaxWeight = 190
PopulationSize = 20
NumIterations = 10

k = Knapsack()
k.details(weights, values, MaxWeight, PopulationSize, NumIterations)
k.run()