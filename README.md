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
For GA the mean value is 0.976 and variance is 0.0009463
For PSO the mean value is 0.999 and variance is 0.0000012 

Suppose both solutions are approximately normally distributed with unequal 
variances, check whether GA is superior to B at 𝛼 = 0.05 (smaller α means more 
strict and more confident decision).

<img width="386" height="460" alt="image" src="https://github.com/user-attachments/assets/6d4ea29f-db40-45bf-bc06-411a074ae109" />
