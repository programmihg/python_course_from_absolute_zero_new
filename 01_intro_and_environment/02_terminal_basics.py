"""!
Работа с терминала (CMD, PowerShell, Bash, Zsh), основни команди като ls, cd, pwd, ping и 
променливи на средата (PATH)
!"""
import os  # Внасяме модула 'os' за взаимодействие с операционната система
import platform  # Внасяме 'platform', за да разберем детайли за хардуера и софтуера


def show_system_info():  # Дефинираме функция за показване на системна информация
    print("--- Информация за текущата система ---")  # Извеждаме заглавие

          # platform.system() връща 'Linux', 'Windows' или 'Darwin' (Mac)
    print(f"Операционна система: {platform.system()}")

    # platform.node() връща името на компютъра в мрежата (hostname)
    print(f"Име на хоста (Hostname): {platform.node()}")

    # os.getcwd() връща 'Current Working Directory' (папката, в която е проекта)
    print(f"Текуща работна директория: {os.getcwd()}")


def main():  # Главна функция
    show_system_info()  # Извикваме горната функция

    print("\n--- Списък с файлове в тази папка: ---")
    # os.listdir('.') изпълнява команда, подобна на 'ls' в терминала на Linux
    files = os.listdir('..')
    for file in files:  # Преминаваме през всеки намерен файл
        print(f" Намерен файл: {file}")  # Извеждаме името му

    # Преместете генерирането тук, за да е последното нещо в терминала
    # Вашите нови знания от видеото
    term_commands = [
        ("ls / dir", "Показва съдържанието на папката"),
        ("mkdir", "Създава нова папка"),
        ("PATH", "Списък с папки, в които ОС търси програми")
    ]

    print("\n--- Генериран HTML за вашия Markdown сайт ---")
    for cmd, desc in term_commands:
        # Генерираме HTML без интервали в началото
        html = f'<div class="flashcard-container">\n' \
               f'<div class="flashcard">\n' \
               f'<div class="flashcard-front">{cmd}</div>\n' \
               f'<div class="flashcard-back">{desc}</div>\n' \
               f'</div>\n' \
               f'</div>'
        print(html)


# Проверяваме дали стартираме файла директно
if __name__ == "__main__":
    main()  # Ако е директно, стартираме основната логика