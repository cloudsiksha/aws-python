import boto
conn = EC2Connection()
group_name  = 'CloudSiksha'
description = 'CloudSiksha: Test Security Group.'
 
group = conn.create_security_group(
    group_name, description
)
 
group.authorize('tcp', 8888,8888, '<a href="http://0.0.0.0/0">0.0.0.0/0</a>')
import random
from string import ascii_lowercase as letters
 
# Create the random data in the right format
data = random.choice(('UK', 'US'))
for a in range(4):
    data += '|'
    for b in range(8):
        data += random.choice(letters)
import hashlib
 
# Your chosen password goes here
password = 'password'
 
h = hashlib.new('sha1')
salt = ('%0' + str(12) + 'x') % random.getrandbits(48)
h.update(password + salt)
 
password = ':'.join(('sha1', salt, h.hexdigest()))

data += '|' + password

# NotebookCloud AMI
AMI = 'ami-affe51c6'
 
conn.run_instances(
    AMI,
    instance_type = 't1.micro',
    security_groups = ['python_central'],
    user_data = data,
    max_count = 1
)

import time
 
while True:
    inst = [
        i for r in conn.get_all_instances()
        for i in r.instances
    ][0]
 
dns = inst.__dict__['public_dns_name']
 
if dns:
    # We want this instance id for later
    instance_id = i.__dict__['id']
    break
 
time.sleep(5)

print('https://{}:8888'.format(dns))