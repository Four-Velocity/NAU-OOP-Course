class String:
    def __init__(self, value):
        self.value = value

    def len(self):
        return len(self.value)

    def all_upper(self):
        self.value = self.value.upper()

    def compare(self, string):
        if string == self.value:
            return 1
        else:
            return 0

    def get(self):
        return self.value


class Text:
    def __init__(self, string=None):
        if string is None:
            self.text = []
        else:
            self.text = [string]

    def show(self):
        if len(self.text) > 0:
            print('\n'.join(list(map(lambda x: x.get(), self.text))))

    def add(self, string: String):
        self.text.append(string)

    def delete_one(self, index=None):
        if index is None:
            self.text.pop(-1)
        else:
            self.text.pop(index)

    def delete_all(self):
        self.text = []

    # That delete_len smells like bad code :|
    def delete_len(self, length):
        result = []
        for i in range(len(self.text)):
            if self.text[i].len() == length:
                result.append(i)
        for i in range(len(result)):
            self.text.pop(result[i]-i)

    def upper(self):
        for string in self.text:
            string.all_upper()

    def search(self, value):
        result = 0
        for string in self.text:
            result += string.compare(value)
        return result
if __name__ == '__main__':
    s1 = String("Foo Bar")
    s2 = String("Spam Eggs")
    s3 = String("Pupa Lupa")

    del_all = Text()
    del_one = Text()
    del_len = Text()
    other = Text()

    del_all.add(s1)
    del_all.add(s2)
    del_all.add(s3)

    del_one.add(s1)
    del_one.add(s2)
    del_one.add(s3)

    del_len.add(s1)
    del_len.add(s2)
    del_len.add(s3)

    other.add(s1)
    other.add(s2)
    other.add(s3)
    other.add(s2)

    print("Повне видалення")
    del_all.delete_all()
    del_all.show()

    print("Видалення одного елементу за індексом та без")
    del_one.delete_one()
    del_one.delete_one(0)
    del_one.show()

    print("Видалення усіх елементів з довжиною 9")
    del_len.delete_len(9)
    del_len.show()

    print("Пошук та приведення до верхнього регістру ")
    print(f"{other.search('Spam Eggs')} 'Spam Eggs' знайдено у тексті")
    other.upper()
    other.show()