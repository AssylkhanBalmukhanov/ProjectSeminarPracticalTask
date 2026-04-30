"""
run_tests.py -- Check your solutions for all three tasks.
Run with:  python run_tests.py
"""

import sys
import numpy as np


def check(label: str, got, expected, tol: float):
    passed = abs(got - expected) <= tol
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}]  {label}")
    print(f"         got={got:.5f}  expected~{expected:.5f}  tolerance=+-{tol}")
    if not passed:
        print(f"         Difference {abs(got-expected):.5f} exceeds tolerance.")
    return passed


def test_task1():
    print("\n-- Task 1 : Estimating pi -------------------------------------")
    try:
        from task1_pi import estimate_pi
        results = []
        for n in [10_000, 100_000, 1_000_000]:
            est = estimate_pi(n)
            ok  = check(f"estimate_pi(n={n:>9,})", est, np.pi, tol=0.05)
            results.append(ok)
        return all(results)
    except Exception as exc:
        print(f"  ERROR: {exc}")
        return False


def test_task2():
    print("\n-- Task 2 : Numerical Integration -----------------------------")
    try:
        from task2_integral import integral_x_squared, integral_sin, integral_exp
        r1 = check("integral x^2  [0,1]",   integral_x_squared(), 1/3,            tol=0.01)
        r2 = check("integral sin  [0,pi]",   integral_sin(),       2.0,            tol=0.02)
        r3 = check("integral e^x  [1,3]",    integral_exp(),       np.e**3 - np.e, tol=0.10)
        return all([r1, r2, r3])
    except Exception as exc:
        print(f"  ERROR: {exc}")
        return False


def test_task3():
    print("\n-- Task 3 : Stock Price Simulation ----------------------------")
    try:
        from task3_stock import simulate_gbm, probability_above, expected_final_price

        paths = simulate_gbm(n_paths=50_000, seed=0)

        r1 = check("paths shape  (50000, 253)",
                   float(paths.shape == (50_000, 253)), 1.0, tol=0.5)

        r2 = check("Starting price S0=100",
                   float(np.allclose(paths[:, 0], 100.0)), 1.0, tol=0.5)

        p  = probability_above(paths, 110.0)
        r3 = check("P(S_T > 110)  ~ 0.42",  p,  0.42, tol=0.04)

        e  = expected_final_price(paths)
        r4 = check("E[S_T]        ~ 110.52", e, 110.52, tol=1.5)

        return all([r1, r2, r3, r4])
    except Exception as exc:
        print(f"  ERROR: {exc}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("  Monte Carlo Seminar -- Test Suite")
    print("=" * 60)

    t1 = test_task1()
    t2 = test_task2()
    t3 = test_task3()

    print("\n" + "=" * 60)
    total = sum([t1, t2, t3])
    print(f"  Result: {total}/3 tasks passed")
    if total == 3:
        print("  All tests passed. Great work.")
    else:
        print("  Keep going -- check the [FAIL] lines above for hints.")
    print("=" * 60)

    sys.exit(0 if total == 3 else 1)
