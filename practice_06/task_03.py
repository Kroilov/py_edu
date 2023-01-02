# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты
# имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого
# набора объектов, функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

# Пример:
# same_by(lambda x: x % 2, [2,4,6,8])

# Ответ: True

def same_by(characteristic, objects):
    if not objects:
        return True

    for i in objects:
        if characteristic(i) != characteristic(objects[0]):
            return False

    return True


print(same_by(lambda x: x % 2, [2, 4, 6, 8]))  # True
print(same_by(lambda x: x, [2, 2, 2]))  # True
print(same_by(lambda x: x, []))  # True