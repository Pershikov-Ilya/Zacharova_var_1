import numpy as np

def f_1(x):
    return (x**(2/3))+1

def f_1_1(x):
    return -((x**(2/3))+1)

def f_2(x):
    return x**(2/3) - np.sqrt(1-x**2) + 1

def f_2_2(x):
    return -(x**(2/3) - np.sqrt(1-x**2) + 1)

# функция для вычисления интегралов
def simpson(f, a, b, k):
    h = (b - a) / k
    x = [a + i * h for i in range(k + 1)]
    fx = [f(xi) for xi in x]
    s = fx[0] + fx[-1] + 4 * np.sum(fx[1:-1:2]) + 2 * np.sum(fx[2:-1:2])
    return s * h / 3


# Функция для проверки(находится ли точка внутри фигуры)
def is_real_number(num):
    return isinstance(num, (int, float))

def point_inside_shape(x, y, f1, f2, f2_2, f1_1):
    f1_result = f1(x)
    f2_result = f2(x)
    f2_2_result = f2_2(x)
    f1_1_result = f1_1(x)

    if all(map(is_real_number, [f1_result, f2_result, f2_2_result, f1_1_result])):
        if ((y <= f1_result) and (y >= f2_result)) or ((y <= f2_2_result) and (y >= f1_1_result)):
            return True
    return False

def point_inside_shape_1(x, y):
    return point_inside_shape(x, y, f_1, f_2, f_2_2, f_1_1)

def point_inside_shape_2(x, y):
    return point_inside_shape(-x, y, f_1, f_2, f_2_2, f_1_1)
# Определение пределов интегрирования
a, b, c, d = -1, 1, -2, 2

# Функция для подсчета количества точек внутри фигуры
def count_point_1(N_points, point_inside_shape_1):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(c, d)
        if point_inside_shape_1(x, y): count += 1
    return count

def count_point_2(N_points, point_inside_shape_2):
    count = 0
    for _ in range(N_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(c, d)
        if point_inside_shape_2(x, y): count += 1
    return count

def main():
    # (k) - количество подоотрезков для аппроксимации в функции simpson
    k = 10000
    # (pl) - площадь области, в которой находится наша фигура
    pl = 8

    # фактическая площадь фигуры
    square_of_our_figure = (simpson(f_1, -1, 1, k) - simpson(f_2, -1, 1, k)) * 2
    print("Our square:", square_of_our_figure)

    N_points = 10
    while N_points <= 1000000:
        points = count_point_1(N_points, point_inside_shape_1) + count_point_2(N_points, point_inside_shape_2)
        Square = pl * points / N_points
        print(f"N = {N_points}")
        print(f"ПЛОЩАДЬ = {Square}")
        print(f"ПОГРЕШНОСТЬ = {abs(Square - square_of_our_figure) / square_of_our_figure}\n")
        N_points *= 10

if __name__ == "__main__":
    main()