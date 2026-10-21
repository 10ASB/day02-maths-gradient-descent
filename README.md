# Day 2 — The Maths That Actually Matters

AI & ML Internship — Week 1: Foundations & Classical ML (Part 1)

## Topics covered
- Vector dot product
- Matrix multiplication
- Min-max normalization
- Partial derivatives
- Gradient descent on a two-variable function

## Files
- `math_matters.py` — NumPy examples for dot product, matrix multiplication, and min-max normalization.
- `gradiant_decent_2var.py` — gradient descent for the function \(f(x,y)=x^2+y^2\).

## Run locally
Install NumPy first:

```bash
python -m pip install numpy
python math_matters.py
python gradiant_decent_2var.py
```

`math_matters.py` also imports Matplotlib, although the current example does not use it.

## Learning note
Gradient descent updates parameters in the direction opposite to the gradient. The learning rate controls the size of each update; if it is too large, the steps can overshoot the minimum.

These are practice scripts from the internship learning exercises.
