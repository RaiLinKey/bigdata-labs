from pyhive import hive

conn = hive.Connection(host="localhost", port=10000, username="kali", database="sample_company")
cursor = conn.cursor()


def completed_request(req):
    cursor.execute(req)
    for result in cursor.fetchall():
        print(result)


while True:
    listener = input("What's request check (req1, req2, req3, req4, req5): ")
    if listener == "req1":
        req1 = "select workers.id, workers.surname, workers.name, workers.otchestvo," \
               " workers.position, office.place from workers" \
               " join work_place on workers.id_wp=work_place.id" \
               " join office on work_place.id_office=office.id"
        completed_request(req1)
    elif listener == "req2":
        req2 = "select work_place.id, work_place.type, office.name, office.place from work_place join office on " \
               "work_place.id_office=office.id"
        completed_request(req2)
    elif listener == "req3":
        req3 = "select workers.id, workers.surname, workers.name, workers.otchestvo, workers.position, " \
               "work_place.type from workers join work_place on workers.id_wp=work_place.id"
        completed_request(req3)
    elif listener == "req4":
        req4 = "select * from workers where salary>=150000"
        completed_request(req4)
    elif listener == "req5":
        req5 = "select id, surname, name, otchestvo, salary from workers where position='Programmer'"
        completed_request(req5)
    elif listener == "exit":
        break
    else:
        print("Input ERROR!")
