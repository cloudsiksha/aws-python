import boto3
s3 = boto3.resource('s3')
myfile = s3.Object('suresh0302','s3.py').download_file('mycontent.py')