#!/bin/bash

my_file=$1
my_bucket=$2
expiration_length=$3

aws s3 cp "$my_file" s3://"$my_bucket"/

presigned_url=$(aws s3 presign s3://"$my_bucket"/"$my_file" --expires-in "$expiration_length")

echo "$presigned_url"