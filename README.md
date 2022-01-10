# Azure-Storages

    versions Used:
    Python==3.8.10
    azure-storage-blob==12.9.0
    azure-storage-file-share==12.6.0
    azure-storage-queue==12.1.6
    azure-cosmosdb-table==1.0.6
    azure-storage-file-datalake==12.5.0

<h2>Azure Blob storage</h2>
    <h3>Library Used: pip install azure-storage-blob</h3>
    <a href="https://github.com/Amitshendge/Azure-Storages/blob/main/blob_storage/blob.py">blob.py</a>
<p>Here in Azure Blob storage file can be stored directly there is no folder structure available just drop your file in and out when required.</p>
<p>In this code we used a connection string to connect to Azure Storage via blob service client throught which we performed all operations.</p>

<h2>Azure File Share Storage</h2>
    <h3>Library Used: pip install azure-storage-file-share</h3>
    <a href="https://github.com/Amitshendge/Azure-Storages/blob/main/dataLake_storage/dataLake.py">dataLake.py</a>
<p>Here in Azure File Share storage file can be stored inside a folder like structure unlike the blob storages and permissions can be given to each share.</p>
<p>In this code we used a connection string to connect to Azure Storage via share client throught which we performed all operations.</p>
    
<h2>Azure Queue Storage</h2>
    <h3>Library Used: pip install azure-storage-queue</h3>
    <a href="https://github.com/Amitshendge/Azure-Storages/blob/main/queue_storage/queue.py">queue.py</a>
<p>Here in Azure Queue storage we cannot save the Files here only messages can be stored in bytes format which can be queued and dequeued on requirment.</p>
<p>In this code we used a connection string to connect to Azure Storage via queue client throught which we performed all operations.</p>
<p>We also imported Binary 64 Encoder and decoders which helps in encoding and decoding our string to binary format to store and retrive messages.</p>
    
<h2>Azure Table Storage</h2>
    <h3>Library Used: pip install azure-storage-table</h3>
    <a href="https://github.com/Amitshendge/Azure-Storages/blob/main/table_storage/tables.py">tables.py</a>
<p>Here in Azure Table storage we can store a no-SQL like structured entities.</p>
<p>In this code we used a Account name and account key to connect to Azure Storage via table client throught which we performed all operations.</p>

<h2>Azure DataLake Storage</h2>
    <h3>Library Used: pip install azure-storage-file-datalake</h3>
    <a href="https://github.com/Amitshendge/Azure-Storages/blob/main/dataLake_storage/dataLake.py">dataLake.py</a>
<p>Here in Azure DataLake storage file can be stored inside a folder like structure unlike the blob storages and permissions can be given to each share.</p>
<p>In this code we used a connection string to connect to Azure Storage via DataLake Service client throught which we performed all operations.</p>
    
