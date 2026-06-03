import math

class PhysicsModule:
    def __init__(self, config):
        self.pi = config.PI
        self.G = config.G
        self.M = config.M
        self.c = config.C
        self.L = config.L
        self.R_sun = 6.957e8
        self.sgp = self.G * self.M

    def get_radius(self, T):
        return math.sqrt(self.L / (16 * self.pi * 5.67e-8 * T**4))

    def orbit_elements(self, r_m, H, rho):
        area_mass_ratio = 1 / (H * rho)
        area_mass_limit = (4 * self.pi * self.G * self.M * self.c) / self.L

        beta = area_mass_ratio / max(area_mass_limit, 1e-30)
        effective_mu = self.sgp * (1 - min(beta, 0.999999))

        period = 2 * self.pi * math.sqrt(r_m**3 / max(effective_mu, 1e-30)) / 86400

        return area_mass_ratio, area_mass_limit, period

    def solar_flux(self, r_m):
        return self.L / (4 * self.pi * r_m * r_m)

    def finite_disk_factor(self, r_m):
        if r_m <= self.R_sun:
            return 0.0
        x = self.R_sun / r_m
        return math.sqrt(max(0.0, 1 - x * x))

    def radiation_pressure(self, r_m, P_factor, cos_inc=1.0):
        flux = self.solar_flux(r_m)
        disk = self.finite_disk_factor(r_m)
        return (flux / self.c) * P_factor * disk * max(0.0, cos_inc)

    def calculate_delta_v(self, D_km):
        R1 = 1.496e11
        R2 = D_km * 1000
        a = (R1 + R2) / 2

        mu = self.sgp

        v1 = math.sqrt(mu / R1)
        v2 = math.sqrt(mu / R2)
        vt1 = math.sqrt(mu * (2 / R1 - 1 / a))
        vt2 = math.sqrt(mu * (2 / R2 - 1 / a))

        return abs(vt1 - v1) + abs(v2 - vt2), math.pi * math.sqrt(a**3 / mu)