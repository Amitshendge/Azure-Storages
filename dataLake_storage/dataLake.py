'''
@Author: Amit Shendge
@Date: 2022-01-08 6:30 PM
@Title : DataLake-Storage
'''
class DataLakeSamples():
    """
    Description:
        Class for create Table Storage, Add , Update, Delete, Get Entity from Table Storage
    """
    import os
    from azure.storage.filedatalake import DataLakeServiceClient,DataLakeFileClient
    from dotenv import load_dotenv
    load_dotenv("data.env")
    connection_string = os.getenv("connection_string")
    service = DataLakeServiceClient.from_connection_string(conn_str=os.getenv("connection_string"))

    def create_container(self,name):
        """
        Description:
            Function for creating the Datalake container
        Parameter:
            using name for a new Datalake container
        Return:
            None
        """
        try:
            self.service.create_file_system(name)
            print("New Container created:",name)
        except:
            print("Container with name ",name," already Exists")

    def delet_container(self,name):
        """
        Description:
            Function for Deleting the Datalake container
        Parameter:
            using name for a Deleting Datalake container
        Return:
            None
        """
        try:
            self.service.delete_file_system(name)
            print("Container Deleted:",name)
        except:
            print("Container with name ",name," does not Exists")

    def upload_file(self,container_name,file_name):
        """
        Description:
            Method for uploading the file into Datalake container
        Parameter:
            using file name which is to be uploaded and container name where to be uploaded
        Return:
            None
        """
        dataclient = self.DataLakeFileClient.from_connection_string(self.connection_string,container_name,file_path=file_name)
        dataclient.create_file()
        local_file = open(file_name,'r')
        file_contents = local_file.read().encode("utf8")
        print(file_contents)
        dataclient.append_data(data=file_contents, offset=0, length=len(file_contents))
        dataclient.flush_data(len(file_contents))

    def download_file(self,container_name,file_name):
        """
        Description:
            Method for downloading the file from Datalake container
        Parameter:
            using file name which is to be downloaded, container name from to be downloaded
        Return:
            None
        """
        file = self.DataLakeFileClient.from_connection_string(conn_str=self.connection_string,
                                                 file_system_name=container_name, file_path=file_name)

        with open(file_name, "wb") as my_file:
            download = file.download_file()
            download.readinto(my_file)


if __name__ == '__main__':
    sample = DataLakeSamples()
    # sample.create_container("newdata")
    # sample.delet_container("newdata")
    # sample.upload_file("newdata","downloadedfile.txt")
    # sample.download_file("newdata","downloadedfile.txt")
