# Database Functions

# ------------------ Importing Libraries ------------------ #
import sqlite3 as sl


# ------------------ Database Functions ------------------ #

def create_database(database_name):
    connection = sl.connect(str(database_name))


def create_table(database_name, table_name, table_parameters):
    connection = sl.connect(str(database_name))

    sql_create_table = f"CREATE TABLE {table_name} ("
    for key, value in table_parameters.items():
        sql_create_table = sql_create_table + key + ' ' + value + ', '
    sql_create_table = sql_create_table[:len(sql_create_table) - 2] + ');'

    with connection:
        connection.execute(sql_create_table)


def insert_data(database_name, table_name, table_parameters, data_tuple):
    connection = sl.connect(str(database_name))
    sql_insert_data = f"INSERT INTO {table_name} ("
    sql_insert_tuple = "("

    for key in table_parameters.keys():
        if "AUTOINCREMENT" not in table_parameters[key]:
            sql_insert_data = sql_insert_data + key + ', '
            sql_insert_tuple = sql_insert_tuple + '?, '
    
    sql_insert_data = sql_insert_data[:len(sql_insert_data) - 2] + ') values ' + sql_insert_tuple[:len(sql_insert_tuple) - 2] + ')'

    with connection:
        connection.execute(sql_insert_data, data_tuple)


def retrieve_data(database_name, table_name, id_num):
    connection = sl.connect(str(database_name))
    sql_retrieve = f"SELECT * FROM {table_name} WHERE id={id_num}"

    data_output = []
    with connection:
        output = connection.execute(sql_retrieve)
        for data in output:
            data_output.append(data)

    return data_output