from config import PhysicalConstants
from constants import MATERIALS
from engine import DysonSwarmEngine

def main():

    mob_input = float(input("\nEnter global resource mobilization factor (0.0 to 1.0): "))
    print("\nChoose your desired material:")
    for k, v in MATERIALS.items():
        print(f"{k}: {v[0]} ({v[1]} kg/m^3)")
    choice = input("\nSelect Material (1-4): ")
    mat_name, rho = MATERIALS.get(choice, ("Standard Dyson Material", 2000))
    T = float(input("Enter max temperature (K): "))
    H = float(input("Enter Panel Thickness (m): "))
    P_factor = float(input("Enter coverage factor (0.0 to 1.0): "))
    sat_size = float(input("Enter side-length of one satellite in km: "))

    engine = DysonSwarmEngine(PhysicalConstants())
    res = engine.calculate_swarm(T, H, rho, P_factor)
    total_dv, travel_time_sec = engine.calculate_delta_v(res.radius_km)
    merc_cost, moon_cost = engine.calculate_resource_cost(res.total_mass_kg)
    sat_count, build_time, maintenance = engine.calculate_mission_stats(res.radius_km, P_factor, res.total_mass_kg, sat_size, mob_input)

    print(f"\nResults for {mat_name}")
    print(f"Radius: {res.radius_km/1e9:.2f} million km")
    print(f"Total Mass: {res.total_mass_kg:.2e} kg")
    print(f"Panel Area/Mass Ratio: {res.actual_am_ratio:.3f} m^2/kg (Limit: {res.area_mass_limit:.3f})")

    print("\nPlanning")
    print(f"Total Delta-V Cost: {total_dv:.2f} m/s")
    print(f"Transfer Time: {travel_time_sec / 86400:.2f} days")
    print(f"Orbital Period: {res.orbital_period_days:.2f} days")

    print("\nPlanetary Consumption")
    print(f"Mercury-mass Planets: {merc_cost:.2f}")
    print(f"Moon-mass Objects: {moon_cost:.2f}")

    print(f"\nMission Operations ({mob_input * 100:.0f}% Mobilization / Exponential Growth)")
    print(f"Total Satellites: {sat_count:.2e}")

    time_display = f"{build_time:.2f} years" if isinstance(build_time, (int, float)) else build_time
    print(f"Theoretical Min. Construction Time: {build_time:.2f} years")
    print("\n*Note: Assumes the best fitting exponential manufacturing growth without logistic bottlenecks.")
    print(f"Annual Maintenance: {maintenance:.2e} replacements/year")

    total_power = engine.calculate_power_harvested(res.radius_km * 1e3, P_factor)
    print(f"\nEnergy Potential")
    print(f"Total Power Harvested: {total_power:.2e} Watts")
    print(f"Efficiency: {(total_power / res.total_mass_kg):.2f} Watts/kg")

    if res.actual_am_ratio > res.area_mass_limit:
        print("\nCRITICAL WARNING: Radiation pressure exceeds gravity! Swarm will drift away without tethers.")
    else:
        print("\nSwarm Status: Gravitationally stable orbit.")
    print("Recommendation: Use the moon." if moon_cost <= 1 else "Recommendation: Deconstruct Mercury.")

if __name__ == "__main__":
    main()
