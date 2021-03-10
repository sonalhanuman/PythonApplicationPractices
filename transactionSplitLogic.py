import psycopg2

# def clear_country_table():
#     conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("DROP TABLE IF EXISTS")
#     conn.commit()
#     conn.close()

def create_transaction_group_table():
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS T_TRANSACTIONGROUP (GROUP_NAME TEXT, PASSWORD TEXT)")
    conn.commit()
    conn.close()
def create_transaction_record_table():
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS T_TRANSACTIONRECORD (GROUP_NAME TEXT, PASSWORD TEXT, NAME TEXT, MONEY DECIMAL(9,2))")
    conn.commit()
    conn.close()

def insert_transaction_group(group_name, password):
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO T_COUNTRYPEDIA VALUES ('%s', '%s', '%s')" % (country, capital, population))
    cur.execute("INSERT INTO T_TRANSACTIONGROUP VALUES (%s, %s)", (group_name, password))
    conn.commit()
    conn.close()

def insert_transaction_record(group_name, password, name, money):
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO T_COUNTRYPEDIA VALUES ('%s', '%s', '%s')" % (country, capital, population))
    cur.execute("INSERT INTO T_TRANSACTIONRECORD VALUES (%s, %s, %s, %s)", (group_name, password, name, money))
    conn.commit()
    conn.close()
    
def select_transaction_group(group_name, password):
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM T_TRANSACTIONGROUP WHERE GROUP_NAME=%s AND PASSWORD=%s", (group_name,password))
    transactionRows=cur.fetchall()
    conn.close()
    return transactionRows

def select_transactions_records(name, money):
    conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM T_TRANSACTIONRECORD WHERE NAME=%s AND MONEY=%s", (name,money))
    transactionRows=cur.fetchall()
    conn.close()
    return transactionRows
# def view_entire_country_table():
#     conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM T_COUNTRYPEDIA")
#     countryrows=cur.fetchall()
#     conn.close()
#     return countryrows

# def delete_country_info(country):
#     conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM T_COUNTRYPEDIA WHERE country=%s", (country,))
#     conn.commit()
#     conn.close()

# def update_country_info(country, capital, population):
#     conn = psycopg2.connect("dbname='countryInfoDatabaseTest' user='postgres' password='postgres123' host='localhost' port='5432'")
#     cur = conn.cursor()
#     cur.execute("UPDATE T_COUNTRYPEDIA SET capital=%s, population=%s WHERE country=%s", (capital, population, country))
#     conn.commit()
#     conn.close()

# Run Sequence

# # clear_country_table()
# create_country_table()
# # insert_country_info("Singapore", "Singapore", 5638700)
# # insert_country_info("Cambodia", "Phnom Penh", 16486542)
# # insert_country_info("ThailandR", "Phnom Penh", 16486542)
# # insert_country_info("Peru", "Lima", 32510453)
# update_country_info("Thailand", "Bangkok", 69625582)
# # delete_country_info("ThailandR")
# print(view_entire_country_table())