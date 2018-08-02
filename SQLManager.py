"""Database Management."""
__author__ = "Afonso Medeiros"

import MySQLdb as mysql

class MySQL(object):
    """Class MySQL database management"""

    __connection = None
    __connected = False
    __cursor = None
    __params = ()

    def __connect(self):
        """instance connection, command management ang flag connection."""
        self.__connection = mysql.connect(host='', user='', passwd='', db='')
        self.__connected = True
        self.__cursor = self.__connection.cursor()

    def __end_connection(self):
        """End connection, command management and flag connection."""
        if self.__connected:
            self.__connection.close()
            self.__connection = None
            self.__cursor.close()
            self.__cursor = None
            self.__connected = False
        else:
            pass

    def add_param(self, param):
        """Include parameter for execute procedure."""
        self.__params += (param, )

    def add_params(self, *params):
        """Include a list of parameter for execute procedure."""
        for param in params:
            self.__params += (param, )

    def manipulate_procedure(self, procedure: str):
        """
        Execute manipulation procedure.
        Delete, Update, Insert
        procedure :param -> str
        """
        if not self.__connected:
            self.__connect()

        self.__cursor.callproc(procedure, self.__params)
        self.__connection.commit()
        self.__end_connection()

    def consult_procedure(self, procedure: str):
        """
        Execute query procedure.
        procedure :param -> str
        :return -> tuple
        """
        if not self.__connected:
            self.__connect()

        self.__cursor.callproc(procedure, self.__params)
        result_query = self.__cursor.fetchall()
        self.__end_connection()
        if len(result_query) > 1:
            return result_query
        else:
            return result_query[0]

    def manipular_sql(self, sql):
        """Reveive custom sql command for manipulating data"""
        if not self.__connected:
            self.__connect()

        self.__cursor.execute(sql)
        self.__connection.commit()
        self.__end_connection()

    def consultar_sql(self, sql):
        """Receive custom sql command for query."""
        if not self.__connected:
            self.__connect()

        self.__cursor.execute(sql)
        result_query = self.__cursor.fetchall()
        self.__end_connection()
        if len(result_query) > 1:
            return result_query
        else:
            return result_query[0]
