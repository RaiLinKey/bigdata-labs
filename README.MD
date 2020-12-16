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
**REQ1**
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
Будет добавлено чуть позже. :) 