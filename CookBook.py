from pprint import pprint


def create_book(book_name):
    with open('cook.txt', encoding='UTF-8') as fi:
        cook_dict = {}
        for line in fi:
            dish_name = line.strip()
            cook_dict[dish_name] = []
            counter = int(fi.readline().strip())
            for i in range(counter):
                ingredients = fi.readline().strip().split('|')
                temp_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                cook_dict[dish_name].append(temp_dict)
            fi.readline()
        return cook_dict


def get_shop_list_by_dishes(dishes, persons):
    cook_dict = create_book('cook.txt')
    shoplist = {}
    for dish_name in dishes:
        if dish_name in cook_dict:
            for ingredients in cook_dict[dish_name]:
                if ingredients['ingredient_name'] in shoplist:
                    shoplist[ingredients['ingredient_name']]['quantity'] += int((ingredients['quantity']) * persons)
                else:
                    shoplist[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                'quantity': int(ingredients['quantity']) * persons}
    return shoplist
