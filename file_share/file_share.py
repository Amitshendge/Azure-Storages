'''
@Author: Amit Shendge
@Date: 2022-01-07 6:00 PM
@Title : File-Share-Storage 
'''
class FileShareSamples(object):
    """
    Description:
        Class for create File Share,upload file,download file,listing contents from File-Share-storage
    """
    import os
    from dotenv import load_dotenv
    load_dotenv("data.env")
    from azure.storage.fileshare import ShareClient,ShareFileClient,ShareDirectoryClient
    connection_string = os.getenv("connection_string")

    def create_share(self,name):
        """
        Description:
            Function for creating the File Share
        Parameter:
            using name for a new File Share
        Return:
            None
        """
        share = self.ShareClient.from_connection_string(self.connection_string,share_name=name)
        try:
            share.create_share()
            print("New share created:",name)
        except:
            print("Share with name ",name," already Exists")

    def delet_share(self,name):
        """
        Description:
            Function for Deleting the File Share
        Parameter:
            using name for a Deleting File Share
        Return:
            None
        """
        share = self.ShareClient.from_connection_string(self.connection_string,share_name=name)
        try:
            share.delete_share()
            print("share has been Deleted:",name)
        except:
            print("Share with name ",name," does not Exists")

    def upload_to_share(self,share_name,file_name):
        """
        Description:
            Method for uploading the file into File Share
        Parameter:
            using file name which is to be uploaded and File Share name where to be uploaded
        Return:
            None
        """
        file_client = self.ShareFileClient.from_connection_string(conn_str=self.connection_string, share_name=share_name,file_path=file_name)
        with open(file_name, "rb") as source_file:
            file_client.upload_file(source_file)

    def download_from_share(self,share_name,file_name,output_file):
        """
        Description:
            Method for downloading the file from File Share
        Parameter:
            using file name which is to be downloaded, File Share name from to be downloaded and output file name
        Return:
            None
        """
        file_client = self.ShareFileClient.from_connection_string(conn_str=self.connection_string, share_name=share_name,file_path=file_name)
        with open(output_file, "wb") as file_handle:
            data = file_client.download_file()
            data.readinto(file_handle)

    def list_contents(self,share_name,dir_path=""):
        """
        Description:
            Function Listing contents in File Share
        Parameter:
            using File Share name and path of directory if required
        Return:
            None
        """
        parent_dir = self.ShareDirectoryClient.from_connection_string(conn_str=self.connection_string, share_name=share_name, directory_path=dir_path)
        my_list = list(parent_dir.list_directories_and_files())
        for i in my_list:
            if i['is_directory']:
                print(i['name']+"\t"+"DIR")
            else:
                print(i['name']+"\t"+"FILE")



if __name__ == '__main__':
    sample = FileShareSamples()
    # sample.create_share("tem1")
    # sample.download_from_share('tem1','testfile.txt','downloadedfile.txt')
    # sample.list_contents('tem1')
    # sample.delet_share('tem1')