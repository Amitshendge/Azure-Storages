'''
@Author: Amit Shendge
@Date: 2022-01-07 7:30 PM
@Title : Table-Storage 
'''
class TableSamples():
    """
    Description:
        Class for create Table Storage, Add , Update, Delete, Get Entity from Table Storage
    """
    from random import randint
    import os
    from azure.cosmosdb.table.tableservice import TableService
    from azure.cosmosdb.table.models import Entity
    table_service = TableService(account_name=os.getenv("account_name"), account_key=os.getenv("account_key"))

    def create_table(self,table_name):
        """
        Description:
            Function for creating the Table Storage
        Parameter:
            using name for a new Table Storage
        Return:
            None
        """
        self.table_service.create_table(table_name=table_name)
        print('Table created successfully')

    def add_entity(self,table_name,row_key):
        """
        Description:
            Function for adding entity in Table Storage
        Parameter:
            using name of table and row key
        Return:
            None
        """
        try:
            task = self.Entity()
            task.PartitionKey = 'tasksSeattle'
            task.RowKey = str(row_key)
            task.description = 'Wash the car'
            task.priority = 100
            self.table_service.insert_entity(table_name, task)
            print("Entity added successfully")
        except:
            print("row key already exists")

    def update_entity(self,table_name):
        """
        Description:
            Function for updating entity in Table Storage
        Parameter:
            using name of table
        Return:
            None
        """
        try:
            task = self.Entity()
            task.PartitionKey = 'tasksSeattle'
            task.RowKey = '55'
            task.description = 'Break the car'
            task.priority = 100
            self.table_service.update_entity(table_name, task)
            print("Entity updated successfully")
        except:
            print("Entity does not exists")

    def insert_or_replace_entity(self,table_name):
        """
        Description:
            Function for inserting or replacing entity in Table Storage
        Parameter:
            using name of table
        Return:
            None
        """
        try:
            task = self.Entity()
            task.PartitionKey = 'tasksSeattle'
            task.RowKey = str(self.randint(1,1000))
            task.description = 'Break the car'
            task.priority = 100
            self.table_service.insert_or_replace_entity(table_name, task)
            print("Entity added successfully")
        except:
            print("Row Key already exists")

    def get_entity(self,table_name,partition_key,row_key):
        """
        Description:
            Function for getting entity in Table Storage
        Parameter:
            using name of table with partition and row key
        Return:
            None
        """
        task = self.table_service.get_entity(table_name= table_name,partition_key= partition_key,row_key= row_key)
        print(task.description)
        print(task.priority)

    def delet_entity(self,table_name,partition_key,row_key):
        """
        Description:
            Function for deleting entity in Table Storage
        Parameter:
            using name of table with partition and row key
        Return:
            None
        """
        try:
            task = self.table_service.delete_entity(table_name= table_name,partition_key= partition_key,row_key= row_key)
            print("Entity Deleted Successfully")
        except:
            print("Entity Does not Exists")



if __name__ == '__main__':
    sample = TableSamples()
    # sample.create_table('tasktable')
    # sample.add_entity('tasktable','55')
    # sample.update_entity('tasktable')
    # sample.insert_or_replace_entity('tasktable')
    # sample.get_entity('tasktable','tasksSeattle','55')