import boto3
from datetime import datetime
client = boto3.client('cloudwatch')

response = client.put_metric_data(\
    Namespace='Mem',\
    MetricData=[\
        {\
            'MetricName': 'Memory',\
            'Dimensions': [\
                {
                    'Name': 'InstanceId',\
                    'Value': 'i-5c2bca85'\
                },\
            ],\
            'Timestamp': datetime(2016,5,20,00,00,00),\
            'Value': 60,\
            'Unit': 'Percent'\
       },\
	   {\
            'MetricName': 'Memory',\
            'Dimensions': [\
                {
                    'Name': 'InstanceId',\
                    'Value': 'i-5c2bca85'\
                },\
            ],\
            'Timestamp': datetime(2016,5,20,00,10,00),\
            'Value': 70,\
            'Unit': 'Percent'\
       },\
	   {\
            'MetricName': 'Memory',\
            'Dimensions': [\
                {
                    'Name': 'InstanceId',\
                    'Value': 'i-5c2bca85'\
                },\
            ],\
            'Timestamp': datetime(2016,5,20,00,20,00),\
            'Value': 40,\
            'Unit': 'Percent'\
       },\
	   {\
            'MetricName': 'Memory',\
            'Dimensions': [\
                {
                    'Name': 'InstanceId',\
                    'Value': 'i-5c2bca85'\
                },\
            ],\
            'Timestamp': datetime(2016,5,20,00,30,00),\
            'Value': 50,\
            'Unit': 'Percent'\
       },\
	   {\
            'MetricName': 'Memory',\
            'Dimensions': [\
                {
                    'Name': 'InstanceId',\
                    'Value': 'i-5c2bca85'\
                },\
            ],\
            'Timestamp': datetime(2016,5,20,00,40,00),\
            'Value': 70,\
            'Unit': 'Percent'\
       },\
    ]\
)\