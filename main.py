"""
Алгоритм: Представляем свободные поля как набор прямоугольников. Сначала размещаем П-полиомино, затем прямоугольные.
При размещении полиомино делят прямоугольник на набор меньших прямоугольников. Большой прямоугольник из массива удаляем,
меньшие вставляем. Место для полиомино пытаемся найти начиная с меньших по площади прямоугольников.
"""


def added_rect(poliomino, rect):
    """
    Функция пытается вставить полиомино в прямоугольник так, чтобы добиться максимальной площади одного из
    образованных внешних прямоугольников. Возвращает список внешних прямоугольников или сигнал о невозможности
    размещения.
    """
    long_rect = max(rect)
    short_rect = min(rect)
    long_p = max(poliomino)
    short_p = min(poliomino)

    if long_rect - long_p < 0 or short_rect - short_p < 0:
        return False
    if short_rect - long_p >= 0:
        ans = [[(short_rect - long_p, long_rect), (short_rect - long_p) * long_rect],
               [(long_p, (long_rect - short_p)), (long_rect - short_p) * long_p]]
    else:
        ans = [[(long_rect - long_p, short_rect), (long_rect - long_p) * short_rect],
               [(long_p, (short_rect - short_p)), (short_rect - short_p) * long_p]]
    return ans


def insert_poliominos(list_poliominos, list_rects, type_pol):  # основная функция
    list_r = list_rects  # определяем списки полиомино и прямоугольников
    list_p = list_poliominos
    flag = False
    while list_p:  # обрабатываем первый полиомино в списке
        rect_founded = False
        count_rect = 0
        while count_rect < len(list_r):  # пытаемся вставить полиомино в прямоугольники по возрастанию
            new_rect = added_rect(list_p[0][0], list_r[count_rect][0])
            if new_rect:  # при удаче обрабатываем список прямоугольников
                list_r.pop(count_rect)
                for i in new_rect:  # вставляем новые внешние прямоугольники в общий список
                    if i[1] > 0:
                        list_r.append(i)
                if type_pol == "P":
                    rect_insides = [  # для П-полиомино образовываем и вставляем в список внутренний прямоугольник
                        (list_p[0][0][0] - 1, list_p[0][0][1] - 2),
                        (list_p[0][0][0] - 1) * (list_p[0][0][1] - 2)]
                    if rect_insides[1] > 0:
                        list_r.append(rect_insides)

                list_r = sorted(list_r, reverse=False, key=lambda x: x[1])  # сортируем список доступных прямоугольников
                rect_founded = True
                break
            else:
                count_rect += 1

        if not rect_founded:
            flag = True
            break

        else:
            if list_p[0][1] == 1:
                list_p.pop(0)
            else:
                list_p[0][1] -= 1
    """
    Если все полиомино обработаны, возвращаем единицу, если нет - ноль. Возвращаем список оставшихся прямоугольников.
    """
    if flag:
        return [0, list_r]
    else:
        return [1, list_r]


n, m = 4, 3
list_rect_poliominos = [[(2, 2), 1]]
list_p_poliominos = [[(3, 4), 1]]

list_rects = [[(max(n, m), min(n, m)), n * m]]  # список доступных прямоугольников

flag, list_rects = insert_poliominos(list_p_poliominos, list_rects, type_pol='P')

if flag:
    flag, list_rects = insert_poliominos(list_rect_poliominos, list_rects, type_pol='R')

if not flag:
    print("False")
else:
    print("True")
