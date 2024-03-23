class BMI:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    def BMI_Value(self):
        return self.berat / (self.tinggi ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.berat == other.berat and self.tinggi == other.tinggi
        return False
