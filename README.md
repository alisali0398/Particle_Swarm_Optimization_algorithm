# Particle_Swarm_Optimization_algorithm
Particle_Swarm_Optimization_algorithm test case

## Optimization problem - maximize
f(x, y) = cos((x - 1.14)<sup>6</sup>) - 100 * (y<sup>2</sup> - x)<sup>4</sup>

0 &le; x &le; 2

0 &le; y &le; 3

x + y &ge; 1

## Swarm size and termination condition:

Swarm size is **200 particles** 

Termination condition is **5000 iterations**

## Tuning parameters: 
Inertia weight w = 0.7

Acceleration constants c<sub>1</sub> = c<sub>2</sub> = 2.0

Velocity maximum v = 1.0

## Additional featute
Dissipative mechanism: To maintain diversity, each particle has a 1% chance of being randomly reinitialized in the search space.

## Constraint handling: 
Bouncing mechanism: Instead of using a penalty for constraint handling (as in GA), a bouncing strategy was applied to keep all particles inside the feasible region. If a particle violates the constraint, it is immediately reflected back into the valid space.

## Comparison with GA
As the number of samples is small and the time is limited, student t test will be 
used to compare GA and PSO.  

For both algorithms were made 10 trials.  
For GA the mean value is 0.976 and variance is 0.0009463. For PSO the mean value is 0.999 and variance is 0.0000012 

Suppose both solutions are approximately normally distributed with unequal 
variances, check whether GA is superior to B at 𝛼 = 0.05 (smaller α means more 
strict and more confident decision).

## Statistical Analysis
* Hypotheses:

H<sub>0</sub> : σ<sup>2</sup><sub>GA</sub> = σ<sup>2</sup><sub>PSO</sub>

H<sub>1</sub> : σ<sup>2</sup><sub>GA</sub> ≠ σ<sup>2</sup><sub>PSO</sub>

* Calculate F statistics:

F = s<sup>2</sup><sub>GA</sub> / s<sup>2</sup><sub>PSO</sub> = 788. 583

* Critical values for F statistics:

d<sub>fGA</sub> = n<sub>GA</sub> - 1 = 9

d<sub>fPSO</sub> = n<sub>PSO</sub> - 1 = 9

* Two two-tailed test, split α into two parts:

  α/2 = 0.025

* F distribution table

F<sub>(0.025;9,9)</sub> = 4.03 - right tail

1/F<sub>(0.025;9,9)</sub> = 0.248 - left tail

* Rejection regions

F = 788.583 > 4.03

Solutions of GA are significantly greater than solutions of PSO, so reject H<sub>0</sub> This is also statistical evidence that PSO is more consistent than GA. 
  
## Student t test: 

A two-sample t-test with unequal variances (Welch’s t-test) was performed.

<img width="810" height="532" alt="image" src="https://github.com/user-attachments/assets/2aa542a8-ed7c-4770-8b48-ff1cad425b7e" />

As PSO has a higher mean than GA, the test indicates that PSO achieves statistically significantly better results than GA.

<img width="797" height="417" alt="image" src="https://github.com/user-attachments/assets/114a4c83-c7b9-4e60-88fd-608836acdfe1" />

The null hypothesis is rejected, confirming that PSO’s mean performance is significantly better than GA’s.

## Mann–Whitney U Test

A nonparametric Mann–Whitney U test was also performed to compare the distributions of GA and PSO results.

p-value < 0.05

The difference between GA and PSO is statistically significant. Code can be found in a separate file. 

## Conclusion

To compare the performance of GA and PSO a set of statistical tests were made based on the results from 10 independent runs of each algorithm. 


Based on F test there is a significant difference between the variances of the two algorithms, it is clear that PSO is more consistent than GA. 


Based on Student t test for mean comparison with unequal variances, the difference in means is statistically significant. So, the PSO outperforms GA in terms of 
average objective function value. 


Based on Mann – Whitney U test, there is a difference between GA and PSO performance distribution, which shows that PSO performance is much better than GA performance. 


Based on three tests, PSO performance is significantly more stable, and has higher average performance. PSO is statistically superior to GA for the given optimization task.







