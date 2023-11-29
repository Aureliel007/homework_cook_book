def cook_book_read(file):    
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        cook_book[recipe_name] = []
        for i in range(int(file.readline())):
            ingr = file.readline()
            name, q, m = ingr.strip().split(' | ')
            cook_book[recipe_name].append({'ingredient_name': name, 'quantity': int(q), 'measure': m})
        file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr_name = ingr['ingredient_name']
            if ingr_name in ingr_list:
                ingr_list[ingr_name]['quantity'] += ingr['quantity'] * person_count
            else:
                ingr_list[ingr_name] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
    return ingr_list

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = cook_book_read(file)
    all_ingredients = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print(all_ingredients)