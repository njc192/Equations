from mpmath import *


class Unit:
    def __init__(self):
        self.dict_units = {}
        self.letter_conversion = {}

        # set the precision of the numbers
        mp.prec = 40

        self.dict_units["meter"] = mpf(1)
        self.dict_units["gram"] = mpf(1)
        self.dict_units["second"] = mpf(1)
        # big

        self.dict_units["kilo"] = pow(mpf(10), 3)
        self.dict_units["mega"] = pow(mpf(10), 6)
        self.dict_units["giga"] = pow(mpf(10), 9)
        self.dict_units["tera"] = pow(mpf(10), 12)

        self.dict_units["centi"] = pow(mpf(10), -2)
        self.dict_units["milli"] = pow(mpf(10), -3)
        self.dict_units["micro"] = pow(mpf(10), -6)
        self.dict_units["nano"] = pow(mpf(10), -9)
        self.dict_units["pico"] = pow(mpf(10), -12)

        self.letter_conversion['k'] = "kilo"
        self.letter_conversion['M'] = "mega"
        self.letter_conversion['G'] = "giga"
        self.letter_conversion["T"] = "tera"

        self.letter_conversion['c'] = "centi"
        self.letter_conversion['m'] = "milli"
        self.letter_conversion['u'] = "micro"
        self.letter_conversion['n'] = "nano"
        self.letter_conversion['p'] = "pico"

    def convert(self, value, unit_of_measurement_start: str, unit_of_measurement_end: str):
        u1 = unit_of_measurement_start
        u2 = unit_of_measurement_end
        base_unit1 = self.get_base_unit(u1)
        base_unit2 = self.get_base_unit(u2)

        if base_unit1 != base_unit2:  # base units are the same e.g. meter to meter
            return Exception(f"Base {base_unit1} does not match {base_unit2}")

        x1 = self.get_value_for_letter(u1)

        x2 = self.get_value_for_letter(u2)

        valid_units = x2 is not None and x1 is not None
        if valid_units:
            answer = value * (x1 / x2)
            print(f"Convert: {value} {u1} to {u2} : {answer} {u2} \n\n")
            return answer

    def convert_to_base(self, value, unit_of_measurement):
        base_unit = self.get_base_unit(unit_of_measurement)
        return self.convert(value, unit_of_measurement, base_unit[0])

    def get_base_unit(self, x1: str):
        if len(x1) == 1:
            base_unit = x1[0]
        else:
            base_unit = x1[1]
        if base_unit == "m":
            return "meter"
        if base_unit == "s":
            return "second"
        if base_unit == "g":
            return "gram"

        if self.dict_units.get(base_unit) is not None:
            return base_unit
        return f"Invalid Base Unit : {base_unit}"

    def get_value_for_letter(self, arg):
        if len(arg) == 1:
            return 1
        return self.dict_units[self.letter_conversion[arg[0]]]


if __name__ == '__main__':
    u = Unit()
    print(nstr(u.convert(12, "km", "um"), 3))
