import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))
    point_numbers = list(range(rw.num_points)) # armazena uma lista com tamanho definido pelo numero de pontos
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap= plt.cm.Blues, edgecolors= 'none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)

    plt.show()
    keep_running = input("Fazer outro passeio? (y/n): ")

    if keep_running == 'n':
        break



