import boto3

# Get the service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test') 

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'Hello World Here I come'
    },
    {
        'Id': '2',
        'MessageBody': 'MyQueueMessage',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Suresh',
                'DataType': 'String'
            }
        }
    }
])