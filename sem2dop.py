import re

def analyze_log(filename):
    warning_records = []
    ip_records = []

    log_regex = re.compile(r"\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+([A-Z]+)\s+(.+)")

    ip_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

    with open(filename, "r", encoding="utf-8") as log_file:
        for line in log_file:
            record = log_regex.fullmatch(line.strip())

            '''Если строка не соответствует шаблону'''
            if record is None:
                continue

            time, level, message = record.groups()
            result = f"{time} {level} {message}"

            if re.fullmatch(r"ERROR|WARN|WARNING", level):
                warning_records.append(result)

            if ip_regex.search(message):
                ip_records.append(result)

    return warning_records, ip_records


def print_records(title, records):
    print(title)

    if records:
        print("\n".join(records))
    else:
        print("Подходящих записей нет.")
    print()


try:
    warnings, ip_addresses = analyze_log("log.txt")
except FileNotFoundError:
    print("Файл log.txt не найден.")
except UnicodeError:
    print("Сохраните файл log.txt в кодировке UTF-8.")
else:
    print_records("Errors and Warnings::", warnings)
    print_records("Lines with IP addresses:", ip_addresses)