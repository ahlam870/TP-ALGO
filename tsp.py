import random
import math

distance_matrix = [
    [0, 3, 6, 4, 5, 7, 3, 6, 8, 4],
    [3, 0, 2, 5, 4, 6, 3, 5, 7, 6],
    [6, 2, 0, 7, 5, 4, 6, 8, 9, 7],
    [4, 5, 7, 0, 6, 8, 4, 7, 6, 5],
    [5, 4, 5, 6, 0, 3, 7, 6, 8, 7],
    [7, 6, 4, 8, 3, 0, 5, 6, 7, 6],
    [3, 3, 6, 4, 7, 5, 0, 4, 5, 4],
    [6, 5, 8, 7, 6, 6, 4, 0, 3, 5],
    [8, 7, 9, 6, 8, 7, 5, 3, 0, 9],
    [4, 6, 7, 5, 7, 6, 4, 5, 9, 0]
]


def calculate_total_distance(tour):  #GA3
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]] # BE TRTIB OU NWLI LLWLA 
    return total_distance

def get_neighbor(tour):
    neighbor = tour[:] # NBDL 2 VILLE 
    i, j = random.sample(range(len(tour)), 2) # CEST PAS LE MM
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i] # NBD PLASA 
    return neighbor


def simulated_annealing(initial_temperature, cooling_rate, max_iterations):
    # NKHYR MASAR BRK N3WED TRTYB BACH NDIR MSAR JDID 
    current_tour = list(range(len(distance_matrix)))
    random.shuffle(current_tour) # BE HDY NBDL
    current_distance = calculate_total_distance(current_tour) # N3WED TRTYB BACH NDIR MSAR JDID 
    
    best_tour = current_tour[:]
    best_distance = current_distance #  NDIRHA THE BEST 
    
    temperature = initial_temperature
    
    for iteration in range(max_iterations): # NBDA NKRER FYHA N FOIS 
    
        neighbor_tour = get_neighbor(current_tour) #  MSAR JDID 
        neighbor_distance = calculate_total_distance(neighbor_tour) #  NHSBLO MSAFA 
        
    
        if neighbor_distance < current_distance:
            accept_prob = 1.0  # N9BLOHA IDA KANT 9EL MN 9DIMA
        else:
            accept_prob = math.exp((current_distance - neighbor_distance) / temperature) 
        
       
        if neighbor_distance < current_distance or random.random() < accept_prob: 
            current_tour = neighbor_tour[:]
            current_distance = neighbor_distance
            
           
            if current_distance < best_distance:
                best_tour = current_tour[:]
                best_distance = current_distance
        
        
        temperature *= cooling_rate
    
    return best_tour, best_distance


initial_temperature = 100
cooling_rate = 0.995
max_iterations = 10000


best_tour, best_distance = simulated_annealing(initial_temperature, cooling_rate, max_iterations)


print("Best tour:", best_tour)
print("Best distance:", best_distance)
