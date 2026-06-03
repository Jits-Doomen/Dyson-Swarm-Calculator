import math
from dataclasses import dataclass
from .physics import PhysicsModule
from .perturbation import PerturbationModule
from .mission import MissionModule

@dataclass(frozen=True)
class SwarmResult:
    radius_km: float
    orbital_period_days: float
    total_mass_kg: float
    area_mass_limit: float
    actual_am_ratio: float
    drift_warning: bool

class DysonSwarmEngine:
    def __init__(self, config):
        self.physics = PhysicsModule(config)
        self.perturb = PerturbationModule()
        self.mission = MissionModule()
        self.L = config.L

    def calculate_swarm(self, T, H, rho, P_factor):
        r_m = self.physics.get_radius(T)

        am_ratio, am_limit, period = self.physics.orbit_elements(r_m, H, rho)

        mass = 4 * math.pi * r_m * r_m * H * rho * P_factor

        drift = self.perturb.drift_risk(r_m)

        return SwarmResult(
            r_m / 1000,
            period,
            mass,
            am_limit,
            am_ratio,
            drift
        )

    def calculate_delta_v(self, r_km):
        return self.physics.calculate_delta_v(r_km)

    def calculate_resource_cost(self, M_total):
        return self.mission.calculate_costs(M_total)

    def calculate_mission_stats(self, r_km, P_factor, M_total, sat_size, mob):
        r_m = r_km * 1000

        target, years = self.mission.simulate_construction(
            r_m, P_factor, M_total, sat_size, mob, self.L
        )

        beta = self.physics.beta(r_m, M_total / max(target, 1e-30))

        maint = self.perturb.stationkeeping_cost(r_m, beta, M_total)

        return target, years, maint

    def calculate_power_harvested(self, r_km, P_factor):
        r_m = r_km * 1000
        return self.physics.radiation_pressure(r_m, P_factor)
