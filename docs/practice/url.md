# Url
-----

### 3\. Попълване на `docs/practice/url.md`

Този проект тренира "нарязването" (slicing) и методите на низовете.

````markdown
# Проект: URL Parser (Анализатор на адреси)

Целта е да разделим един уеб адрес на неговите компоненти (протокол, домейн, път).

### Примерна логика:
```python
url = "[https://mysite.com/blog](https://mysite.com/blog)"

# Извличане на протокол
protocol = url.split("://")[0]

# Извличане на домейн и път
full_address = url.split("://")[1]
domain = full_address.split("/")[0]
path = full_address.split("/")[1]

print(f"Протокол: {protocol}")
print(f"Домейн: {domain}")
print(f"Път: {path}")
```

🧠 Упражнение: URL Parser
<div class="flashcard-container"> <div class="flashcard"> <div class="flashcard-front">Кой метод на низовете е най-подходящ за разделяне на URL?</div> <div class="flashcard-back">Методът .split().</div> </div> </div>