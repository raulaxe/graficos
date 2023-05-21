import matplotlib.pyplot as plt # importa a biblioteca

x_values = list(range(1, 25)) # Cria uma lista armazenando os valores na variavel
y_values = [x**2 for x in x_values] # Cria um laço a partir dos valores da variavel anterior

plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) # Cria os pontos especificos no Gráfico
plt.title("Square Numbers", fontsize=24) # Cria o titulo e ajusta o tamanho da fonte
plt.xlabel("Value", fontsize=14) # Cria o texto do eixo X e ajusta o tamanho da fonte
plt.ylabel("Square of Value", fontsize=14) # Cria o texto do eixo Y e ajusta o tamanho da fonte
plt.tick_params(axis='both', which='major', labelsize=14) # Personaliza os rotulos e marcações dos eixos
#plt.axis([0, 1100, 0, 1100000]) # Define o intervalo em cada eixo
plt.savefig('squares_plot.png', bbox_inches='tight') #Salva a imagem do grafico no mesmo diretorio do codigo
plt.show() # Mostra o visualizador do grafico


