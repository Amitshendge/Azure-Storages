'''
@Author: Amit Shendge
@Date: 2022-01-06 6:00 PM
@Title : Blob-Storage 
'''
class BlobSamples(object):
    """
    Description:
        Class for create container,upload file,download file,listing files & to delete container from the azure bolo-storage
    """
    import os
    from dotenv import load_dotenv
    load_dotenv("data.env")
    from azure.storage.blob import BlobServiceClient
    connection_string = os.getenv("connection_string")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def create_container(self,name):
        """
        Description:
            Function for creating the Blob container
        Parameter:
            using name for a new container
        Return:
            None
        """
        try:
            self.blob_service_client.create_container(name)
            print("New container created:",name)
        except:
            print("Container with name ",name," already Exists")

    def list_containers(self):
        """
        Description:
            Function Listing existing Blob containers
        Parameter:
            No parameter required self object is sufficient
        Return:
            None
        """
        no=0
        for i in self.blob_service_client.list_containers():
                no= no+1
                print(no,".",i["name"])
    
    def delet_containers(self,name):
        """
        Description:
            Function for Deleting the Blob container
        Parameter:
            using name for a Deleting container
        Return:
            None
        """
        try:
            self.blob_service_client.delete_container(name)
        except:
            print("Container with name ",name," does not Exists")

    def download_blob(self,file_name,container_name,output_dest_path=""):
        """
        Description:
            Method for downloading the file from blob container
        Parameter:
            using file name which is to be downloaded, container name from to be downloaded and output path if required
        Return:
            None
        """
        if output_dest_path!="":
            dest=str(output_dest_path+"/"+file_name)
        else:
            dest=file_name
        
        container_client=self.blob_service_client.get_container_client(container_name)
        download_stream=container_client.download_blob(blob=file_name).readall()
        with open(dest,"wb") as file:
            file.write(download_stream)

    def upload_blob(self,file_name,container_name):
        """
        Description:
            Method for uploading the file into blob container
        Parameter:
            using file name which is to be uploaded and container name where to be uploaded
        Return:
            None
        """
        container_client=self.blob_service_client.get_container_client(container_name)
        try:
            with open(file_name, "rb") as single_file:
                    container_client.upload_blob(data=single_file,name=file_name)
        except:
            print("File already Exists")
    
    def upload_from_folder(self,path,container_name):
        """
        Description:
            Method for uploading multiple or single file from a folder into blob container
        Parameter:
            using path of folder and container name where to be uploaded
        Return:
            None
        """
        files_in_folder = self.os.listdir(path)
        container_client=self.blob_service_client.get_container_client(container_name)
        for single_file in files_in_folder:
            container_client.upload_blob(data=single_file,name=single_file)

    def list_blob(self,container_name):
        """
        Description:
            Method for Listing the files in blob container
        Parameter:
            using container name
        Return:
            None
        """
        container_client=self.blob_service_client.get_container_client(container_name)
        no=0
        for i in container_client.list_blobs():
            no= no+1
            print(no,".",i["name"])

    def download_all_blobs(self,container_name,output_dest_path=""):
        """
        Description:
            Method for downloading all the files
        Parameter:
            using container name and path where to be downloaded
        Return:
            None
        """
        container_client=self.blob_service_client.get_container_client(container_name)
        for i in container_client.list_blobs():
            file_name=i["name"]
            if output_dest_path!="":
                dest=str(output_dest_path+"/"+file_name)
            else:
                dest=file_name
            download_stream=container_client.download_blob(blob=file_name).readall()
            with open(dest,"wb") as file:
                file.write(download_stream)
        print("All Files successfully downloaded")

    def delet_blob(self,container_name,file_name):
        """
        Description:
            Method for deleting file or blob from container
        Parameter:
            using container name and file name to be deleted
        Return:
            None
        """
        container_client=self.blob_service_client.get_container_client(container_name)
        container_client.delete_blob(file_name)
        print(file_name,"has been deleted Successfully")

    def delet_all_containers(self):
        """
        Description:
            Method for deleting all containers
        Parameter:
            No parameter required self object is sufficient
        Return:
            None
        """
        try:
            temp=0
            for i in self.blob_service_client.list_containers():
                self.delet_containers(i)
                temp=1
            if temp==1:
                print("All containers have been Deleted successfully")
            else:
                print("There were no containers to delet")
        except:
            print("Error Occured while deleting all containers")


if __name__ == '__main__':
    sample = BlobSamples()
    # sample.list_containers()
    # sample.delet_containers('temp')
    # sample.create_container('temp')
    # sample.upload_blob("downloaded.txt","temp")
    # sample.download_blob("testfile.txt","temp","test_folder")
    # sample.list_containers()
    # sample.upload_from_folder("/home/amit/practise/input_data","newcon")
    # sample.delet_all_containers()
    # sample.list_blob("temp")
    # sample.download_all_blobs("temp","another_test")
    # sample.delet_blob('temp','downloaded.txt')
    # sample.list_blob("temp")