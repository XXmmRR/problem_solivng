Решения задач для книги http://aliev.me/runestone/Introduction/ProgrammingExercises.html

1 Реализуйте простые методы getNum и getDen, возвращающие числитель и знаменатель дроби.

2 Во многих отношениях было бы лучше, если бы все дроби приводились в сокращённом виде с самого начала. Измените конструктор класса Fraction таким образом, чтобы GCD с самого начала использовался для сокращения дробей. Заметьте, это означает, что функция __add__ больше не нуждается в сокращениях. Произведите необходимые модификации.

3 Реализуйте оставшиеся простые арифметические операторы (__sub__, __mul__ и __truediv__).

4 Реализуйте оставшиеся операторы отношений (__gt__, __ge__, __lt__, __le__, and __ne__)

5 Модифицируйте конструктор класса дробей таким образом, чтобы он поверял, являются ли числитель и знаменатель целыми числами. Если хотя бы одно из условий не выполняется, то вызовите исключение.

6 В определении дробей мы предположили, что отрицательные дроби имеют отрицательный числитель и положительный знаменатель. Использование отрицательного знаменателя может повлечь за собой неправильные результаты некоторых операторов отношений. Вообще, это ограничение является не таким уж необходимым. Модифицируйте конструктор таким образом, чтобы пользователь мог вводить отрицательный знаменатель, а все операторы продолжали работать правильным образом.

7 Исследуйте метод __radd__. В чём его отличие от __add__? Когда он используется? Реализуйте __radd__.

8 Задание аналогично предыдущему, но на этот раз рассмотрите метод __iadd__.

9 Исследуйте __repr__ метод. Чем он отличается от __str__? Когда используется? Реализуйте __repr__.

В файле fraction.py я реализовал все нужные функции из этого списка

11 Наиболее простая арифметическая цепь называется полусумматор. Исследуйте и реализуйте её.

12 Теперь расширьте эту цепь и реализуйте 8-битный полный сумматор.

13 Симуляция цепи, показанная в данной части, работает в обратном направлении. Другими словами, выходное значение вычисляется с помощью обратного прохода через входные значения, которые в свою очередь запрашивают свои выходы. Это продолжается до тех пор, пока очередь не дойдёт до внешних входных линий. Именно в этот момент значения для них будут запрошены у пользователя. Измените реализацию таким образом, чтобы эти действия происходили в прямом направлении: схема вычисляла занчение выхода после получения данных на входах.

В файле half_summator.py я реализовал эти задачи