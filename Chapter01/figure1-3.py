import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.switch_backend('agg')

a = np.arange(16)
poi = stats.poisson
lambda_ = [1.5, 4.25] #variable "lambda" is impossible
colors = ["#348ABD", "#A60628"]

plt.figure(figsize=(12.5, 4))
# poisson, probability mass function will be used.
for idx, lam in enumerate(lambda_):
    plt.bar(a, poi.pmf(a, lam), color = colors[idx], 
        label=r"$\lambda = {}$".format(lam), alpha = 0.6,
        edgecolor = colors[idx], lw="3")

plt.xticks(a+ 0.4, a)
plt.legend()
plt.ylabel(r"probability of $k$")
plt.xlabel(r"$k$")
plt.title(r'''
Probability mass function of a Poisson random variable; differing $\lambda$ values
    ''')

plt.savefig("./Chapter01/figure1-3.png", dpi = 300)
