from datetime import datetime, timedelta

def calculate_return_date(days):
    """
    Функция, которая принимает на вход количество дней (например, 14) 
    и возвращает будущую дату, которая наступит через указанное количество дней 
    от текущего момента.
    
    Args:
        days (int): Количество дней от текущего момента
        
    Returns:
        datetime: Будущая дата
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date
