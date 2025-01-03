import re

def normalize_phone(phone_number) -> str:
    #Дана функція перевіряє та приводить номера телефонів до міжнародного виду +380
    #Видалляэмо всі зайві символи крім чисел та знака +
    clean_phone = re.sub(r"[^\d+]","",phone_number)
    
    #перевірка на '+' '+38' '380'
    #Якщо починається з 0 то додаємо +38
    if clean_phone.startswith("0"):
        clean_phone = "+38" + clean_phone
    # Якшо починається з 380 то додаємо +
    elif clean_phone.startswith("380"):
        clean_phone = "+" + clean_phone
    #Окремий варіант коли починається з + але не з +38
    elif clean_phone.startswith("+") and (not clean_phone.startswith("+38")):
        clean_phone = re.sub(r"\+","+38", clean_phone)
    #Повертаємо результат роботи функції
    return clean_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     +0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "a3809595995",
]
raw_clean_numbers = [normalize_phone(num) for num in raw_numbers]
print(raw_clean_numbers)