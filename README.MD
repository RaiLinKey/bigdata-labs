# Лабы по BigData
## Лаба 1 HDFS клиент
Чтобы всё заработало достаточно запустить Hadoop (`hdpStart.sh`). Если появятся проблемы, то сначала нужно выключить хадуп (`hdpStop.sh`), затем очистить файловую систему (`hdpClean.sh`) и снова запустить.  

Для запуска достаточно просто запустить на питоне `main.py`.
## Лаба 2 MapReduce
Сначала в hdfs выгружаются входные данные. Входные данные в данном случае это файлы `inputBD` папках MR1 и MR2. Он идентичны. Чтобы вгрузить данные нужно запсутить любой файл `copyInput.sh`. Чтобы сгенерировать Новые входные данные, нужно в питоне запустить файл `bdgen.py`. Тогда сформируется новый `inputBD`, который нужно закинуть в одну дирректорию с `copyInput.sh`.  

В папке MR1 находится реализованный паттерн cross-corelation pairs. В MR2 лежит cross-corelation stripes.  

Для запуска одного или другого метода используется `runPy.sh` в папках MR1 и MR2.  

Чтобы вывести полученные данные в корне лабы нужно запустить `main.py`.
## Лаба 3 Pig, Hive, MapReduce
### Начало
Запускаем хадуп, затем скрипты Лебедева `hiveMeta.sh` и `hiveStart.sh` как в его инструкции.  

Далее в папке `deploy` нужно запустить `deploy_data.py`, чтобы загрузить данные в hdfs. Данные представлены в виде:  
```
data\tdata\t...data\n
```
Запросы к бд в лабе на SQL:  
*REQ1*
```sql
SELECT workers.id, workers.surname, workers.name, workers.otchestvo, workers.position, office.place FROM workers
    JOIN work_place ON workers.id_wp=work_place.id
    JOIN office ON work_place.id_office=office.id
```
*REQ2*
```sql
SELECT work_place.id, work_place.type, office.name, office.place FROM work_place
    JOIN office ON work_place.id_office=office.id
```
*REQ3*
```sql
SELECT workers.id, workers.surname, workers.name, workers.otchestvo, workers.position, work_place.type FROM workers
    JOIN work_place ON workers.id_wp=work_place.id
```
*REQ4*
```sql
SELECT * FROM workers
    WHERE salary>=150000
```
*REQ5*
```sql
SELECT workers.id, workers.surname, workers.name, workers.otchestvo, workers.salary FROM workers
    WHERE position='Programmer'
```
### Hive
Всё связанное с хайвом находится в папке `hive`. Для создания базы данных и таблиц и внесения данных в эту бд нужно запустить `createDB.py` и подождать надписи `complete` в консоли. Чтобы произвести запросы нужно запустить `hive_requests.py` и выбрать соответствующий запрос. Чтобы выйти нужно ввести `exit`.  

Принцип работы тут максимально прост: с помощью библиотеки `pyhive` отправлятся запросы в бд и в случае необходимости выводятся ответы. При создании бд ответы нам выводить не нужно, при совершении запросов резултатом запроса как раз будет полученный ответ.
### Pig
Все запросы к pig можно запихнуть в один pig-скрипт. Чтобы запустить этот скрипт, в консоли нужно написать `pig sampleDB.pig`. Результат его выполнения отправляется в HDFS.  

Чтобы вывести результаты запросов, нужно запустить `readPig.py` и ввести соответсвующий запрос.  

В принципе работы pig тоже ничего сложного нет. По большому счёту, это просто получение данных из HDFS и разделение их по "таблицам", затем написание запросов схожих с SQL.
### MapReduce
В мапредьюсе для каждого запроса свои мапперы и редьюсеры. Для выполнения запроса нужно зайти в соответствующую папку и запустить `runPy.sh`. Единственное отличие в `req1` из-за двойного джоина, нужно 2 раза сделать мапредьюс, а значит написать 2 маппера и 2 редьюсера, следовательно и запустить их нужно последовательно. Поэтому там 2 файла `runPy.sh`. Чтобы всё заработало достаточно запустить ранпай только с индексом 1. Они были разделены мно для более простой отладки при "разработке".  

2 и 3 запросы тоже содержат джоины, но они написаны не так как требует Лебедев. По его требованиям написан только 1-й запрос. Поэтому 2 и 3 запросы рассматривать не буду. Чтобы переписать мапперы и редьюсеры из 1-го запроса под 2 и 3, достаточно в маппере изменить формат получаемых выводимых данных и в маппере и редьюсере изменить теги, на те которые вам нужны. В целом 2 и 3 запросы работают, но по неправильной логике.  

4 и 5 запросы не представляют из себя ничего сложного и можно было обойтись одним только маппером в каждом, но мне было лень экспериментировать, поэтому редьюсер просто выводит в консоль то, что получает от маппера.  

Имеет смысл разбирать код только одного мапредьюса из 1-го запроса.  

