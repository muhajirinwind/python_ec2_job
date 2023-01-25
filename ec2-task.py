import boto3

action = "OFF"
ec2_resource=boto3.resource('ec2', region_name='us-west-2')

instances = ec2_resource.instances.filter(
    Filters = [{'Name': 'tag:Environment', 'Values':['dev']}])

if action == 'OFF':
     for instance in instances:
        try:
            instance.stop()
            print(f'{instance} stopped')
        except:
            print(f'Error stopping {instance}')
else:
    for instance in instances:
        try:
            instance.start()
            print(f'{instance} Started')
        except:
            print(f'Error Starting {instance}')