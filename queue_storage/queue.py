'''
@Author: Amit Shendge
@Date: 2022-01-07 7:00 PM
@Title : Queue-Storage 
'''
class QueueSamples(object):
    """
    Description:
        Class for create Queue,Delete Queue, Insert Message, Delete Message, clear all messages from Queue
    """
    import os
    from dotenv import load_dotenv
    load_dotenv("data.env")
    from azure.storage.queue import QueueClient,BinaryBase64EncodePolicy,BinaryBase64DecodePolicy
    connection_string = os.getenv("connection_string")

    def create_queue(self,queue_name):
        """
        Description:
            Function for creating the Queue Storage
        Parameter:
            using name for a new Queue Storage
        Return:
            None
        """
        try:
            queue_client = self.QueueClient.from_connection_string(self.connection_string, queue_name=queue_name)
            queue_client.create_queue()
            print("New queue created:",queue_name)
        except:
            print("Queue with name ",queue_name," already Exists")



    def delet_queue(self,queue_name):
        """
        Description:
            Function for Deleting the Queue Storage
        Parameter:
            using name for a Deleting Queue Storage
        Return:
            None
        """
        try:
            queue_client = self.QueueClient.from_connection_string(self.connection_string, queue_name=queue_name)
            queue_client.delete_queue()
            print(queue_name,"has been deleted")
        except:
            print(queue_name,"does not exists")

    def insert_message(self,queue_name,message):
        """
        Description:
            Function for Inserting Message in Queue
        Parameter:
            using name of Queue and message to be inserted
        Return:
            None
        """
        base64_queue_client = self.QueueClient.from_connection_string(
                            conn_str=self.connection_string, queue_name=queue_name,
                            message_encode_policy = self.BinaryBase64EncodePolicy(),
                            message_decode_policy = self.BinaryBase64DecodePolicy()
                        )
        input_message=str(message).encode('utf8')
        base64_queue_client.send_message(input_message)
        print("message added to queue")

    def peek_message_queue(self,queue_name):
        """
        Description:
            Function for getting peek Message in Queue
        Parameter:
            using name of Queue
        Return:
            None
        """
        queue_client = self.QueueClient.from_connection_string(
                            conn_str=self.connection_string, queue_name=queue_name,
                            message_encode_policy = self.BinaryBase64EncodePolicy(),
                            message_decode_policy = self.BinaryBase64DecodePolicy()
                        )
        messages = queue_client.peek_messages()

        for peeked_message in messages:
            print(peeked_message.content)

    def clear_messages(self,queue_name):
        """
        Description:
            Function for clearing all Messages in Queue
        Parameter:
            using name of Queue
        Return:
            None
        """
        queue_client = self.QueueClient.from_connection_string(self.connection_string, queue_name=queue_name)
        queue_client.clear_messages()
        print("Your Queue has been cleared successfully")

    def delet_message(self,queue_name,message):
        """
        Description:
            Function for deleting Message in Queue
        Parameter:
            using name of Queue and message you want to delete
        Return:
            None
        """
        try:
            queue_client = self.QueueClient.from_connection_string(
                            conn_str=self.connection_string, queue_name=queue_name,
                            message_encode_policy = self.BinaryBase64EncodePolicy(),
                            message_decode_policy = self.BinaryBase64DecodePolicy()
                        )
            for i in queue_client.receive_messages():
                if i.content == message.encode("utf8"):
                    queue_client.delete_message(i)
            print("Your message has been deleted")
        except:
            print("Message does not exists")


if __name__ == '__main__':
    sample = QueueSamples()
    # sample.create_queue("tem1")
    # sample.delet_queue("tem1")
    # sample.insert_message("tem1","Hello World")
    # sample.peek_message_queue('tem1')
    # sample.clear_messages('tem1')
    # sample.delet_message('tem1','Hello World')




