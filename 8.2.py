import mysql.connector
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='inkkukinkku55',
        autocommit=True
    )

input = input("anna maakunta: ")
sql = f"select type, count(*) from airport where iso_country = '{input}' group by type;"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for i in tulos:
        print(i)
