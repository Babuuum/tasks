cook_book = {}

def get_data(file_name):
    with open (file_name, mode="r", encoding="utf-8") as file:
        for line in file:
            cook_book[line.rstrip("\n")] = []
            quantity = int(file.readline().strip())
            for ingredient in range(quantity):
                crutch_2 = file.readline().rstrip("\n").split("|")
                crutch = {}
                crutch['ingredient_name'] = crutch_2[0]
                crutch['quantity'] = crutch_2[1]
                crutch['measure'] = crutch_2[2]
                cook_book[line.rstrip("\n")].append(crutch)
            file.readline()



get_data("recipes.txt")

