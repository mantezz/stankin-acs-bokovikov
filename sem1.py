def check_cow_status(signal: float | int) -> str:
    '''Вычисляет температуру и определяет состояние датчика и коровы'''
    if type(signal) not in (int, float) or type(signal) == bool:
        raise TypeError("Неверный тип сигнала")
    if signal < 0:
        raise ValueError("Ошибка: сигнал не может быть отрицательным")
    if signal == 0:
        return "Получен сигнал 0 мА, датчик отключен"
    if signal < 4 or signal > 20:
        return f"Получен сигнал {signal} мА, датчик неисправен"

    '''Перевод сигнала 4–20 мА в температуру 0–75 градусов'''
    min_t = 0
    max_t = 75
    temperature = ((signal - 4) * (max_t - min_t) / (20 - 4) + min_t)
    temperature = round(temperature, 1)

    if 37.5 <= temperature <= 39:
        status = "с коровой все хорошо"
    elif 35 <= temperature < 37.5:
        status = "корова замерзла, требуется обогрев"
    elif 39 < temperature <= 39.5:
        status = "корова перегрелась, требуется охлаждение"
    elif temperature < 35:
        status = ("требуется внимание: датчик свалился или корова плохо себя чувствует")
    else:
        status = "срочно вызовите ветеринара, корова заболела"

    return (f"Получен сигнал датчика {signal} мА, датчик исправен, температура {temperature} градусов, {status}")

try:
    input_signal = float(input("Введите значение сигнала датчика в мА: "))
    result = check_cow_status(input_signal)
    print(result)
except (ValueError, TypeError):
    print("Ошибка: введены некорректные данные")