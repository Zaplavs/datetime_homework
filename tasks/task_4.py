from datetime import datetime

def validate_date_format(date_str):
    """
    Функция, которая принимает на вход строку и проверяет, 
    является ли она корректной датой в формате "ДД/ММ/ГГГГ". 
    Функция должна вернуть True, если формат верный и дата существует 
    (например, не "32/13/2025"), и False в противном случае.
    
    Args:
        date_str (str): Строка с датой в формате "ДД/ММ/ГГГГ"
        
    Returns:
        bool: True, если дата корректна, иначе False
    """
    # Проверяем формат строки с помощью регулярного выражения
    import re
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(pattern, date_str):
        return False
    
    try:
        # Проверяем формат даты
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        # Если формат неправильный или дата несуществующая (например, 32/13/2025)
        return False
