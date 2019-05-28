''' Histograma '''

import matplotlib.pyplot as plt

tabela = [63, 50, 57, 56, 68, 82, 75, 95, 47, 75, 95, 47, 75, 95, 47, 63, 50, 57, 56, 68, 82, 75, 95, 47,
          61, 76, 61, 52, 63, 80, 80, 68, 72, 64, 77]

# Histograma bruto
plt.plot(tabela)  # porém funciona plt.plot(tabela)
plt.show()


x_axis = range(len(tabela))
width_n = 0.4
bar_color = 'red'

plt.bar(x_axis, tabela, width=width_n, color=bar_color)
plt.show()

# scatter_plot = plt.scatter(tabela, alpha=0.5,
#                            c=exemploPanda)
# plt.show()
