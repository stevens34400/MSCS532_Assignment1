# MSCS532_Assignment1

## Overview
This repository contains an implementation of the Insertion Sort algorithm in Python, specifically designed to sort arrays in descending order. This project was created for MSCS532 (Data Structures and Algorithms) Assignment 1.

## Features
- **Insertion Sort Algorithm**: Implements the classic insertion sort algorithm
- **Descending Order**: Sorts arrays in decreasing order (largest to smallest)
- **Interactive Input**: Accepts user input for dynamic testing

## Algorithm Details

### Insertion Sort
The insertion sort algorithm builds the final sorted array one item at a time. Each iteration takes an element from the unsorted part and inserts it into its correct position in the sorted part.

**Time Complexity**: O(n²) - worst and average case  
**Space Complexity**: O(1) - in-place sorting

### How It Works
1. Start with the second element (index 1) since the first element is considered sorted
2. Compare the current element with the previous elements
3. Shift larger elements to the right to make space for the current element
4. Insert the current element into its correct position
5. Repeat until all elements are sorted

## Usage

### Running the Program
```bash
python insertion_sort.py
```

### Input Format
Enter numbers separated by spaces when prompted:

Enter numbers separated by spaces (e.g., 5 2 9 1 5 6):
5 2 9 1 5 6

### Example Output
Original array: [5, 2, 9, 1, 5, 6]
Sorted in decreasing order: [9, 6, 5, 5, 2, 1]
## File Structure
```
532_assignment1/
├── insertion_sort.py    # Main implementation file
└── README.md           # This file
```

## Requirements
- Python 3.x
- No external dependencies required

## Author
Created for MSCS532 Data Structures and Algorithms Assignment 1

## License
This project is created for educational purposes as part of MSCS532 coursework.