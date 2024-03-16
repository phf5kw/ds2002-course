import boto3
from urllib.request import urlretrieve
import requests
  
# Retrieving the resource located at the URL 
# and storing it in the file name a.png 
url = "https://static.wikia.nocookie.net/prettycure/images/0/05/Cure_sunny_finish.jpg"
# urlretrieve(url, "akane.png") 
r = requests.get(url, allow_redirects=True)

open('akane.jpg', 'wb').write(r.content)

# create client
s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2002-phf5kw'
local_file = 'akane.jpg'

bucket_name = 'ds2002-phf5kw'
object_name = 'akane.jpg'
expires_in = 604800

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read'
)

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(response)

# IMAGE URL
# https://ds2002-phf5kw.s3.amazonaws.com/akane.jpg?AWSAccessKeyId=ASIAYS2NU4KKNH2DEPTU&Signature=FkZBvncB4EpJGkoiIuJ%2Fw%2Bt6JlY%3D&x-amz-security-token=FwoGZXIvYXdzEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGseYFK9vPusSswyISLEASeLWnhdzokVLST%2FsMAEbeB4jFlUhpZlVo0FeEeeoaUgs%2BhWLieVIKCso%2FJvIUldTfmhZqOxJOe4jPaF%2BedxUQXXgwSqtnWFeyfIFOuAbc95uRPjj0OmwAMRmXmhVIbsjGBFInLdV8dhKA7iRi7P%2Fvh1Lon35Rs8I5ZZ12IotB0sCRaNZPPsdgVs9QKClVHhHAmvU5gZWUG3N6pJHnTequpMT4Xq%2BEvVrFug%2Fd2pKbWJ5Lk7DFkpg3mneK8secPOjKUxoC4oguPTrwYyLUam2WIudIG%2BclJnFDVPJ9InR%2BO83qhoEKSadpVGOAR3rd%2F4tN29pvAUOXHveg%3D%3D&Expires=1711167161
