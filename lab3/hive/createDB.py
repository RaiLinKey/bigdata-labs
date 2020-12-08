from pyhive import hive
import pyhdfs

fs = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="kali")
conn = hive.Connection(host="localhost", port=10000, username="kali")
cursor = conn.cursor()

cursor.execute("create database if not exists sample_company")
cursor.execute("use sample_company")
cursor.execute("create table if not exists office (id int, name string, place string)")
cursor.execute("create table if not exists work_place(id int, type string, id_office int)")
cursor.execute("create table if not exists workers(id int, surname string, name string, otchestvo string,"
               "position string, salary int, id_wp int)")

with fs.open("/user/kali/input/office/office") as f:
    values = ''
    for line in f.readlines():
        sym_arr = line.decode().strip().split("\t")
        values += f'({sym_arr[0]}, "{sym_arr[1]}", "{sym_arr[2]}"), '
    values = values[0:-2]
    cursor.execute(f"insert into office(id, name, place) values {values}")
    # print(f"insert into office(id, name, place) values {values}")

with fs.open("/user/kali/input/work_place/work_place") as f:
    values = ''
    for line in f.readlines():
        sym_arr = line.decode().strip().split("\t")
        values += f'({sym_arr[0]}, "{sym_arr[1]}", {sym_arr[2]}), '
    values = values[0:-2]
    cursor.execute(f"insert into work_place(id, type, id_office) values {values}")
    # print(f"insert into work_place(id, type, id_office) values {values}")

with fs.open("/user/kali/input/workers/workers") as f:
    values = ''
    for line in f.readlines():
        sym_arr = line.decode().strip().split("\t")
        values += f'({sym_arr[0]}, "{sym_arr[1]}", "{sym_arr[2]}", "{sym_arr[3]}", ' \
                  f'"{sym_arr[4]}", {sym_arr[5]}, {sym_arr[6]}), '
    values = values[0:-2]
    cursor.execute(f"insert into workers(id, surname, name, otchestvo, position, salary, id_wp) values {values}")
    # print(f"insert into work_place(id, surname, name, otchestvo, position, salary, id_wp) values {values}")

print("complete")

# for result in cursor.fetchall():
#     print(result)
