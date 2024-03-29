# Алгоритм замены символа звездочки и предшествующего ей символа с учетом их произвольного количества. Программная эмуляция Backspace.

Написать на python функцию, которая принимает тип string как параметр и в данной строке звёздочку заменяет на эффект "backspace" самой звездочки и символа до нее, т.е. удаляет звездочку и один символ перед ней. 

## Случаи использования:

1.  **Нет звездочек:**
    
    -   Если в строке нет звездочек, то программа просто вернет исходную строку без изменений.
2.  **Одна звездочка в начале строки:**
    
    -   Если строка начинается с звездочки, программа просто удаст эту звездочку и символ перед ней.
3.  **Одна звездочка в середине/конце строки:**
    
    -   Программа удаляет звездочку и символ перед ней в любом месте строки.
4.  **Две звездочки подряд:**
    
    -   Если в строке есть две звездочки подряд, программа удаляет обе звездочки и два символа перед ними.
5.  **Две звездочки, но не подряд:**
    
    -   Если есть две звездочки, но они не находятся подряд, программа удаляет только первую звездочку и символ перед ней.
6.  **Пустая строка:**
    
    -   Если входная строка пуста, программа также вернет пустую строку.

Таким образом, алгоритм учитывает различные сценарии и обрабатывает их корректно.

Конкретные примеры:

 1.  **Если в строке N звездочек, то удаляет N звездочек и N символов перед ними.**
    
    -   Пример: `"abc**def***ghi"` превращается в `"ghi"`.
 2.  **Учитывает вариативность звездочек, в том числе, если звездочки идут подряд N раз.**
    
    -   Пример: `"abc*def**ghi"` превращается в `"adefghi"`.
 3.  **Если в строке отсутствует звездочка, то возвращает исходную строку без изменений.**
    
    -   Пример: `"abcdefghi"` остается без изменений.
 4.  **Если строка начинается с звездочки, то удаляет эту звездочку и символ перед ней.**
    
    -   Пример: `"*abc*def*ghi"` превращается в `"abc*def*ghi"`.
 5.  **Если строка заканчивается звездочкой, то удаляет эту звездочку и символ перед ней.**
    
    -   Пример: `"abc*def*ghi*"` превращается в `"abc*def*ghi"`.
 6.  **Пустая строка возвращает пустую строку.**
    
    -   Пример: `""` остается без изменений.
 7.  **Если входной аргумент `None`, то возвращает пустую строку.**
    
    -   Пример: `None` превращается в `""`.
 8.  **Если входной аргумент не является строкой, вызывается `TypeError`.**
    
    -   Пример: `123` вызывает исключение `TypeError`.
 9. Если строка заканчивается звездочкой, то программа удаляет эту звездочку и символ перед ней.

Пример:-   Входная строка `"*abc*def*ghi*"` превращается в `"abc*def*ghi"`
Эти сценарии были учтены в тестах:

    python -m unittest test_backspace_replacer
    

В этих тестaх прoверяются рaзличные сцeнарии, включая oтсутствие звeздочек, наличие одной и двух звездочек пoдряд, a также грaничные условия, такие как пустaя строка и None в кaчестве входных дaнных. 
