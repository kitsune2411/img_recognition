import csv
import boto3

with open('credential.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[0]
        secret_access_key = line[1]

photo = 'hot_air_baloon.jpg'

client = boto3.client('rekognition',
                      region_name = 'ap-southeast-1',
                      aws_access_key_id = access_key_id,
                      aws_secret_access_key = secret_access_key)

with open(photo, 'rb') as source_img:
    source_bytes = source_img.read()

response = client.detect_labels(Image={'Bytes' : source_bytes},
                                MaxLabels=2)

print(response)


