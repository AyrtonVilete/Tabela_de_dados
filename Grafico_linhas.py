import matplotlib.pyplot as plt

# Dados
anos = [2020, 2021]
taxa_abandono_total = [2.3, 5.6]

# Gráfico de linha: Evolução da taxa de abandono escolar de 2020 a 2021
plt.figure()
plt.plot(anos, taxa_abandono_total, marker='o')
plt.xlabel('Ano')
plt.ylabel('Taxa de Abandono (%)')
plt.title('Evolução da Taxa de Abandono Escolar (2020-2021)')

# Exibir os gráficos
plt.show()
