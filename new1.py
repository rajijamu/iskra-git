import math


def main(x, z, y):
    a = math.sqrt((54 * y - 46 * x ** 3 - z ** 2) ** 4)
    b = (y ** 3 - x - 29) ** 7 - 36 * (math.sqrt(25 * z ** 2)) ** 4
    c = 78 * math.sin((81 * y ** 3 - 80 * z)) ** 3 + (37 * x + 53 * z ** 3) ** 7
    d = math.sqrt(b / c)
    result = a + d
    return result
    
    a = 58 - math.cos(77 * x - 1 - y ** 3) ** 7
    


print("{:.2e}".format(main(-0.48, -0.08, 0.99)))

