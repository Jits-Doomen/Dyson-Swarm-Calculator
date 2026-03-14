class Units:
    KM_TO_MILES = 0.621371
    KG_TO_LBS = 2.20462

    def __init__(self, mode):
        self.is_metric = (mode.upper() == "EU")

    def format_dist(self, km):
        dist = km * self.KM_TO_MILES if not self.is_metric else km

        if dist >= 1_000_000:
            val = dist / 1_000_000
            unit = "million km" if self.is_metric else "million miles"
        else:
            val = dist
            unit = "km" if self.is_metric else "miles"

        return f"{val:.2f} {unit}"

    def format_mass(self, kg):
        val = kg if self.is_metric else kg * self.KG_TO_LBS
        unit = "kg" if self.is_metric else "lbs"
        return f"{val:.2e} {unit}"
