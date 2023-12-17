prices = [2.65, 7.65, 8.25, 9.56, 12.34, 15.67, 18.9]
for price in prices:
    print(price)
if __name__ == '__main__':
    temps = [32, 46, 95, 10, 50]
    list = temps.index(95)
    print(list)
if __name__ == '__main__':
    temps = [32, 46, 95, 10, 50]
    list = temps.count(10)
    print(list)
if __name__ == '__main__':
    values = [x * x for x in range(100, 200)]
    print(values)
if __name__ == '__main__':
    values = [x * x for x in range(100, 200) if x % 2 == 0]
    print(values)
if __name__ == '__main__':
    x, y, z = (100, 200, 150)
    print("x", x)
    print("y", y)
    print("z", z)
if __name__ == '__main__':
    coord = (100, 200, 150)
    height = coord[1]
    print("height", height)
if __name__ == '__main__':
    coord = (100, 200, 150)
    for value in coord:
        print(value)