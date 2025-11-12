# Fibonacci Sequence Generator

This project contains a simple Python implementation that generates the Fibonacci sequence using a for loop.

## Overview

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence typically starts with 0 and 1:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

## Files

- `fibForLoop.py` - Main implementation using a for loop to generate the first 12 numbers of the Fibonacci sequence

## How it Works

The program uses an iterative approach with a for loop:

1. Initializes the first two Fibonacci numbers (0 and 1)
2. Prints the initial values
3. Uses a loop to calculate and print the next 10 numbers
4. Each new number is calculated by adding the two previous numbers
5. Updates the previous values for the next iteration

## Usage

To run the program:

```bash
python fibForLoop.py
```

## Output

The program will output the first 12 numbers of the Fibonacci sequence:
```
0
1
1
2
3
5
8
13
21
34
55
89
```

## Algorithm Complexity

- **Time Complexity**: O(n) - where n is the number of Fibonacci numbers to generate
- **Space Complexity**: O(1) - uses only a constant amount of extra space

## Requirements

- Python 3.x

## Author

Created as a learning exercise for implementing the Fibonacci sequence.