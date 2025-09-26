from datetime import datetime

def calculate_age(birth_date_str):
    """
    Функция, которая принимает на вход строку с датой рождения в формате "ГГГГ-ММ-ДД" 
    и вычисляет, сколько полных лет исполнилось человеку на сегодняшний день.
    
    Args:
        birth_date_str (str): Дата рождения в формате "ГГГГ-ММ-ДД"
        
    Returns:
        int: Количество полных лет
    """
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    today = datetime.now()
    
    # Вычисляем возраст
    age = today.year - birth_date.year
    
    # Проверяем, был ли день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age
