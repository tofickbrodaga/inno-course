def calculate_rectangle_area(width, height):
    try:
        area = width * height
        return area
    except TypeError:
        raise TypeError("Ошибка: неверный тип данных для вычисления площади")

def calculate_rectangle_perimeter(width, height):
    try:
        perimeter = 2 * (width + height)
        return perimeter
    except TypeError:
        raise TypeError("Ошибка: неверный тип данных для вычисления периметра")

try:
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    area = calculate_rectangle_area(width, height)
    perimeter = calculate_rectangle_perimeter(width, height)
    if area and perimeter:
        print(f"Площадь прямоугольника: {area}")
        print(f"Периметр прямоугольника: {perimeter}")
except ValueError:
    raise ValueError("Ошибка: введено неверное значение")