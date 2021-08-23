import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.switch_backend('agg')

dist = stats.beta # what is this?
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
# simulate binominal, toss coin exp.
data = stats.bernoulli.rvs(0.5, size = n_trials[-1])

x = np.linspace(0, 1, 100) # make 100 data point between 0 and 1

fig, ax = plt.subplots(len(n_trials), sharex= True, sharey=True, constrained_layout=False)
fig.set_size_inches((8,20))

for idx, N in enumerate(n_trials):
    #plt.setp(ax.get_yticklabels(), visible = False)
    heads = data[:N].sum() # get simulated data.
    y = dist.pdf(x, 1 + heads, 1+ N-heads) # what is this?
    ax[idx].plot(x, y, label = "observe {:2d} tosses, \n  {:2d} heads".format(N, heads))
    ax[idx].fill_between(x, 0, y, color = "blue", alpha = 0.4)
    ax[idx].vlines(0.5, 0, 20, color = "k", linestyles="--", lw = 1)

    leg = ax[idx].legend()
    leg.get_frame().set_alpha(0.1)

plt.xlabel("$p$, probability fo heads")

plt.suptitle("Bayesian updating of posterior prob", y = 0.9, fontsize = 14)


plt.savefig("./Chapter01/figure1-1.png", dpi = 300)