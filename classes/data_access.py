'''
Created on Mar 25, 2015

@author: Liyan Xu; Hongmou Zhang
'''
import pyodbc
# from household import Household


class DataAccess(object):
    '''
    Class for accessing data from the database
    '''
    
    def __init__(self, dbname, dbdriver):
        '''
        dbname: path+name of DB
        dbdriver: specific database driver (pyodbc related definition)
        '''
        self.connector = pyodbc.connect('DRIVER={};DBQ={}'.format(dbdriver, dbname))
        self.cursor = self.connector.cursor()




    def get_table (self, table_name):
        '''
        Get a table by a given name in the database; create a pointer to that table
        '''
        
        try:
    
            table_cursor = self.cursor.execute('SELECT * FROM ' + table_name)
            table = table_cursor.fetchall()        
        
            return table
        
        except pyodbc.ProgrammingError: #This is ridiculously indecent... How to get a None value decently here?
            return None

        

    def get_var_list(self, table_name):
        '''
        Get the variables list for a table by a given name in the database
        '''

        var_list = list()
        for row in self.cursor.columns(table=table_name):
            var_list.append((row.column_name, row.ordinal_position-1, row.type_name))        
    
        return var_list
    



    def create_table(self, order):
        '''
        Create a new table in the database by an order,
        Which is a "create table from ..." sql order in string format
        '''
        self.cursor.execute(order)

    

    def insert_table(self, order):
        '''
        Insert a new record to a table in the database by an order, similar as "create_table"
        '''
        self.cursor.execute(order)
    
    
    def db_commit(self):
        '''
        Commit an activity in the database
        '''
        self.connector.commit()        

    