"""!
Инсталация на интерпретатор и настройка на IDE (Visual Studio Code или PyCharm)
!"""
import os  # Модул за работа с файловата система
import sys  # Модул за работа с параметрите на Python интерпретатора


def check_environment():  # Дефинираме функция за проверка на средата
    print("--- Проверка на настройките на средата (Setup & IDE) ---")

    # sys.prefix ни показва пътя до интерпретатора, който използваме в момента
    # Ако използвате виртуална среда, пътят ще завършва на '.venv'
    executable_path = sys.prefix
    print(f"Текущ интерпретатор (venv): {executable_path}")

    # Проверяваме дали сме във виртуална среда
    # hasattr проверява дали съществува определен системен атрибут
    is_venv = hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix)
    print(f"Активна ли е виртуалната среда? {'Да' if is_venv else 'Не'}")


def main():  # Главна функция
    check_environment()  # Извикваме проверката

    # Обяснение за PyCharm настройките чрез принт
    print("\nСъвет за PyCharm:")
    print("1. Използвайте Ctrl+Alt+S за настройки (Settings).")
    print("2. Проверете 'Project Interpreter', за да сте сигурни, че ползвате правилния Python.")


# Стандартната проверка дали файлът се изпълнява директно
if __name__ == "__main__":
    main()