#!/bin/bash

curl https://static.wikia.nocookie.net/prettycure/images/6/65/PopProfileImage.jpg/revision/latest?cb=20120312105358 > pop.jpg

aws s3 cp pop.jpg s3://ds2002-phf5kw/

aws s3 presign --expires-in 604800 s3://ds2002-phf5kw/pop.jpg

# Image URL
# https://ds2002-phf5kw.s3.us-east-1.amazonaws.com/pop.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYS2NU4KKNH2DEPTU%2F20240316%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240316T015001Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGseYFK9vPusSswyISLEASeLWnhdzokVLST%2FsMAEbeB4jFlUhpZlVo0FeEeeoaUgs%2BhWLieVIKCso%2FJvIUldTfmhZqOxJOe4jPaF%2BedxUQXXgwSqtnWFeyfIFOuAbc95uRPjj0OmwAMRmXmhVIbsjGBFInLdV8dhKA7iRi7P%2Fvh1Lon35Rs8I5ZZ12IotB0sCRaNZPPsdgVs9QKClVHhHAmvU5gZWUG3N6pJHnTequpMT4Xq%2BEvVrFug%2Fd2pKbWJ5Lk7DFkpg3mneK8secPOjKUxoC4oguPTrwYyLUam2WIudIG%2BclJnFDVPJ9InR%2BO83qhoEKSadpVGOAR3rd%2F4tN29pvAUOXHveg%3D%3D&X-Amz-Signature=d977678b11f28009689348bb8222e1452167d8adebecdd72acdc601a036ce690