*`mapperReq1.py`*
```python
1 #!/usr/bin/python3
2 import sys
3 
4 for _line in sys.stdin:
5     data = _line.strip().split('\t')
6     if len(data) == 3:
7         print(f'{int(data[0])}\t{["wp", [int(data[2])]]}')
8     else:
9         print(f'{int(data[6])}\t{["workers", [data[0], data[1], data[2], data[3], data[4]]]}')
```
На 1-й строчке указано то, откуда хадуп будет брпть интерпретатор питона (на сколько я понял).  
На 4-й строчке получаем строку из консоли (а именно туда хадуп выводит данные из файлов в input-папке, которая указывается в `runPy.sh`).  
Далее разделяем строку по символу табуляции и помещаем данные в переменную `data`.  
Так как маппер в тупую получает все данные из всех входных папок, нужно понять что из какой пришло. Когда мы это поняли выводим данные в консоль в том ввиде, в котором нам нужно: где-то выводим только индекс, где-то выносим его вперёд. формат вывода:  
`id (по которому производится join)\t[тег(в редьсере по нему будем понимать что к чему присоединять), [data, data...]]`  
*`reducerReq1.py`*
```python
1  #!/usr/bin/python3
2  import sys
3 
4  tag1 = "wp"
5  tag2 = "workers"
6  h = {}
```
Начало как в маппере. Далее задаются теги для более удобного использования. Теги соответствуют тем, которые отправляет маппер. И создаётся пустой словарь, с которым мы потом и будеи работать.

```python
22 for _line in sys.stdin:
23     data = _line.strip().split("\t")
24     key = int(data[0])
25     tagged_tuple = eval(data[1])
26     if not h:
27         h.update({key: [{tagged_tuple[0]: [tagged_tuple[1]]}]})
28     else:
29         if key in list(h.keys()):
30             for i in range(len(h[key])):
31                 if tagged_tuple[0] == list(h[key][i].keys())[0]:
32                     h[key][i][tagged_tuple[0]].append(tagged_tuple[1])
33                 elif len(h[key]) == 1:
34                     h[key].append({tagged_tuple[0]: [tagged_tuple[1]]})
35         else:
36             emit(h)
37             h = {}
38             h.update({key: [{tagged_tuple[0]: [tagged_tuple[1]]}]})
39 
40 emit(h)
```
Получаем данные из консоли, которые нам туда отправил маппери разделяем их. Получаем список, в котором первый элемент этто айдишник, а второй элемент это tagged tuple (проименовый список). Далее приводим обе части к тому виду, с которым можно работать.  

Теперь идёт череда проверок того что будем пихать в словарь h, а что нет. в итоговом варианте должна получится структура:  
```
{id:
    [
        {tag: 
            [data, data...]
        },
        {tag: 
            [data, data...]
        }
    ]
}
```  
В качестве ключа для h используем `id`. Это тот айдишник по которому происходит join.  
По этому ключу отправляем в его значение список словарей. У этих словарей ключ это тег, а значение это данные из "бд".  

Возвращаясь к коду.
* Сначала мы проверяем пустой ли список h.
* Если да, то отправляем туда первые данные.  
* Если словарь не пустой, то смотрим какой ключ для h пришёл.  
   * Если пришёл уже имеющийся айдишник значит проверям тэг.  
      * Если такой тег уже в списке, добавляем к словарю с ключом соответствующим тегу данные.  
      * Если тега ещё нет, добавляем словарь с ключом соответствующем тегу вместе с данными в список.  
   * Если айдишник пришёл другой, то нужно вывести данные, очистить список и добавить в него эти новые данные.  

В конце у нас получается ситуация, что пришли последние данные, а новый айдишник не пришёл, поэтому словарь не будет выведен. Чтобы это исправить выводим данные вне цикла считывания данных из консоли. Тогда выведутся данные, которые у нас остались в самом конце.

Теперь подробнее про вывод.
```python
9  def emit(t):
10     for key in list(t.keys()):
11         wp = []
12         workers = []
13         for i in range(len(t[key])):
14             if list(t[key][i].keys())[0] == tag1:
15                 wp = t[key][i][tag1][0]
16             elif list(t[key][i].keys())[0] == tag2:
17                 workers = t[key][i][tag2]
18         for worker in workers:
19             print(f"{worker[0]}\t{worker[1]}\t{worker[2]}\t{worker[3]}\t{worker[4]}\t{wp[0]}")
```  
На вход функции вывода мы получаем словарь h (в описании функции я использовал t, чтобы не было конфликта глобальных и локальных переменных).  
Для удобства работы со словарём (а если быть точнее, то именно с ключом) я запускаю цикл, который проживёт всего одну итерацию, потому что ключ у основного словаря у нас только один.  
Создаём пустые списки, которые потом заполним данными на вывод.  
Теперь запускаем цикл, который занесёт данные на вывод соответствующие списки. Дальше я не помню что происходит и как это работает, но это работает и заносятся правильные данные.  
В конце просто вывод в консоль полученных данных. Тут нужно просто понимать что на какой позиции находится... 
