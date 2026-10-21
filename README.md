# Day 2 — The Maths That Actually Matters

AI & ML Internship — Week 1: Foundations & Classical ML (Part 1)

## Roadmap goals

The Day 2 roadmap asks for:
- Linear algebra: vectors, dot product, matrix multiplication, and why datasets are matrices.
- Probability and statistics: mean, variance, distributions, conditional probability, Bayes' theorem, and correlation versus causation.
- Calculus: derivative as slope, partial derivatives, gradient, and chain rule.
- Gradient descent: learning rate, local minima, and convergence.
- NumPy implementations of dot product, matrix multiplication, and normalization.
- Gradient descent from scratch for `f(x) = x² + 3x + 4`, with a plot of the descent path.
- A two-variable extension, testing learning rates `0.001`, `0.01`, `0.5`, and `1.5`, with a written explanation of their effects.

## Files

- `math_matters.py` — NumPy examples for dot product, matrix multiplication, and min-max normalization.
- `scratch_mini.py` — one-variable gradient descent for `f(x) = x² + 3x + 4`, including a plotted descent path. The current script uses learning rate `0.1`.
- `gradiant_decent_2var.py` — gradient descent for the two-variable function `f(x, y) = x² + y²`. The current script uses learning rate `1.5`.

## Run locally

Install the libraries used by these scripts:

```bash
python -m pip install numpy matplotlib
```

Run each exercise:

```bash
python math_matters.py
python scratch_mini.py
python gradiant_decent_2var.py
```

## Learning-rate experiment status

The uploaded scripts demonstrate the required core exercises, but they do **not yet** run all four roadmap learning rates (`0.001`, `0.01`, `0.5`, `1.5`) side by side or include a full written comparison. Add that experiment and explanation to complete the roadmap deliverable.

These are practice scripts from the internship learning exercises.
