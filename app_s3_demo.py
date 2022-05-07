import aws_cdk as cdk
from aws_cdk.aws_s3 import Bucket

app = cdk.App()
stack = cdk.Stack(app, "test")

Bucket(stack, "TestBucket")

app.synth()
