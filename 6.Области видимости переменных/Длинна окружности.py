def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))


def circle_length(radius):
    return 2 * float(radius) * 3.14159


def circle_area(radius):
    return 3.14159 * (float(radius) ** 2)

