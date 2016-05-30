import boto3

s3 = boto3.resource('s3')

s3.Object('suresh0302', 's3.py').put(Body=open('s3.py','rb'))
