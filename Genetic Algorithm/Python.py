import random

# Step 1: Initialize population with random binary chromosomes
def initialize_population(population_size, chromosome_length):
  population = []
  for _ in range(population_size):
    individual = [random.randint(0, 1) for _ in range(chromosome_length)]
    population.append(individual)
  return population

# Step 2: Evaluate fitness for each individual (custom fitness function)
def evaluate_fitness(population):
  fitness_scores = []
  for individual in population:
    fitness = sum(individual) # Example fitness: maximize number of 1's
    fitness_scores.append(fitness)
  return fitness_scores

# Step 3: Select parents using roulette wheel selection
def select_parents(population, fitness_scores):
  total_fitness = sum(fitness_scores)
  probabilities = [fitness / total_fitness for fitness in fitness_scores]
  parents = random.choices(population, weights=probabilities, k=2)
  return parents[0], parents[1]

# Step 4: Perform crossover between two parents
def crossover(parent1, parent2, crossover_rate):
  if random.random() < crossover_rate:
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
  else:
    child = random.choice([parent1, parent2])
  return child

# Step 5: Apply mutation to an individual
def mutate(individual, mutation_rate):
  for i in range(len(individual)):
    if random.random() < mutation_rate:
      individual[i] = 1 - individual[i] # Flip the bit
  return individual
# Step 6: Find the best individual in the population
def find_best_individual(population, fitness_scores):
  best_index = fitness_scores.index(max(fitness_scores))
  return population[best_index], max(fitness_scores)

# Main genetic algorithm
def genetic_algorithm(population_size, num_generations, chromosome_length, crossover_rate=0.8, mutation_rate=0.01):
  population = initialize_population(population_size, chromosome_length)

  for generation in range(num_generations):
    fitness_scores = evaluate_fitness(population)
    new_population = []

    for _ in range(population_size):
      parent1, parent2 = select_parents(population, fitness_scores)
      child = crossover(parent1, parent2, crossover_rate)
      child = mutate(child, mutation_rate)
      new_population.append(child)

    population = new_population # Move to the next generation

  # Recalculate fitness after the final generation
  fitness_scores = evaluate_fitness(population)
  best_individual, best_fitness = find_best_individual(population, fitness_scores)
  
  return best_individual, best_fitness


# Example usage of the genetic algorithm
population_size = 10
num_generations = 20
chromosome_length = 5
best_individual, best_fitness = genetic_algorithm(population_size, num_generations, chromosome_length)

print("Best individual:", best_individual)
print("Best fitness:", best_fitness)
