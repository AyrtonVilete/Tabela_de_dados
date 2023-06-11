import matplotlib.pyplot as plt

# Dados
regioes = ['Sul', 'Sudeste', 'Centro-Oeste', 'Norte', 'Nordeste']
taxas_abandono = [3.3, 3.3, 4.9, 7.6, 13.9]

# Criar gráfico de barras
plt.figure()

# Adicionar título e rótulos aos eixos
plt.plot(regioes, taxas_abandono)
plt.title('Taxa de Abandono Escolar por Região em 2019')
plt.xlabel('Regiões')
plt.ylabel('Taxa de Abandono (%)')

# Exibir gráfico
plt.show()
