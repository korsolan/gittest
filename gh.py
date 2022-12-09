# 1)Создать отдельный файл и поместить в него набор функций, которые возвращают разную информацию о
# температуре.
# 1 функция - принимает список из температур, принимает два числа - диапазон, возвращает количество
# элементов в этом диапазоне
# 2 функция - принимает список из температур и возвращает список без дубликатов
# 3 функция принимает список из температур и возвращает среднюю
def get_count_in_range(list, num_1, num_2):
    count = 0
    for i in range(len(list)):
        if num_1 <= list[i] <= num_2:
            count += 1
            return count
def unique_temp(list_temp):
    new_list_temp = list(set(list_temp))
    return new_list_temp
def avr_temp(list):
    avr = sum(list) / len(list)
    return avr
