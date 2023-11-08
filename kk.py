cook_book = {}

with open('recipes.txt', 'r', encoding='UTF8') as f:
    dishes = f.readlines()
    numbers = 0
    recipes_name = str()

    for l in dishes:
        if numbers == 0:
            recipes_name = l.strip()
            cook_book[l.strip()] = []
            numbers += 1
            continue
        if l == '\n':
            numbers = 0
        if numbers == 1:
            numbers += 1
            continue
        if numbers > 1:
            ingredient_list = l.split(' | ')
            ingredient_dict = {}
            ingredient_dict['ingredient_name'] = ingredient_list[0].strip()
            ingredient_dict['quantity'] = ingredient_list[1].strip()
            ingredient_dict['measure'] = ingredient_list[2].strip()
            cook_book[recipes_name].append(ingredient_dict)

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}


    for dish_name in dishes:
        if dish_name in cook_book.keys():
            ingredients = cook_book[dish_name]


            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                shopping_list[ingredient_name] = {}
                shopping_list[ingredient_name]['measure'] = measure
                shopping_list[ingredient_name]['quantity'] = int(quantity * person_count)


    return shopping_list


shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shopping_list)




def sort_file():
    import os

    dir_path = '/Users/mac/PycharmProjects/files/newfiles'
    file_names = os.listdir(dir_path)

    line_counts = []

    for file_name in file_names:
        with open(os.path.join(dir_path, file_name), 'r', encoding='UTF-8') as file:
            line = file.readlines()
            file_info = (len(line), file_name)
            line_counts.append(file_info)

    line_counts.sort()
    # print(line_counts)


    with open('result.txt', 'w', encoding='UTF-8') as res_file:
        for file_info in line_counts:
            line_counts, file_name = file_info
            res_file.write(f'{file_name}\n{line_counts}\n')

            with open(os.path.join(dir_path, file_name)) as s_file:
                content = s_file.read()
                res_file.write(content)


sort_file()

with open('result.txt', 'r', encoding='UTF-8') as res_file:
    content = res_file.read()
    print(content)







