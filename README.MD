Тестовое задание в mail.ru на позицию автотестера.

Общие правила:

0. Установить requirements.txt
1. Для каждого аппарата нужно запускать отдельный сервер Appium.
2. Настройки подключаемых аппаратов нужно добавлять в devices.ini по шаблону:
[device<%x>]
name = Android
version = 7.0
device = Honor 8 Lite
country = Russia
port = 5723

2.1 X - порядковый номер подключаемого аппарата
2.2 name - Android для Андроида и iOS для Айфона
2.3 version - версия OS на аппарате
2.4 device - наименование аппарата (пишите что хотите, но в логах будет отображаться именно наименование)
2.5 country - страна (по дефолту Russia)
2.6 port - порт сервера Appium, который вы запустили для этого аппарата

3. запуск кейса в командной строке:

pytest case_rukkola.py -n <%x>

где x количество подключенных аппаратов.

На Linux не проверялось, на работать должно (раз на винде работает, то уж на линуксе по идее еще лучше будет)
На MacOS не проверял.

Плюс, в задании написано про редактирование, но в редактирования в ресторане нет. Можно "объявиться владельцем".
Может не туда смотрел. Такие дела.

По архитектуре: можно написать свой фреймворк, но нужно больше кейсов. Около 10, не меньше, желательно разнообразных.
Надо найти общие признаки, выделить их в отдельные методы, и, в теории, можно сильно упростить и ускорить написание
кейсов.