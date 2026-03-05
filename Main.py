import math

class DysonSwarmEngine:
    def __init__(self):
        self.pi = math.pi
        self.c = 299_792_458
        self.L = 3.828e26
        self.M = 1.989e30
        self.G = 6.674e-11
        self.sigma = 5.670e-8
        self.sgp = self.G * self.M

    def calculate_swarm(self, T, H, rho, P_factor):
        D = math.sqrt(self.L / (16 * self.pi * self.sigma * T**4))
        AreaMassLimit = (4 * self.pi * self.G * self.M * self.c) / self.L
        M_total = (4 * self.pi * D**2) * H * rho * P_factor
        P_orb_sec = 2 * self.pi * math.sqrt(D**3 / self.sgp)
        P_orb_days = P_orb_sec / 86400

        Actual_AM = 1 / (H * rho)

        return D, P_orb_days, M_total, AreaMassLimit, Actual_AM

    def calculate_delta_v(self, D):
        R1 = 1.496e11
        R2 = D
        Atrans = (R1 + R2) / 2
        TravelTime = self.pi * math.sqrt(Atrans**3 / self.sgp)
        Vc1 = math.sqrt(self.sgp / R1)
        Vc2 = math.sqrt(self.sgp / R2)
        Vtrans1 = math.sqrt(self.sgp * (2 / R1 - 1 / Atrans))
        Vtrans2 = math.sqrt(self.sgp * (2 / R2 - 1 / Atrans))
        dv1 = abs(Vc1 - Vtrans1)
        dv2 = abs(Vc2 - Vtrans2)
        return (dv1 + dv2), TravelTime

    def calculate_resource_cost(self, M_total):
        m_moon = 7.348e22
        m_mercury = 3.301e23
        return M_total / m_mercury, M_total / m_moon

    def calculate_mission_stats(self, D, P_factor, M_total, sat_size_km):
        surfasphere = (4 * self.pi * D**2)
        total_area_needed = surfasphere * P_factor
        sat_area_m2 = (sat_size_km**2) * 1e6
        sat_count = total_area_needed / sat_area_m2

        m_initial = 450000

        initial_doubling_time = 1.5
        final_doubling_time = 0.25
        avg_doubling_time = (initial_doubling_time + final_doubling_time) / 2

        if M_total > m_initial:
            construction_years = avg_doubling_time * math.log2(M_total / m_initial)
        else:
            construction_years = 0

        failure_rate = 0.01
        maintenance_load = sat_count * failure_rate

        return sat_count, construction_years, maintenance_load

def main():
    materials = {
        "1": ("Carbon Fiber / Alloy", 1600),
        "2": ("Standard Dyson Material", 2000),
        "3": ("Iron / Steel Shell", 7800),
        "4": ("Heavy Shielding (Lead)", 11340)
    }

    print("\nChoose your desired material:")
    for k, v in materials.items():
        print(f"{k}: {v[0]} ({v[1]} kg/m^3)")

    choice = input("\nSelect Material (1-4): ")
    mat_name, rho = materials.get(choice, ("Standard Dyson Material", 2000))

    T = float(input("Enter max temperature (K): "))
    H = float(input("Enter Panel Thickness (m): "))
    P_factor = float(input("Enter coverage factor (0.0 to 1.0): "))
    sat_size = float(input("Enter side-length of one satellite in km (e.g., 1.0): "))

    engine = DysonSwarmEngine()

    D, P_orb_days, M_total, AM_Limit, Actual_AM = engine.calculate_swarm(T, H, rho, P_factor)
    total_dv, travel_time_sec = engine.calculate_delta_v(D)
    merc_cost, moon_cost = engine.calculate_resource_cost(M_total)

    sat_count, build_time, maintenance = engine.calculate_mission_stats(D, P_factor, M_total, sat_size)

    print(f"\nResults for {mat_name}")
    print(f"Radius: {D/1e9:.2f} million km")
    print(f"Total Mass: {M_total:.2e} kg")
    print(f"Panel Area/Mass Ratio: {Actual_AM:.3f} m^2/kg (Limit: {AM_Limit:.3f})")

    print("\nPlanning")
    print(f"Total Delta-V Cost: {total_dv:.2f} m/s")
    print(f"Transfer Time: {travel_time_sec / 86400:.2f} days")
    print(f"Orbital Period: {P_orb_days:.2f} days")

    print("\nPlanetary Consumption")
    print(f"Mercury-mass Planets: {merc_cost:.2f}")
    print(f"Moon-mass Objects: {moon_cost:.2f}")

    print("\nMission Operations (75% Mobilization / Exponential Growth)")
    print(f"Total Satellites: {sat_count:.2e}")
    print(f"Construction Time: {build_time:.2f} years")
    print(f"Annual Maintenance: {maintenance:.2e} replacements/year")

    if Actual_AM > AM_Limit:
        print("\nCRITICAL WARNING: Radiation pressure exceeds gravity! Swarm will drift away without tethers.")
    else:
        print("\nSwarm Status: Gravitationally stable orbit.")

    if moon_cost <= 1:
        print("Recommendation: Use the moon.")
    else:
        print("Recommendation: Deconstruct Mercury.")

if __name__ == "__main__":
    main()
