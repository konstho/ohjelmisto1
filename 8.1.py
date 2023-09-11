import mysql.connector
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='inkkukinkku55',
        autocommit=True
    )

input = input("anna lentokentän ICAO-koodi: ")
sql = f"select name, municipality from airport where ident = '{input}';"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(f"lentokenttä on: {tulos}")

