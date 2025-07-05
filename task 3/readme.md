# Task 4 - Optimization Model

## Overview
This project solves a business optimization problem using linear programming. The goal is to maximize profit based on product constraints like labor and machine hours.

## Technologies Used
- Python
- PuLP (Linear Programming Library)

## Problem Statement
Maximize profit by deciding how many units of Product A and Product B to produce under limited resources.

### Objective Function
Maximize: `20A + 30B`

### Constraints
- `2A + 4B ≤ 100` (Labor)
- `3A + 1B ≤ 90` (Machine)

## Output
- Optimal number of each product to produce
- Maximum profit achieved

## How to Run
```bash
python optimization_model.py
