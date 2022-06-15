#import from aws library
import boto3

#region specified
region = "eu-west-2"

#aws console up and runnunig
session =  boto3.Session()

#available resource from aws account
available_resources = session.get_available_resources()
print(available_resources)

print("list of available resources from my aws account" )
for resource in available_resources:
    print(resource)