"""
Would need to install boto3, aws cli, aws configure
upon configuring aws, you would need to create a new user and download the user's details which contains access key etc.
Make sure that the new user has the admin access of whichever service is required.
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

instanceID=instance[0].id
instance=ec2.Instance(instance_id)
responce=instance.terminate()
print(response)

# Creating S3 bucket via scripting

s3=boto3.resource('s3')
bucket_name='azrambucket'
try:
    response=s3.create_bucket(Bucket=bucket_name, CreatingBucketConfiguration={'LocationConstraint' : 'us-east-2'})
    print(response)

except Exception as error
    print(error)