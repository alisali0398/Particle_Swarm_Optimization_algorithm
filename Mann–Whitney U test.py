from scipy.stats import mannwhitneyu

# Sample results from 10 runs of each algorithm
ga_results = [0.983, 0.997, 0.996, 0.902, 0.989, 0.975, 0.998, 0.945, 0.975, 0.999]
pso_results = [0.999, 0.998, 0.999, 1.000, 0.997, 0.998, 1.000, 0.999, 0.997, 0.998]

# Perform the Mann–Whitney U test
statistic, p_value = mannwhitneyu(ga_results, pso_results, alternative='two-sided')

# Display results
print(f"Mann–Whitney U statistic: {statistic}")
print(f"P-value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("The difference is statistically significant (p < 0.05).")
else:
    print("The difference is not statistically significant (p ≥ 0.05).")
