import stan

schools_code = """
data {
  int<lower=0> J;         // number of schools
  array[J] real y;              // estimated treatment effects
  array[J] real<lower=0> sigma; // standard error of effect estimates
}
parameters {
  real mu;                // population treatment effect
  real<lower=0> tau;      // standard deviation in treatment effects
  vector[J] eta;          // unscaled deviation from mu by school
}
transformed parameters {
  vector[J] theta = mu + tau * eta;        // school treatment effects
}
model {
  target += normal_lpdf(eta | 0, 1);       // prior log-density
  target += normal_lpdf(y | theta, sigma); // log-likelihood
}
"""
schools_data = {
    "J": 8,  # number of schools
    "y": [28, 8, -3, 7, -1, 1, 18, 12],  # estimated treatment effects
    "sigma": [15, 10, 16, 11, 9, 11, 10, 18],  # standard error of effect estimates
}


posterior = stan.build(schools_code, data=schools_data, random_seed=1)
# This function returns an instance of stan.model.Model.
# (For reproducibility, we specify a random seed using the random_seed argument.)
# Building, in this context, involves converting the Stan program code into C++ code
# and then compiling that C++ code. This step may take some time.


fit = posterior.sample(num_chains=1, num_samples=1000)
# move to HP Z workstation
eta = fit["eta"]
print(eta)
df = fit.to_frame()
print(df)
