def main():
    # Запрашиваем у пользователя слово
    word = input("Введите слово из маленьких латинских букв: ")

    # Определяем гласные и согласные буквы
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}  # Словарь для подсчета гласных
    consonant_count = 0

    # Подсчитываем гласные и согласные буквы
    for letter in word:
        if letter in vowels:
            vowel_count[letter] += 1
        elif letter.isalpha():  # Проверяем, что это буква
            consonant_count += 1

    # Проверяем, есть ли все гласные
    if any(count == 0 for count in vowel_count.values()):
        print(False)
    else:
        # Выводим результаты
        print(f"Количество гласных: {sum(vowel_count.values())}")
        print(f"Количество согласных: {consonant_count}")
        print("Количество каждой гласной буквы:", vowel_count)

if __name__ == "__main__":
    main()
