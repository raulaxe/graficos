from random import choice

class RandomWalk():

    def __init__(self, num_points = 5000): # Inicialização da classe com numero de pontos inicializado com valor de 5000
        self.num_points = num_points
        self.x_values = [0] # lista para valores do eixo x
        self.y_values = [0] # lista para valores do eixo y

    def fill_walk(self): # metodo criado para calcular o passeio aleatório

        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1]) # direção do eixo x (movimento para esquerda e direita)
            x_distance =  choice([0,1,2,3,4]) # distancia entre os pontos
            x_step = x_direction * x_distance # calculo das posicoes dos pontos baseados na direção pela distancia

            y_direction = choice([1,-1]) # sentido do eixo y (movimento para cima e para baixo)
            y_distance = choice([0,1,2,3,4]) # distancia entre os pontos do eixo y
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step # proxima posição armazenada com soma do ultimo valor da lista a x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x) # concatenando a ultima posicao na lista do eixo X
            self.y_values.append(next_y)






