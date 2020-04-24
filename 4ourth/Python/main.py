from math import log10


class Handler:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.__result = None

    def calculate(self):
        # [lg(4b-c)a]/[b+c/d-1]
        print("Початок обчислення")
        print(f'[lg(4*{self.b}-{self.c})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        first = 4 * self.b
        print(f'[lg({first}-{self.c})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        second = first - self.c
        print(f'[lg({second})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        try:
            third = log10(second)
            print(f'[{third})*{self.a}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        except ValueError:
            raise ValueError(f"Базою логарифму не може бути {second}")
        fourth = third * self.a
        print(f'[{fourth}]/[{self.b}+{self.c}/{self.d}-1] = ', end='')
        try:
            fifth = self.c/self.d
            print(f'[{fourth}]/[{self.b}+{fifth}-1] = ', end='')
        except ZeroDivisionError:
            raise ZeroDivisionError("d не може дорівнювати 0")
        sixth = self.b + fifth
        print(f'[{fourth}]/[{sixth}-1] = ', end='')
        seventh = sixth - 1
        print(f'{fourth}/{seventh} = ', end='')
        try:
            self.__result = fourth / seventh
            print(f'{self.__result}')

        except ZeroDivisionError:
            raise ZeroDivisionError("b+c/d-1 не може дорівнювати 0")

    def result(self):
        if self.__result is None:
            raise NotImplementedError("Значення ще не обчислене")
        else:
            return self.__result

    def logging_implement(self, rewrite=False):
        if rewrite:
            right = 'w+'
        else:
            right = 'a+'
        with open('python.log.txt', right) as log:
            try:
                self.calculate()
            except ZeroDivisionError:
                log.write('e0')
            except ValueError:
                log.write('eL')
            except:
                log.write('e?')
            try:
                log.write(str(self.result()) + '\r\n')
            except NotImplementedError:
                log.write('eI\r\n')
