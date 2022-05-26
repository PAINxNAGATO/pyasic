from dataclasses import dataclass, field, asdict


@dataclass
class MinerData:
    ip: str
    model: str = "Unknown"
    hostname: str = "Unknown"
    hashrate: float = 0
    temperature_avg: int = field(init=False)
    left_board_temp: int = 0
    left_board_chip_temp: int = 0
    center_board_temp: int = 0
    center_board_chip_temp: int = 0
    right_board_temp: int = 0
    right_board_chip_temp: int = 0
    wattage: int = 0
    fan_1: int = -1
    fan_2: int = -1
    fan_3: int = -1
    fan_4: int = -1
    left_chips: int = 0
    center_chips: int = 0
    right_chips: int = 0
    total_chips: int = field(init=False)
    ideal_chips: int = 1
    percent_ideal: float = field(init=False)
    nominal: int = field(init=False)
    pool_split: str = 0
    pool_1_url: str = "Unknown"
    pool_1_user: str = "Unknown"
    pool_2_url: str = ""
    pool_2_user: str = ""

    @property
    def total_chips(self):  # noqa - Skip PyCharm inspection
        return self.right_chips + self.center_chips + self.left_chips

    @total_chips.setter
    def total_chips(self, val):
        pass

    @property
    def nominal(self):  # noqa - Skip PyCharm inspection
        return self.ideal_chips == self.total_chips

    @nominal.setter
    def nominal(self, val):
        pass

    @property
    def percent_ideal(self):  # noqa - Skip PyCharm inspection
        return round((self.total_chips / self.ideal_chips) * 100)

    @percent_ideal.setter
    def percent_ideal(self, val):
        pass

    @property
    def temperature_avg(self):  # noqa - Skip PyCharm inspection
        total_temp = 0
        temp_count = 0
        for temp in [
            self.left_board_chip_temp,
            self.center_board_chip_temp,
            self.right_board_chip_temp,
        ]:
            if not temp == 0:
                total_temp += temp
                temp_count += 1
        if not temp_count > 0:
            return 0
        return round(total_temp / temp_count)

    @temperature_avg.setter
    def temperature_avg(self, val):
        pass

    def asdict(self):
        return asdict(self)