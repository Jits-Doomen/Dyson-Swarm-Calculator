### Dyson Swarm Calculator 
___
# Dyson Swarm Parameter Calculator.

**A physics-based study for mega-scale orbital energy structures to bring us to a Type II civilization on the Kardashev scale.**

This repository contains a Python implementation of a Dyson Swarm feasibility model. It derives the necessary physical constraints (distance, mass, and orbital dynamics) required to construct an energy-collection shell around a star.
___
##  Physics Implementation

The simulator uses four important laws of astrophysics to determine the eventual results:

1. **Thermal Equilibrium (Stefan-Boltzmann Law)**:
Calculates the orbital radius ($D$) where a satellite maintains a specific temperature ($T$) based on the star's luminosity ($L$).

$$D = \sqrt{\frac{L}{16 \pi \sigma T^4}}$$

2. **Orbital Mechanics (Kepler's Third Law)**:
Determines the time ($P$) it takes for a swarm element to complete one revolution.

$$P = 2\pi\sqrt{\frac{D^3}{GM}}$$

3. **The "Statite" Limit (Eddington Ratio Reciprocal)**:
Derives the required **Area-to-Mass ratio** ($A/m$) where radiation pressure equals gravitational pull, allowing satellites to "hover" without orbiting.
4. **Integrated Shell Mass**:
Estimates the total planetary material required based on panel thickness, density, and swarm coverage.
___
## Example Results (Sol-Based)

Using the solar constant and a target temperature of **373K** (the boiling point of water):

* **Orbital Radius:** 84.34 million km (0.56 AU)
* **Orbital Period:** 151.7 Earth Days
* **Critical A/m Ratio:** 1.305 $m^2/kg$
___
## How to Use

1. **Clone the repo**: `git clone https://github.com/Jits-Doomen/Dyson-Swarm-Simulator.git`
2. **Run the script**: `python dyson_swarm.py`
3. **Input Constants**: Enter your own custom star luminosity or material density to test different star systems.
