from datetime import datetime

def analyze_timestamps(start_time, end_time):
    """
    Функция, которая принимает две строки с временными метками:
    start_time = "2025-09-26 10:5:00" и end_time = "2025-09-26 11:07:30".
    Вычисляет разницу между ними и возвращает результат в виде строки: 
    "Операция заняла: 12 минут 30 секунд.".
    
    Args:
        start_time (str): Начальное время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
        end_time (str): Конечное время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
        
    Returns:
        str: Строка с разницей во времени
    """
    # Преобразуем строки в объекты datetime
    start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    
    # Вычисляем разницу
    diff = end_dt - start_dt
    
    # Получаем общее количество секунд
    total_seconds = int(diff.total_seconds())
    
    # Вычисляем минуты и секунды
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return f"Операция заняла: {minutes} минут {seconds} секунд."
