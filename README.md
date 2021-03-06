thematic_map
============

Создание тематических карт регионов РФ

Описание
--------
Это приложение, которое позволяет отображать данные на карте регионов (субъектов федерации) России – раскрашиват регионы в тот или иной цвет в зависимости от значения определенного признака. На входе имеем файл в формате csv, который содержит две колонки – код региона и значение признака. На выходе имеем раскрашенную карту в формате png.
- Для карты графств США процедура создания скрипта описана здесь — http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/ задача заключалась в том, чтобы модифицировать скрипт для карты регионов России, добавив в него некоторые функции.
- Процесс написания скрипта для создания png-карты из svg-файла и файла с данными подробно описан здесь — http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/ . Он просто повторён для России. 
- Заложина возможность создания карты в нескольких цветовых палитрах. Варианты цветовых палитр см. на http://colorbrewer2.org . Одна из цветовых палитр - градации серого. Кроме нее, реализованно еще три варианта: оранжевый, фиолетовый, зеленый.
- Разбивка данных на интервалы. Предусмотрены следующие возможности: ручная разбивка на 4, 5 и 6 интервалов с ручным заданием границ интервалов (обратите внимание, что коды цветов для палитр с разным количеством интервалов можно узнать на colorbrewer2.org , меняя параметр "number of data classes on your map" в левом верхнем углу страницы). Второй вариант задания интервалов должен быть автоматическим. В этом случае данные автоматически должны делиться на 5 интервалов по квинтилям (нижние 20% случаев в одном интервале, следующие 20% случаев – во втором и т.д.).
- На карте присутствует легенда с указанием того, какой цвет какому интервалу соответствует.
- Работа с неполными данными. Иногда для некоторых регионов отсутствуют исходные данные. В csv-файле с данными отсутствующие значения обозначаются как "NA", "." или просто пробел. В этом случае в цветных палитрах регионы с отсутствующими данными окрашиваются на карте серым цветом. В черно-белой палитре такие регионы заштрихованы. Цвет или рисунок, присвоенный отсутствующим значениям, также выводиться в легенду (в случае когда отсутствующие значения имеются).
- Получившаяся карта сохраняется в формате png по заданнаму пути в локальной файловой системе. 

Примеры получаемых изображений (карт)
-------------------------------------
Пример1

![Screenshot](https://raw.github.com/rusakovprz/thematic_map/master/example_image/Example_image_1.png)

Пример2

![Screenshot](https://raw.github.com/rusakovprz/thematic_map/master/example_image/Example_image_2.png)

Пример3

![Screenshot](https://raw.github.com/rusakovprz/thematic_map/master/example_image/Example_image_3.png)
