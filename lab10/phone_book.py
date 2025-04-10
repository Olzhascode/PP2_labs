import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="Kesha2412:)",
    host="localhost",
    port="5432"
)
cur = conn.cursor()