"""
Would need to install boto3, aws cli, aws
"""
import boto3

ec2=boto3.resource('ec2')

# Creating an instance via scripting

instance= ec2.create_instances(
    ImageID='ami-23452857',
    MinCount=1,
    MaxCount=4,
    InstanceType='t2.micro'
)
print(instance[0].id)


# Terminating an instance via scripting

# instanceID=instance[0].id
# instance=ec2.Instance(instance_id)
# responce=instance.terminate()
# print(response)