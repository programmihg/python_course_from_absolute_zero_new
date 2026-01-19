import os
import platform

def add_system_flashcards(filename):
    # 1. Пътища
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    docs_path = os.path.join(project_root, 'docs', 'intro', filename)

    # 2. Динамично извличане на данни (от предишния ви скрипт)
    # Използваме знанията от platform и os модулите
    system_info = [
        ("Каква е моята ОС?", platform.system()),
        ("Име на хоста (Hostname):", platform.node()),
        ("Текуща работна директория:", os.getcwd()),
        ("Процесорна архитектура:", platform.machine())
    ]

    # 3. Подготовка на HTML съдържанието
    content = ""
    # Проверяваме дали файлът е нов, за да добавим заглавие
    if not os.path.isfile(docs_path):
        content += f"# Автоматичен системен преговор\n\nГенерирано на база текущата система.\n\n---\n"

    for q, a in system_info:
        content += (
            f'<div class="flashcard-container">\n'
            f'<div class="flashcard">\n'
            f'<div class="flashcard-front">{q}</div>\n'
            f'<div class="flashcard-back">{a}</div>\n'
            f'</div>\n'
            f'</div>\n\n'
        )

    # 4. Записване (Append режим)
    try:
        os.makedirs(os.path.dirname(docs_path), exist_ok=True)
        with open(docs_path, 'a', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Успешно добавени системни данни в: {docs_path}")
    except Exception as e:
        print(f"❌ Грешка при запис: {e}")

if __name__ == "__main__":
    # Изпълняваме функцията
    add_system_flashcards('terminal_review.md')