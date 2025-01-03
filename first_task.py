from datetime import datetime

def get_days_from_today(date)-> int:
    #Дана функція рахує кількість днів між задоною датою та поточною
    #Тестуємо правильність вводу, в разі не правильного вводу результат None
    try:
        #Перетворюємо date з string в datetime 
        set_date = datetime.strptime(date,"%Y.%m.%d").date()
        #Оримуємо дату сьогодні
        today = datetime.today().date()
        #Повертаємо результат
        return (today - set_date).days
    except ValueError:
        print('Error неправильний формат дати. Введіть у форматі: "YYYY-MM-DD"!')
        return None

#Тест   
print(get_days_from_today("2025.01.01"))    
