def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызываем функцию test_function
test_function()

# Попробуем вызвать inner_function вне функции test_function

inner_function()  # Это вызовет ошибку, так как inner_function доступна только внутри test_function
