import numpy as np
import matplotlib.pyplot as plt
import time

# Part_1 – initialization parameters
POPULATION_SIZE = 200
NUM_ITERATIONS = 5000
W = 0.7
C1 = 2.0
C2 = 2.0
V_MAX = 1.0
DISSIPATION_RATE = 0.01

# Part_2 – objective function (no penalty needed)
def objective_function(x, y):
    return np.cos((x - 1.14) ** 6) - 100 * (y ** 2 - x) ** 4

# Part_3 – particle initialization
x = np.random.uniform(0, 2, POPULATION_SIZE)
y = np.random.uniform(0, 3, POPULATION_SIZE)
vx = np.random.uniform(-V_MAX, V_MAX, POPULATION_SIZE)
vy = np.random.uniform(-V_MAX, V_MAX, POPULATION_SIZE)

pbest_x = np.copy(x)
pbest_y = np.copy(y)
pbest_val = np.array([
    objective_function(x[i], y[i]) if x[i] + y[i] >= 1 else -np.inf
    for i in range(POPULATION_SIZE)
])

gbest_index = np.argmax(pbest_val)
gbest_x = pbest_x[gbest_index]
gbest_y = pbest_y[gbest_index]
gbest_val = pbest_val[gbest_index]

convergence_history = [gbest_val]

# Part_4 – main PSO loop with bouncing strategy
start_time = time.time()

for t in range(NUM_ITERATIONS):
    for i in range(POPULATION_SIZE):
        r1, r2 = np.random.rand(), np.random.rand()

        # Velocity calculation
        vx[i] = W * vx[i] + C1 * r1 * (pbest_x[i] - x[i]) + C2 * r2 * (gbest_x - x[i])
        vy[i] = W * vy[i] + C1 * r1 * (pbest_y[i] - y[i]) + C2 * r2 * (gbest_y - y[i])

        vx[i] = np.clip(vx[i], -V_MAX, V_MAX)
        vy[i] = np.clip(vy[i], -V_MAX, V_MAX)

        # Particle movement
        x[i] += vx[i]
        y[i] += vy[i]

        # Clamp to variable bounds
        x[i] = np.clip(x[i], 0, 2)
        y[i] = np.clip(y[i], 0, 3)

        # Part_5 – constraint handling with bouncing
        if x[i] + y[i] < 1:
            diff = 1 - (x[i] + y[i])
            x[i] += diff / 2
            y[i] += diff / 2
            # Clamp again after bounce
            x[i] = np.clip(x[i], 0, 2)
            y[i] = np.clip(y[i], 0, 3)

        # Part_6 – dissipative mechanism
        if np.random.rand() < DISSIPATION_RATE:
            x[i] = np.random.uniform(0, 2)
            y[i] = np.random.uniform(0, 3)

        # Fitness check only if feasible
        if x[i] + y[i] >= 1:
            val = objective_function(x[i], y[i])
        else:
            val = -np.inf

        if val > pbest_val[i]:
            pbest_x[i], pbest_y[i], pbest_val[i] = x[i], y[i], val

    # Global best update
    gbest_index = np.argmax(pbest_val)
    gbest_x = pbest_x[gbest_index]
    gbest_y = pbest_y[gbest_index]
    gbest_val = pbest_val[gbest_index]

    convergence_history.append(gbest_val)

elapsed_time = time.time() - start_time

# Part_7 – print and plot results
print(f"Best solution found: x = {gbest_x:.4f}, y = {gbest_y:.4f}")
print(f"Maximum value of f(x, y): {gbest_val:.6f}")
print(f"PSO (Bouncing Strategy) runtime: {elapsed_time:.4f} seconds")

plt.plot(convergence_history)
plt.title("PSO with Bouncing Constraint Handling")
plt.xlabel("Iterations")
plt.ylabel("Best Objective Value")
plt.grid(True)
plt.show()
