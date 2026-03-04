import math

pi = math.pi
c = 299_792_458
L = 3.828e26
M = 1.989e30
G = 6.674e-11
sigma = 5.670e-8
T = float(input("Enter the maximum temperature of the swarm in K: "))
H = float(input("Enter the Panel Thickness of every satellite in m: "))
rho = float(input("Enter the density of the material in kg/m^3: "))
P_factor = float(input("Enter the coverage factor (0.0 to 1.0): "))

## Calculates the Stefan-Boltzmann Law. (Had to Google(trademark logo) the name)
D = math.sqrt(L / (16 * pi * sigma * T**4))

## Calculates the Eddington Ratio Reciprocal. (Had to Google(trademark logo) the name again, I am bad at remembering.)
AreaMass = (4 * pi * G * M * c) / L

## Formula for Total Mass of a Spherical Shell
M_total = (4 * pi * D**2) * H * rho * P_factor

#3 Keplers third law (:
P_orb_sec = 2 * pi * math.sqrt(D**3 / (G * M))
## Turns it into days
P_orb_days = P_orb_sec / 86400

print("Dyson Swarm Results:")
print(f"Radius {D/1e9:.2f} million km")
print(f"Orbital Period {P_orb_days:.1f} days")
print(f"Total Mass {M_total:.2e} kg")
print(f"Area/Mass Ratio: {AreaMass:.3f} m^2/kg")