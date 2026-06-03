import math

class MissionModule:
    def calculate_costs(self, M_total):
        merc = M_total / 3.301e23
        moon = M_total / 7.348e22
        return merc, moon

    def simulate_construction(self, r_m, P_factor, M_total, sat_size_km, mob, L):
        sat_area = (sat_size_km * 1000) ** 2
        target = (4 * math.pi * r_m * r_m * P_factor) / max(sat_area, 1e-30)

        built = 0.0
        year = 0
        max_years = 50000

        while built < target and year < max_years:
            progress = built / max(target, 1e-30)

            power = L * P_factor * progress
            efficiency = max(1e7, power * 1e-12)

            logistic = 1 / (1 + math.exp(-0.1 * (year - 20)))

            capacity = efficiency * logistic * mob

            built += capacity
            year += 1

            if capacity < 1e-6:
                break

        return target, year