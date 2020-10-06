from flask import current_app
from boto3 import Session

def create_s3():
    
    access_key = current_app.config["AWS_ACCESS_KEY"]
    secret_key = current_app.config["AWS_SECRET_KEY"]
    region_name = current_app.config["AWS_REGION_NAME"]

    ses = Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region_name
        )

    return ses.client('s3')