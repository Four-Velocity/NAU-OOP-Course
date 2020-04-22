class BaseString:
    def __init__(self, value):
        self.value = str(value)

    def len(self):
        return sum(1 for _ in self.value)


class SymbolString(BaseString):
    def replace(self, a, b):
        result = self.value
        for i in range(self.len()):
            if result[i] == a:
                a1 = result[:i]
                a2 = b
                a3 = result[i + 1:]
                result = a1 + a2 + a3
        return result


if __name__ == '__main__':
    baseS = BaseString('Foo Bar')
    symbolS = SymbolString('Spam Eggs')
    print(f'Довжина базового рядка: {baseS.len()}')
    print(f'Довжина символьного рядка: {symbolS.len()}')
    print("Замінемо 'g' на 'b' у символьному рядку")
    print(f"Результат: {symbolS.replace('g', 'b')}")
