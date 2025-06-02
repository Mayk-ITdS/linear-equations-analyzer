  # Linear Equations Analyzer

A Python program for solving and analyzing linear systems of equations using Gaussian elimination with partial pivoting.

## Features

- Solve systems of linear equations using Gaussian elimination
- Handles inconsistent and infinite solution systems
- Random matrix generation with custom size and value range
- Manual matrix input with validation
- Pretty console output with aligned matrix formatting
- Automatic detection of system type:
  - No solution (inconsistent)
  - Unique solution
  - Infinitely many solutions
- Performance timing for matrix generation and computation

## How It Works

1. Choose between manual input or random matrix generation.
2. The program applies Gaussian elimination with partial pivoting.
3. After row-reduction, the rank of the matrix is used to classify the system.
4. Displays the original matrix, its row-echelon form (full and rounded), and solution status.

## Getting Started

### Requirements

- Python 3.x

### Run

```bash
python uklad_rownan.py
