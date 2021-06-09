from utils import is_digit

if __name__ == '__main__':
    edges = list()

    while len(edges) < 3:
        edge = input(f"Введите длину стороны {len(edges) + 1}:\n")
        if not is_digit(edge):
            print("Нужно ввести число: целое или с дробной частью.")
        elif float(edge) <= 0:
            print("Нужно ввести сторону с длиной больше 0.")
        else:
            edges.append(float(edge))

    edges = sorted(edges)

    if edges[2] >= (edges[0] + edges[1]):
        print("Невозможно составить треугольник из приведённых сторон.")
    else:
        print("Из приведённых сторон можно составить треугольник: ")
        first_pair = edges[0] == edges[1]
        second_pair = edges[1] == edges[2]

        if first_pair and second_pair:
            print("равносторонний треугольник!")
        elif first_pair or second_pair:
            print("равнобедренный треугольник!")
        else:
            print("разносторонний треугольник!")
