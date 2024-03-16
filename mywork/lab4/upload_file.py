import boto3
import urllib.request 
  
# Retrieving the resource located at the URL 
# and storing it in the file name a.png 
url = "https://static.wikia.nocookie.net/prettycure/images/0/05/Cure_sunny_finish.jpg/revision/latest?cb=20190103091727"
urllib.request.urlretrieve(url, "akane.png") 

# create client
s3 = boto3.client('s3', region_name="us-east-1")

bucket_name = 'ds2002-phf5kw'
object_name = 'akane.jpg'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )