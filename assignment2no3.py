class Person:
    def __init__(self, weight, height):
        self._weight = weight  # in kilograms
        self._height = height  # in meters

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def BMI_Value(self):
        if self._height <= 0:
            raise ValueError("Height must be positive.")
        return self._weight / (self._height ** 2)

if __name__ == "__main__":
    weight = float(input("Masukkan berat badan (kg): "))
    height = float(input("Masukkan tinggi badan (meter): "))

    person = Person(weight, height)
    print("BMI:", person.BMI_Value())