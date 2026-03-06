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

    def calculate_swarm(self, T, H, rho, P_factor) -> SwarmResult:
        D = math.sqrt(self.L / (16 * self.pi * self.sigma * T**4))
        AreaMassLimit = (4 * self.pi * self.G * self.M * self.c) / self.L
        M_total = (4 * self.pi * D**2) * H * rho * P_factor
        P_orb_sec = 2 * self.pi * math.sqrt(D**3 / self.sgp)
        P_orb_days = P_orb_sec / 86400
        Actual_AM = 1 / (H * rho)

        return SwarmResult(D, P_orb_days, M_total, AreaMassLimit, Actual_AM)

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

    def calculate_mission_stats(self, D, P_factor, M_total, sat_size_km):
        sat_count = (4 * self.pi * D**2 * P_factor) / ((sat_size_km**2) * 1e6)
        construction_years = 0.875 * math.log2(M_total / 450000) if M_total > 450000 else 0
        return sat_count, construction_years, sat_count * 0.01