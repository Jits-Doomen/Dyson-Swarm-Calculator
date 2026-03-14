# Dyson Swarm Calculator

**A physics-based simulator for Type II Civilizational Engineering.**

This engine models the physical and logistical requirements for constructing a **Dyson Swarm**—a megastructure of quadrillions of solar collectors—around a G-type star. It translates abstract astrophysical concepts into concrete engineering data, such as construction timelines, planetary consumption, and orbital stability.
___
## Core Physics

The simulator evaluates the swarm's possibility by solving for four primary variables:
_
### 1. Thermal Equilibrium (The "Goldilocks" Radius)

Using the **Stefan-Boltzmann Law**, we calculate the distance where a satellite maintains a specific operating temperature . This prevents the swarm from melting or freezing.
_
### 2. Orbital Dynamics

Utilizing **Kepler's Third Law**, the engine determines the orbital period and the necessary Delta-V to reach the swarm's destination from a 1 AU (Earth-like) starting point.
_
### 3. The Statite Limit (Radiation Pressure)

A critical feature of this engine is the calculation of the **Area-to-Mass (A/m) Ratio**. This determines if a satellite is "Heavy" (gravity dominated) or a "Light Sail" (radiation pressure dominated).

> **Critical Limit:** For Sol, the balance point is **1.305 m^2/kg**. If a panel exceeds this, it will be blown out of the solar system by sunlight.

### 4. Hyper-Exponential Growth

Unlike linear construction models, this simulator accounts for **Positive Feedback Loops**. It models self-replicating robots that use the energy from active satellites to accelerate the production of new ones.
___
## Output Metrics

When you run the simulation, you receive a full mission report:

* **Planetary Consumption:** How many Mercuries or Moons must be deconstructed to build it.
* **Mission Operations:** Total satellite count and annual maintenance.
* **Construction Timeline:** Total years required using exponential industrial models.
___
## Usage

### Prerequisites

* Python 3.8 or higher.
* `math` library (Standard library).

### Installation

```bash
git clone https://github.com/Jits-Doomen/Dyson-Swarm-Calculator.git
cd Dyson-Swarm-Calculator
py main.py
```
___
## Usage Example

**Input Scenario:**

* **Target Temp:** 825K
* **Coverage:** 50%
* **Thickness:** 5cm

**Engine Output:**

> **Recommendation:** Deconstruct 57% of Mercury.
> **Timeline:** 51.23 years (Unified Humanity Mobilization).
> **Status:** Gravitationally Stable.
