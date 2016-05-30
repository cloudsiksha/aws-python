import boto3
s3 = boto3.resource('s3')
s3.Object('mybucket', 'hello.txt').upload_file('/tmp/hello.txt')