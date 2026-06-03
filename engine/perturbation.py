import math

class PerturbationModule:
    def __init__(self, threshold=1e-9):
        self.threshold = threshold

    def finite_disk_bottleneck(self, r_m):
        if r_m <= 6.957e8:
            return 1.0
        return (6.957e8 / r_m) ** 2

    def drift_risk(self, r_m):
        x = self.finite_disk_bottleneck(r_m)
        return x > self.threshold

    def maintenance_requirement(self, r_m, beta, base_rate=0.01):
        proximity = 1.496e11 / max(r_m, 1e-30)
        return base_rate * proximity * beta

    def stationkeeping_cost(self, r_m, beta, mass):
        base = self.maintenance_requirement(r_m, beta)
        return base * mass