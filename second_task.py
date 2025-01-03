import random

def get_numbers_ticket(min,max,quantity) -> int:
    #Дана функція генерує набір унікальних випадкових чисел
    lottery_numbers = set()
    quantity= int(quantity)
    #Перевіряемо введені данні на тип та визначений діапазон
    try:
        if (1<= min <= max <=1000) and (0 < quantity <= (max-min+1)):
            # Парамтери функції знаходяться в заданих 
            while len(lottery_numbers) < quantity:
                lottery_numbers.add(random.randint(min, max))
        else: 
            print("Ви ввели не правильні числа. Повинно бути від 1 до 1000 та кількість в цьому діапазоні")
            return None
    except TypeError or ValueError:
        print("Введені не правильні аргументи")
        return None
        # Повернення відсортованого списку
    return sorted(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)