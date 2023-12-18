# 2. Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте.
#    Список имен передается в кач-ве аргумента.
#    Например:
#    []                                -->  "no one likes this"
#    ["Peter"]                         -->  "Peter likes this"
#    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"2
list1 = []
list2 = ["Peter"]
list3 = ["Jacob", "Alex"]
list4 = ["Max", "John", "Mark"]
list5 = ["Alex", "Jacob", "Mark", "Max"]

name_list = list5
if len(name_list) == 0:
    print("no one likes this")
elif len(name_list) == 1:
    print(f"{name_list[0]} likes this")
elif len(name_list) == 2:
    print(f"{name_list[0]} and {name_list[1]} likes this")
elif len(name_list) == 3:
    print(f"{name_list[0]}, {name_list[1]} and {name_list[2]} likes this")
elif len(name_list) > 3:
    print(f"{name_list[0]}, {name_list[1]} and {len(name_list) - 2} others likes this")