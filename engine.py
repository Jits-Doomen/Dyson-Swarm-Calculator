import math
from dataclasses import dataclass

@dataclass(frozen=True)
class SwarmResult:
    radius_km: float
    orbital_period_days: float
    total_mass_kg: float
    area_mass_limit: float
    actual_am_ratio: float

class DysonSwarmEngine:
    def __init__(self, config):
        self.pi = config.PI
        self.c = config.C
        self.L = config.L
        self.M = config.M
        self.G = config.G
        self.sigma = config.SIGMA
        self.sgp = config.G * config.M
        self.K = 1e7

    def calculate_power_harvested(self, D, P_factor):
        total_power_watts = self.L * P_factor
        return total_power_watts

    def calculate_swarm(self, T, H, rho, P_factor) -> SwarmResult:
        D = math.sqrt(self.L / (16 * self.pi * self.sigma * T**4))

        area_mass_ratio = 1 / (H * rho)
        area_mass_limit = (4 * self.pi * self.G * self.M * self.c) / self.L

        beta = area_mass_ratio / area_mass_limit

        effective_sgp = self.sgp * (1 - beta)

        if effective_sgp > 0:
            P_orb_sec = 2 * self.pi * math.sqrt(D**3 / effective_sgp)
        else:
            P_orb_sec = float('inf')

        P_orb_days = P_orb_sec / 86400

        M_total = (4 * self.pi * D**2) * H * rho * P_factor

        return SwarmResult(D, P_orb_days, M_total, area_mass_limit, area_mass_ratio)

    def calculate_delta_v(self, D):
        R1 = 1.496e11
        R2 = D
        Atrans = (R1 + R2) / 2
        TravelTime = self.pi * math.sqrt(Atrans**3 / self.sgp)
        Vc1 = math.sqrt(self.sgp / R1)
        Vc2 = math.sqrt(self.sgp / R2)
        Vtrans1 = math.sqrt(self.sgp * (2 / R1 - 1 / Atrans))
        Vtrans2 = math.sqrt(self.sgp * (2 / R2 - 1 / Atrans))
        return (abs(Vc1 - Vtrans1) + abs(Vc2 - Vtrans2)), TravelTime

    def calculate_resource_cost(self, M_total):
        return M_total / 3.301e23, M_total / 7.348e22

    def _get_annual_capacity(self, year):
        K = self.K
        k = 0.1
        t0 = 20
        exponent = -k * (year - t0)
        if exponent > 100:
            return 1
        capacity = K / (1 + math.exp(exponent))
        return max(1, capacity)

    def calculate_mission_stats(self, D, P_factor, M_total, sat_size_km, mobilization_factor):
        sat_count = (4 * self.pi * D**2 * P_factor) / ((sat_size_km**2) * 1e6)
        years_elapsed = 0
        sats_built = 0
        max_years = 10000

        while sats_built < sat_count and years_elapsed < max_years:
            progress_ratio = sats_built / sat_count
            current_power = (self.L * P_factor) * progress_ratio

            dynamic_K = max(1e7, current_power * 1e-12)

            capacity = (dynamic_K / (1 + math.exp(-0.1 * (years_elapsed - 20)))) * mobilization_factor

            sats_built += capacity
            years_elapsed += 1

        return sat_count, years_elapsed, sat_count * 0.01
