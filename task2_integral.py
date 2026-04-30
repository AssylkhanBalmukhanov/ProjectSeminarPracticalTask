"""
Task 2 – Numerical Integration with Monte Carlo  
=====================================================

IDEA:
  To integrate f(x) over [a, b], we can:
    1. Sample n random x values uniformly in [a, b].
    2. Evaluate f(x) at each point.
    3. The integral ≈ (b - a) · mean(f(x))

  This works because the definite integral is the "area under the curve",
  and the mean of sampled function values approximates the average height.

YOUR JOB:
  Implement `monte_carlo_integrate` for an arbitrary function f.
  Then use it to solve two specific integrals below.

Analytical answers (for verification):
  ∫₀¹  x²         dx  =  1/3   ≈ 0.3333
  ∫₀^π sin(x)     dx  =  2.0
  ∫₁^³  e^x        dx  =  e³ - e  ≈ 17.3673
"""
import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_integrate(f, a: float, b: float, n_samples: int = 100_000, seed: int = 42) -> float:
    """
    Estimate the definite integral of f from a to b.

    Parameters
    ----------
    f        : callable  – the function to integrate
    a, b     : float     – lower and upper bounds
    n_samples: int       – number of random samples
    seed     : int       – random seed

    Returns
    -------
    float – the estimated integral value
    """
    rng = np.random.default_rng(seed)

    # TODO 1: Sample n_samples x values uniformly between a and b
    # HINT: Use `rng.uniform()` again, but this time use your bounds `a` and `b`.
    x = ...

    # TODO 2: Evaluate f at every sampled x
    # HINT: You can pass your entire NumPy array `x` directly into the function `f(x)` to evaluate them all at once.
    fx = ...

    # TODO 3: Apply the Monte Carlo integration formula
    # HINT: The formula is (b - a) * mean(f(x)). You can instantly find the mean using `np.mean()`.
    integral = ...

    return integral


# ── Specific integrals to estimate ──────────────────────────────────────────

def integral_x_squared() -> float:
    """Return the Monte Carlo estimate of ∫₀¹ x² dx  (answer: 1/3)."""
    # TODO: Call monte_carlo_integrate with the right function and bounds
    # HINT: Use a lambda function for x² (e.g., `lambda x: x**2`). Bounds are a=0, b=1.
    return monte_carlo_integrate(...)


def integral_sin() -> float:
    """Return the Monte Carlo estimate of ∫₀^π sin(x) dx  (answer: 2.0)."""
    # TODO: Call monte_carlo_integrate with the right function and bounds
    # HINT: Pass `np.sin` as the function. For π, use `np.pi`.
    return monte_carlo_integrate(...)


def integral_exp() -> float:
    """Return the Monte Carlo estimate of ∫₁³ eˣ dx  (answer ≈ 17.3673)."""
    # TODO: Call monte_carlo_integrate with the right function and bounds
    # HINT: Pass `np.exp` as the function. Bounds are a=1, b=3.
    return monte_carlo_integrate(...)

# ── Convergence plot (optional) ──────────────────────────────────────────────

def plot_convergence():
    """Show how the estimate of ∫₀¹ x² dx converges as n grows."""
    sample_sizes = [10, 50, 100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]
    estimates = [monte_carlo_integrate(lambda x: x**2, 0, 1, n, seed=i)
                 for i, n in enumerate(sample_sizes)]
    true_value = 1 / 3

    plt.figure(figsize=(8, 4))
    plt.semilogx(sample_sizes, estimates, "o-", label="MC estimate", color="#2196F3")
    plt.axhline(true_value, color="#F44336", linestyle="--", label=f"True value ({true_value:.4f})")
    plt.xlabel("Number of samples")
    plt.ylabel("Integral estimate")
    plt.title("Convergence of Monte Carlo Integration  (∫₀¹ x² dx)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("task2_plot.png", dpi=150)
    plt.show()
    print("Plot saved to task2_plot.png")


if __name__ == "__main__":
    results = [
        ("∫₀¹  x² dx",    integral_x_squared(), 1/3),
        ("∫₀^π sin(x) dx", integral_sin(),       2.0),
        ("∫₁³  eˣ dx",    integral_exp(),        np.e**3 - np.e),
    ]
    for label, estimate, true in results:
        err = abs(estimate - true)
        print(f"{label:20s}  estimate={estimate:.5f}  true={true:.5f}  error={err:.5f}")

    plot_convergence()
