import boto3

# Get the service resource
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test') 

queue.delete()