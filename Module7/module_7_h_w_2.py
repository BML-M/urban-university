# Создание текстового файла и запись текста
with open('my_poem.txt', 'w') as file:
    file.write("""# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.""")

# Чтение содержимого текстового файла и печать в консоль
with open('my_poem.txt', 'r') as file:
    print(file.read())

# Отличие использования оператора with от file.close() заключается в том, что при использовании with не нужно явно закрывать файл с помощью метода close().
# Оператор with автоматически закрывает файл после завершения работы в его блоке, что делает код более чистым и безопасным, так как гарантируется закрытие файла даже в случае возникновения исключения.
