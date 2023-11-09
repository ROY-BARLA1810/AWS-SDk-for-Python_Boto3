import boto3

s3_client = boto3.client('s3', 
                      aws_access_key_id='AKIA4CH3B3CMSLHFL5AP', 
                      aws_secret_access_key='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',
                      region_name="us-east-1"
)

#creation of bucket

response = s3_client.create_bucket(
    Bucket='pranovboto3testbucket',
)

print (response)


#s3 put object 

response = s3_client.put_object(
     Bucket='pranovboto3testbucket',
     Key='roy',
    
)

print (response)