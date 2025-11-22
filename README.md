# Package Sorter - Robotic Automation Factory

## Overview
This project implements a package sorting system for Thoughtful's robotic automation factory. The system classifies packages into three stacks (STANDARD, SPECIAL, or REJECTED) based on their dimensions and mass.

## Purpose
The robotic arm uses this function to automatically dispatch packages to the correct stack for processing.

## Current State
Fully implemented and tested with 14 comprehensive unit tests, all passing.

## Recent Changes
- Created `sort(width, height, length, mass)` function in `package_sorter.py`
- Implemented bulky detection (volume >= 1,000,000 cm³ OR any dimension >= 150 cm)
- Implemented heavy detection (mass >= 20 kg)
- Created 14 unit tests covering all edge cases
- Added example usage in `main.py`

## Project Architecture

### Files
- `package_sorter.py`: Core sorting function implementation
- `main.py`: Example usage and test runner
- `test_package_sorter.py`: Comprehensive unit tests
- `.gitignore`: Python-specific ignore patterns

### Sorting Rules
1. **STANDARD**: Packages that are neither bulky nor heavy
2. **SPECIAL**: Packages that are either bulky OR heavy (but not both)
3. **REJECTED**: Packages that are both bulky AND heavy

### Classification Criteria
- **Bulky**: Volume >= 1,000,000 cm³ OR any dimension >= 150 cm
- **Heavy**: Mass >= 20 kg

## Usage
```python
from package_sorter import sort

# Returns "STANDARD", "SPECIAL", or "REJECTED"
result = sort(width=50, height=50, length=50, mass=10)
```

## Running Tests
Execute `python main.py` to see example outputs and run all unit tests.
