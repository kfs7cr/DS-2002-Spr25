#!/home/codespace/.python/current/bin/python3

import boto3
import requests
import os
import logging
from botocore.exceptions import ClientError

# from "Download a file using the requests library" Neal Magee
def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

# from Presigned URLs Boto3
def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name, 'ResponseContentDisposition': 'inline',
        'ResponseContentType': 'image/gif'},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

image_url = "https://media.tenor.com/k0BIyQU8ye0AAAAM/chiikawa-hachieware.gif"
file = "hachiware.gif"
path = os.path.join(os.getcwd(), file) # Saves to current directory
bucket_name = "ds2002-kfs7cr"
object_name = file
expiration_time = 3600

download_file(image_url, path)

with open(path, 'rb') as f:
    s3 = boto3.client('s3')
    resp = s3.put_object(
        Body=f,
        Bucket=bucket_name,
        Key=object_name
    )

url = create_presigned_url(bucket_name, object_name, expiration_time)
print(url)