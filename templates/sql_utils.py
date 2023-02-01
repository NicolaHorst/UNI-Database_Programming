#!/usr/bin/env python3
"""
Python Class to deal with SQLite databases.

This Module offers a class SqlUtils which allows to create SQLite databases
from csv files and to explore structure and columns of a database as well to
query the database directly from the terminal. It mimics the functionality of the
sqlite3 tool but offers the possibility to work with SQLite3 databases as well
directly in Python by using this class.

Here is the class Outline:

![](https://kroki.io/plantuml/svg/eNpNizsKgEAMRHtPkXLFT6FHUetllSiBuLAk2Ih3N4qK0wy8eTNxEIEu8aDEAnsGlgoEea4lMSm2MzHeuADvKZJ67669_O35I0yyNYad9R8vqH0YGcW9xKTGJKcXjmHF8rscJ5TOLpU=)
"""
import csv
import os
import re
import sqlite3
import sys
from typing import List


class SqlUtils:
    """Utility class to work with SQLite3 databases in Python"""

    def __init__(self):
        pass

    def csv2sql(self, csvfile_name, db_name, table_name="", delimiter=','):
        """Importing a Csv or Tab file into a SQLite3 database.
        Args:
            :param delimiter:
            :param db_name:
            :param csvfile_name:
            :param table_name:
        Return:
            int : number of rows added from the csvfile

        """
        table_name: str = table_name.split(".")[0]

        # Create the database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        query = f"""DROP TABLE IF EXISTS {table_name}"""
        cursor.execute(query)

        csvfile = open(csvfile_name, 'r')
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        delimiter = "\t" if csvfile_name.endswith(".tab") else ","
        columns = ""
        for i, t in enumerate(csv_reader):
            if i == 0:
                columns = t[0].replace(delimiter, ", ").replace(".", "_")
                # create table
                query = f"CREATE TABLE {table_name} ({columns})"
                cursor.execute(query)
            else:
                t = t[0].replace(delimiter, ",")
                t = self.prepare_values(t)
                query = f'INSERT INTO {table_name} ({columns}) VALUES  ({t})'
                cursor.execute(query)

        csvfile.close()
        connection.commit()
        connection.close()

    @staticmethod
    def prepare_values(t, delimiter: str = ","):
        regnumber = re.compile(r'\d+(?:,\d*)?')
        vals: List = t.split(delimiter)
        prepared: str = ""
        for i in vals:
            if regnumber.match(i):
                prepared += f"{i}, "
            else:
                prepared += f'"{i}", '

        return prepared[:-2]

    def get_tables(self):
        """Return the table names of the database.

        Returns:
            list : names of tables
        """
        pass


def usage(argv):
    print(argv)


def main(argv):
    if len(argv) < 2:
        usage(argv)
    else:
        table_name = None
        csv_name = argv[1]
        if not os.path.exists(csv_name):
            print("Path not exist")
            exit()

        if len(argv) > 2:
            table_name = argv[2]

        sq_utils = SqlUtils()
        sq_utils.csv2sql(csvfile_name=csv_name, db_name="iris.sqlite3", table_name=table_name)


# check length of arguments
# should be app-csv2sqlite csvfile sqlitefile
# check if csv file exists
# if exists create object
# call csv2sqlite3
if __name__ == "__main__":
    main(sys.argv)
