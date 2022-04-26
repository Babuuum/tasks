import task_1
cook_book_2 = {}


def get_shop_list_by_dishes(dishes, person_count):
    for ingredient in dishes:
        for list in task_1.cook_book[ingredient]:
            crutch = {}
            crutch['measure'] = list ['measure']
            crutch['quantity'] = int(list['quantity'])*person_count
            cook_book_2[list['ingredient_name']] = crutch


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print(cook_book_2)

