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

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = cook_book_read(file)
print(cook_book)