import boto3

ACCESS_KEY = '5f9edb1571b5d7218e01afe54b2e2fc2'
SECRET_KEY = '2da0beb0d907bfdd6632a62579a2f1f18b614be4b45be80db72f4e397763d940'
ENDPOINT = "https://44a79af9cc0653dd26cc14c1be388cfb.r2.cloudflarestorage.com"
REGION_NAME = 'EEUR'

PUBLIC_URL = "https://pub-a4accecc8bf54ac684cd697117910cf9.r2.dev"
BUCKET_NAME = 'group04092025'

s3client = boto3.client(
    service_name='s3',
    region_name=REGION_NAME,
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)


target_file_name = "Downloads/spring123.jpeg"
result = s3client.upload_file("spring123.jpeg", BUCKET_NAME, target_file_name)
print(result)


