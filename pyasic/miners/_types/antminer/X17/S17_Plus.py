from pyasic.miners import BaseMiner


class S17Plus(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "S17+"
        self.nominal_chips = 65
        self.fan_count = 4