import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.switch_backend('agg')

a = np.linspace(0, 4, 100) # for continuous variable, return 100 between [0,4]
expo = stats.expon # exponential function
lambda_ = [0.5, 1] # two different lambda value for poisson
colors = ["#348ABD", "#A60628"]


for lam, col in zip(lambda_, colors):
    plt.plot(a, expo.pdf(a, scale=1. / lam), lw =3, color = col, 
        label = r"$\lambda$ = {}".format(lam))
    plt.fill_between(a, expo.pdf(a, scale = 1. /lam), color = col, alpha = 0.3)

plt.legend()
plt.ylabel(r"PDF of $z$", fontsize = 13)
plt.xlabel(r"$z$")
plt.ylim(0, 1.2)
plt.title(r"PDF according to $\lambda$")

plt.savefig("./Chapter01/figure1-4.png", dpi = 300)