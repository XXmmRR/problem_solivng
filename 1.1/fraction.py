import math


class Fraction:

    def __init__(self, top, bottom):
        k = math.gcd(top, bottom)
        self.num = top // k
        self.den = bottom // k

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        if isinstance(otherfraction, Fraction):
            common_denominator = math.lcm(self.den, otherfraction.den)
            numerator = self.num * (common_denominator // self.den) + otherfraction.num * (common_denominator // otherfraction.den)

            # Упрощение результата
            common_gcd = math.gcd(numerator, common_denominator)
            newnum, newden = numerator // common_gcd, common_denominator // common_gcd
            return Fraction(newnum, newden)
        elif isinstance(otherfraction, int):
            # Логика сложения дроби и целого числа
            new_numerator = self.num + otherfraction * self.den
            return Fraction(new_numerator, self.den)
        return NotImplemented  # Если сложение не поддерживается

    def __iadd__(self, otherfraction):
        if isinstance(otherfraction, Fraction):
            common_denominator = math.lcm(self.den, otherfraction.den)
            numerator = self.num * (common_denominator // self.den) + otherfraction.num * (common_denominator // otherfraction.den)

            # Упрощение результата
            common_gcd = math.gcd(numerator, common_denominator)
            newnum, newden = numerator // common_gcd, common_denominator // common_gcd
            self.num = newnum
            self.den = newden
            return self
        elif isinstance(otherfraction, int):
            # Логика сложения дроби и целого числа
            new_numerator = self.num + otherfraction * self.den
            self.num = new_numerator
            return self
        return NotImplemented  # Если сложение не поддерживается

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, otherfraction):
        numerator = self.num * otherfraction.num
        denominator = self.den * otherfraction.den
        # Упрощение результата
        common_gcd = math.gcd(numerator, denominator)
        newnum, newden = numerator // common_gcd, denominator // common_gcd
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        numerator = self.num * otherfraction.den
        denominator = self.den * otherfraction.num
        # Упрощение результата
        common_gcd = math.gcd(numerator, denominator)
        newnum, newden = numerator // common_gcd, denominator // common_gcd
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        common_denominator = math.lcm(self.den, otherfraction.den)
        numerator = self.num * (common_denominator // self.den) - otherfraction.num * (common_denominator // otherfraction.den)

        # Упрощение результата
        common_gcd = math.gcd(numerator, common_denominator)
        newnum, newden = numerator // common_gcd, common_denominator // common_gcd
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return  firstnum != secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __repr__(self):
        return f'Fraction ({self.den}/{self.num}'

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den
