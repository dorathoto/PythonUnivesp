from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_size_inches(16, 4)

# Valores manuais
valores = np.array([1, 2, 3, 4, 5, 6, 3, 8, 8, 8])
valores = np.sort(valores)               # coloca em ordem
# O que é CDF, PDF http://ecologia.ib.usp.br/let/doku.php?id=tutoriais:pdf
# CDF e PDF não funcionam para distribuições discretas
cum = np.cumsum(valores)
pmf = cum / np.amax(cum)                 # normaliza e cria o PMF

# Como PDF não vale contamos os valores
val, count = np.unique(valores, return_counts=True)
# normaliza-se para mostrar em seguida
count = count / np.amax(count)


ax1.plot(val, count, 'r--', label='Frequencia')
ax1.plot(valores, pmf, 'b--', label='PMF')
ax1.hist(valores, bins=len(valores), normed=True, alpha=0.6,
         color='g', edgecolor='black', linewidth=1.2)


# Valores normais
valores = norm.rvs(size=100)  # pegamos de norm 100 valores aleatórios normais
valores = np.sort(valores)     # coloca em ordem

ax2.plot(valores, norm.pdf(valores), 'r--', label='PDF')
ax2.plot(valores, norm.cdf(valores), 'b--', label='CDF')
ax2.hist(valores, bins=len(valores), normed=True, alpha=0.6,
         color='g', edgecolor='black', linewidth=1.2)


plt.show()
