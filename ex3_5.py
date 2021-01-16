def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


class Frac(object):
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def simplify(self):
        x = compute_hcf(self.numerator, self.denominator)
        self.numerator = self.numerator / x
        self.denominator = self.denominator / x
        return self

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def minus(self, another_frac):
        return self.__sub__(another_frac)

    def divide(self, another_frac):
        return self.__truediv__(another_frac)

    def __str__(self):
        return "%i/%i" % (self.numerator, self.denominator)

    def __sub__(self, other):
        if isinstance(other, Frac):
            if self.denominator == other.denominator:
                return Frac(self.numerator - other.numerator,
                            self.denominator).simplify()
            else:
                return Frac(self.numerator * other.denominator -
                            other.numerator * self.denominator,
                            self.denominator * other.denominator).simplify()
        else:
            raise ValueError("Frac type required.")

    def __truediv__(self, other):
        if isinstance(other, Frac):
            return Frac(self.numerator * other.denominator,
                        self.denominator * other.numerator).simplify()
        else:
            raise ValueError("Frac type required.")


def get_value_from_input():
    return input()


def handle():
    input_value = get_value_from_input()
    input_value = input_value.split("\n")
    pre_frac = None
    for i in range(0, int(len(input_value) / 2)):
        new_frac = Frac(input_value[i * 2], input_value[i * 2 + 1])
        if pre_frac is None:
            pre_frac = new_frac
        else:
            if i % 2 == 0:
                pre_frac = pre_frac.divide(new_frac)
            else:
                pre_frac = pre_frac.minus(new_frac)
    return str(pre_frac)
