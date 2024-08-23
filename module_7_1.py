from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self) -> None:
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products: Product) -> None:
        for i in products:
            push = False
            with open('products.txt') as file:
                content = file.read()
                if str(i) in content:
                    print(f'Продукт {i.name} уже есть в магазине')
                    push = True
                else:
                    file = open('products.txt', 'a')
                    file.write(f'{str(i)}\n')
                    push = False
                    print(i)

        for i in products:
            if push:
                print(i)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
