"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для
реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и 
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода 
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов 
проекта, проверить на практике работу декоратора @property.
 """


class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())

"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе 
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы 
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), 
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться 
округление значения до целого числа. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно 
равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только 
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение. 
Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух 
клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление 
количества ячеек этих двух клеток. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и 
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида 
*****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не 
хватает, то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество 
ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 
15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****. 

"""


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)
