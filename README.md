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
Dissipative mechanism – to maintain diversity, add a small chance 1% to each 
particle of being randomly reinitialized in the search space. 

## Constraint handling: 
Bouncing mechanism instead of penalty for GA - all particles stay inside the 
feasible region. The mechanism immediately reflects the particle back into the 
valid space. 

## Comparison with GA
As the number of samples is small and the time is limited, student t test will be 
used to compare GA and PSO.  

For both algorithms were made 10 trials.  
For GA the mean value is 0.976 and variance is 0.0009463. For PSO the mean value is 0.999 and variance is 0.0000012 

Suppose both solutions are approximately normally distributed with unequal 
variances, check whether GA is superior to B at 𝛼 = 0.05 (smaller α means more 
strict and more confident decision).

<img width="386" height="460" alt="image" src="https://github.com/user-attachments/assets/6d4ea29f-db40-45bf-bc06-411a074ae109" />

<img width="985" height="487" alt="image" src="https://github.com/user-attachments/assets/4db41278-77b6-4071-8174-0dbc3fc67718" />

<img width="994" height="786" alt="image" src="https://github.com/user-attachments/assets/32d14326-0f67-49c6-8d01-5f9a37441efa" />

<img width="998" height="133" alt="image" src="https://github.com/user-attachments/assets/ee146970-afc0-4138-acc3-fe9ea0fe0786" />

<img width="985" height="581" alt="image" src="https://github.com/user-attachments/assets/eb8486bd-3b74-4cd3-8159-769385360bdd" />

## Consistency: 
To test consistency F test was used (7a-f), however, Mann – Whitney test is also can be used to prove whether two variables have the same variance.

## Conclusion: 
To compare the performance of GA and PSO a set of statistical tests were made based on the results from 10 independent runs of each algorithm.  


Based on F test there is a significant difference between the variances of the two algorithms, it is clear that PSO is more consistent than GA.  


Based on Student t test for mean comparison with unequal variances, the difference in means is statistically significant. So, the PSO outperforms GA in terms of 
average objective function value. Based on Mann – Whitney U test, there is a difference between GA and PSO performance distribution, which shows that PSO performance is much better than GA performance. 

Based on three tests, PSO performance is significantly more stable, and has higher average performance. PSO is statistically superior to GA for the given optimization task. 




