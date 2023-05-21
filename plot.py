import matplotlib.pyplot as plt # importa a biblioteca de gráficos e plotagens

input_values = [1, 2, 3, 4, 5]

squares = [1, 4, 9, 16, 25]  # criado uma lista que armazena números de raízes quadradas

plt.plot(input_values, squares, linewidth=5) # Passa as listas como 1º e 2º argumentos na função que irá plotar no gráfico,
# e no 3º argumento ajusta a largura da linha do gráfico

plt.title("Squares Numbers", fontsize=24) # Define o texto do título no primeiro argumento,
# e no segundo argumento ajusta o tamanho da fonte

plt.xlabel("Value", fontsize=14) # Define o texto do eixo X e ajusta o tamanho da fonte

plt.ylabel("Square of Value", fontsize=14) # Define o texto do eixo Y e ajusta o tamanho da fonte

plt.tick_params(axis='both', labelsize=14) # Personaliza as marcações dos eixos X e Y,
# e ajusta o tamamho da fonte dos rótulos
plt.show() # Função que mostra o visualizador do gráfico


