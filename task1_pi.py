"""
Task 1 – Estimating π with Monte Carlo  
==========================================

IDEA:
  Imagine a unit circle (radius=1) inscribed in a 2×2 square.
  The area of the circle is π·r² = π.
  The area of the square is 4.
  So  π ≈ 4 · (points inside circle) / (total points)

YOUR JOB:
  1. Generate `n_samples` random (x, y) points, each in [-1, 1].
  2. Count how many fall inside the unit circle (x² + y² ≤ 1).
  3. Return the estimate of π.

Run this file directly to see your result and an optional plot.
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt


def estimate_pi(n_samples: int = 100_000, seed: int = 42) -> float:
    """
    Estimate π using the circle-in-a-square method.

    Parameters
    ----------
    n_samples : int
        Number of random points to generate.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    float
        The estimated value of π.
    """
    rng = np.random.default_rng(seed)

    # TODO 1: Generate n_samples random x values in the range [-1, 1]
    # HINT: Use `rng.uniform(low, high, size)` to generate an array of random numbers instantly.
    x = ...

    # TODO 2: Generate n_samples random y values in the range [-1, 1]
    # HINT: Same as above, just for the y-coordinates.
    y = ...

    # TODO 3: Compute the distance of each point from the origin (0, 0)
    #         Hint: distance² = x² + y²
    # EXTRA HINT: In NumPy, you can use the `**` operator on the whole array to square all numbers at once!
    distance_squared = ...

    # TODO 4: Count how many points are INSIDE the unit circle
    #         (distance² <= 1)
    # HINT: `distance_squared <= 1` creates an array of True/False values.
    # You can use `np.sum()` on this boolean array to count how many 'True' values there are.
    inside = ...

    # TODO 5: Estimate π using the ratio formula described above
    # HINT: The area of the square is 4. Multiply 4 by the ratio of (points inside / total points).
    pi_estimate = ...

    return pi_estimate


def plot_simulation(n_samples: int = 5_000, seed: int = 42):
    """Visualise the circle-in-a-square Monte Carlo method."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, n_samples)
    y = rng.uniform(-1, 1, n_samples)
    inside = x**2 + y**2 <= 1

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x[inside],  y[inside],  s=1, color="#4CAF50", alpha=0.5, label="Inside")
    ax.scatter(x[~inside], y[~inside], s=1, color="#F44336", alpha=0.5, label="Outside")

    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=1.5)

    pi_est = estimate_pi(n_samples, seed)
    ax.set_title(f"Monte Carlo π estimate  ({n_samples:,} samples)\nπ ≈ {pi_est:.5f}  (true: {np.pi:.5f})")
    ax.set_aspect("equal")
    ax.legend(markerscale=6)
    plt.tight_layout()
    plt.savefig("task1_plot.png", dpi=150)
    plt.show()
    print("Plot saved to task1_plot.png")


if __name__ == "__main__":
    for n in [1_000, 10_000, 100_000, 1_000_000]:
        est = estimate_pi(n)
        err = abs(est - np.pi)
        print(f"n={n:>9,}  π ≈ {est:.6f}  error = {err:.6f}")

    plot_simulation()
