import boto3
import json
import os


bucketname = 'interface-log'

session = boto3.Session(
    profile_name='ec-dev'
)

def check_json_inS3():
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucketname)
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        # print(body)
        try:
            json.loads(body)
        except json.JSONDecodeError:
            # print(obj)
            # print(key)
            # To merge Non-Json format log files to One Log file
            with open('no_json_interface_logs', 'ab') as file:
                file.write(body)
            # print(os.path.dirname(key))
            # try:
            #     chk_s3 = boto3.client('s3')
            #     chk_s3.download_file(bucketname, key, key)
            # except FileNotFoundError:
            #     Downloads non-json format objects
            #     make_dir(os.path.dirname(key))
            #     chk_s3.download_file(bucketname, key, key)
            
            
            #     Delete objects with non-json format
            #     del_obj = s3.Object(bucketname, key)
            #     del_obj.delete()
            
                
            
def make_dir(obj):
        if not os.path.exists(obj):
            os.mkdir(obj)

            
check_json_inS3()