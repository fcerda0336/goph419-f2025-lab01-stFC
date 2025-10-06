# goph419-f2025-lab01-stFC

Lab assignment 01 -  Implementation and algorithm to compute the allowable range of launch angle for the rocket system.



* \* Fall Semester 2025
* \* Instructor		: B. Karchewski
* \* Author :		:  Fernando Cerda
* University of Calgary – Computational Methods for Geophysics (F2025)## Projectile Motion and Taylor Series Approximation
* ---
* \### ## Description
* This project implements basic mathematical functions (square root, arcsine, and projectile motion calculations) in Python and validates them using unit tests.
* .
* 
* ---
* 
* \### Repository Contents
* \- `driver.py` — main script to run the program and generate figures  
* \- `functions.py` — contains computational routines (Taylor expansions and angle calculations)  
* \- `tests.py` — optional testing file It gave me some problems but it is fixed  
* \- `requirements.txt` — lists Python dependencies  
* \- `README.md` — this file  
* 
* ---
* 
* \###  To execute the main driver script and generate results:

* \- python examples/driver.py
* \-The program will:
* \-Compute valid launch angles for input parameters (ve/v0, α, tol_α)
* \-Plot launch angles versus altitude fraction (α)
* \-Plot launch angles versus velocity ratio (ve/v0)


* \### ## Usage
* \-To run all tests:
* \-python tests/tests.py
* \-python -m unittest tests/tests.py
