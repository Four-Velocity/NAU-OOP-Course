from math import log10
from itertools import count


from math import log10


class Handler:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.__result = None

    def calculate(self, debug=False):
        # [lg(4b-c)a]/[b+c/d-1]
        if debug:
            print("\nПочаток обчислення")
        if debug:
            print(f'[lg(4*{self.b}-{self.c})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        first = 4 * self.b
        if debug:
            print(f'[lg({first}-{self.c})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        second = first - self.c
        if debug:
            print(f'[lg({second})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        try:
            third = log10(second)
            if debug:
                print(f'[{third})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        except ValueError:
            raise ValueError(f"Базою логарифму не може бути {second}")
        fourth = third * self.a
        if debug:
            print(f'[{fourth}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        try:
            fifth = self.c/self.d
            if debug:
                print(f'[{fourth}]/[{self.b}+{fifth}-1] = ', end='')
        except ZeroDivisionError:
            raise ZeroDivisionError("d не може дорівнювати 0")
        sixth = self.b + fifth
        if debug:
            print(f'[{fourth}]/[{sixth}-1] = ', end='')
        seventh = sixth - 1
        if debug:
            print(f'{fourth}/{seventh} = ', end='')
        try:
            self.__result = fourth / seventh
            if debug:
                print(f'{self.__result}')
        except ZeroDivisionError:
            raise ZeroDivisionError("b+c/d-1 не може дорівнювати 0")
        return first, second, third, fourth, fifth, sixth, seventh

    def getResult(self):
        if self.__result is None:
            raise NotImplementedError("Значення ще не обчислене")
        else:
            return self.__result

    def logger(self):
        with open('logs/python.log.csv', "a+") as log:
            calc = ();
            try:
                calc = self.calculate()
            except ZeroDivisionError:
                log.write('e0')
            except ValueError:
                log.write('eL')
            except:
                log.write('e?')
            try:
                log.write(f'{self.getResult()}, {", ".join(str(i) for i in calc)}\r\n')
            except NotImplementedError:
                log.write('eI\r\n')


if __name__ == '__main__':
    with open("start_values.tsv", "r") as values:
        values = values.readlines()
        values = list(map(lambda x: x.split('\t'), values))

    from itertools import count

    with open("logs/python.log.csv", "w+") as log:
        log.write('Result,First,Second,Third,Fourth,Fifth,Sixth,Seventh\r\n')
    for data, iteration in zip(values, count()):
        handler = Handler(
            float(data[0]),
            float(data[1]),
            float(data[2]),
            float(data[3]),
        )
        handler.logger()
