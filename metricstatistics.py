import boto3
from datetime import datetime
client = boto3.client('cloudwatch')

response = client.get_metric_statistics(\
    Namespace='AWS/EC2',\
    MetricName='CPUUtilization',\
    Dimensions=[\
        {\
            'Name': 'InstanceId',\
            'Value': 'i-4e539888'\
        },\
    ],\
    StartTime=datetime(2016,5,20,00,00,00),\
    EndTime=datetime(2016,5,20,8,30,00),\
    Period=600,\
    Statistics=[\
        'Average',\
    ]\
)
print(response['Datapoints'])