import matplotlib.pyplot as plt

# Dados
idades = ['4 a 5 anos', '6 a 10 anos', '11 a 14 anos', '15 a 17 anos']
quantidades = [384475, 22702, 59760, 629531]

# Criar gráfico de pizza
plt.pie(quantidades, labels=idades, autopct='%1.1f%%')

# Adicionar título
plt.title('Distribuição de Idade das Crianças')

# Exibir gráfico
plt.show()
