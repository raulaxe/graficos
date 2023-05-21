import matplotlib.pyplot as plt # Importação da biblioteca

x_values = [1, 2, 3, 4, 5] # Lista do eixo X
y_values = [1, 4, 9, 16, 25] # Lista do eixo Y

plt.scatter(x_values, y_values, s=200) # Função que cria o ponto no grafico com base nos eixos X e Y

plt.title("Square Numbers", fontsize=24) # Cria o titulo e ajusta o tamanho da fonte
plt.xlabel("Value", fontsize=14) # Cria o texto do eixo X e ajusta o tamanho da fonte
plt.ylabel("Square of Value", fontsize=14) # Cria o texto do eixo Y e ajusta o tamanho da fonte
plt.tick_params(axis='both', which='major' , labelsize=14) # Personaliza os rotulos e marcações dos eixos
plt.show() # Mostra o visualizador do grafico