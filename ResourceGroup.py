import boto3
import json
import time
from inspect import getmembers
from optparse import OptionParser
import sys
from botocore.config import Config


import boto3
# All the region except Bahrain(me-south-1). If you have that region enabled, feel free to add that below.
regions=['eu-west-3' ,'eu-west-2' ,'eu-west-1' ,'ap-northeast-3' , 'ap-northeast-2','ap-northeast-1', 'sa-east-1', 'ca-central-1',  'ap-east-1', 'ap-southeast-1',  'ap-southeast-2',  'eu-central-1', 'us-east-1',  'us-east-2', 'us-west-1', 'us-west-2','sa-east-1','eu-north-1','af-south-1','ap-south-1'
]

for i in regions:
    print("Here are all the resource from "+ i+" region")
    my_config = Config(region_name = i)
    client = boto3.client('resourcegroupstaggingapi',config= my_config)
    #print(client)
    paginator = client.get_paginator('get_resources')
    Resources = paginator.paginate()
    #print(Resources)
    for Listofallresources in Resources:
        Mapping=Listofallresources['ResourceTagMappingList']
        for resourcelist in Mapping:
            print(resourcelist['ResourceARN'])
        print("\n")
