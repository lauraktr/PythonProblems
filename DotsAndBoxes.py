def complete_box():
    print("counting completed boxes ...")

if __name__ == '__main__':
    print("Dots and Boxes")

    array_1 = [["_", "_", "_"],
               ["|", "|", " ", "|"],
               ["_", " ", " "],
               ["|", " ", " ", " "],
               [" ", " ", " "]]

    array_2 = [["_", "_", "_"],
               ["|", "|", "|", "|"],
               ["_", "_", "_"],
               ["|", "|", " ", " "],
               ["_", " ", " "]]

    complete_box(array_1)


