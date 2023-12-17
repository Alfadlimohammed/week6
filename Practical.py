import math
squares = (1, 4, 9, 12)
for number in squares:
    squares_root = math.sqrt(number)
    print(f"the square root of {number} is ...{squares_root}")
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36]
    next_squares = [49, 64, 81]
    squares.append(next_squares[0])
    squares.append(next_squares[1])
    for square in next_squares:
        squares.append(square)
    print("Updated squares list:", squares)
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    next_squares = [121, 144, 169]
    squares.extend(next_squares)
    print("Updated squares list:", squares)
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    squares.insert(0, 2)

    print("Updated squares list:", squares)
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    squares.remove(49)
    print("Updated squares list:", squares)
if __name__ == '__main__':
    mylist = [1, 2, 3, 1, 2]
    mylist.remove(2)
    print("Updated squares list:", mylist)
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    last_value = squares.pop()
    print("Removed value:", last_value)

    print("the list squares:", squares)
if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    first_value = squares.pop(0)
    print("Removed value:", first_value)

    print("the list squares:", squares)
if __name__ == '__main__':
    names = ["Eric", "anna", "Sophie", "sam"]
    names.sort()
    print(names)
if __name__ == '__main__':
    squares = [0, 20, 65, 12]
    list = squares.reverse()

    print("show the list please", squares)
if __name__ == '__main__':
    squares = [0, 20, 65, 12]
    squares[:] = squares[::-1]
    print("show the list please", squares)
if __name__ == '__main__':
    colour = ["red", "green", "yellow", "blue", "red"]
    print(colour.index("blue"))
if __name__ == '__main__':
    colours = ["red", "green", "yellow", "blue", "red"]
    new_colours = colours.copy()
    colours.append("black")
    colours[1] = "orange"
    print("Original colours list:", colours)
    print("Copied colours list:", new_colours)
if __name__ == '__main__':
    cubes = [x * x * x for x in range(2, 20)]
    print("Cubes list:", cubes)
if __name__ == '__main__':
    house_number = 9
    street = "Main Street"
    postcode = "ls1 2ls"
    address = (house_number, street, postcode)
    print("Address:", address)
if __name__ == '__main__':
    address = (9, 'Main Street', 'ls1 2ls')
    house_num, street, postcode = address
    print("House Number:", house_num)
    print("Street:", street)
    print("Postcode:", postcode)
if __name__ == '__main__':
    address = (9, 'Main Street', 'ls1 2ls')
    print("Unpacked Address:", *address)
    print("Original Address:", address)