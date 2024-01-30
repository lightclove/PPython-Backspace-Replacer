class BackspaceReplacer:
    def __init__(self):
        pass

    def replace_stars(self, input_str: str) -> str:
        try:
            if input_str is None:
                return ""

            if not isinstance(input_str, str):
                raise TypeError("Input must be a string")

            result = ""
            i = 0

            while i < len(input_str):
                if input_str[i] == '*':
                    i += 2  # Пропускаем звездочку и символ перед ней
                else:
                    result += input_str[i]
                    i += 1

            return result

        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

if __name__ == "__main__":
    backspace_replacer = BackspaceReplacer()

    # Запрос пользовательского ввода
    user_input = input("Введите строку с звездочками: ")

    # Вызов метода класса для обработки ввода
    result = backspace_replacer.replace_stars(user_input)

    # Вывод результата
    print("Результат обработки:", result)
