import boto3
client = boto3.client('cloudwatch')

response = client.put_metric_alarm(\
    AlarmName='LowCPU',\
    AlarmDescription='Low CPU Alarm',\
    ActionsEnabled=True,\
    AlarmActions=[\
        'arn:aws:sns:us-west-2:033578524086:CPULow',\
    ],\
    MetricName='CPUUtilization',\
    Namespace='AWS/EC2',\
    Statistic='Average',\
    Dimensions=[\
        {\
            'Name': 'InstanceId',\
            'Value': 'i-5c2bca85'\
        },\
],\
    Period=300,\
    Unit='Percent',\
    EvaluationPeriods=1,\
    Threshold=70,\
    ComparisonOperator='LessThanThreshold'\
)