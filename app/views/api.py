from flask import (
    Blueprint, request, current_app
)
from app.extensions import create_s3

import traceback
import datetime
import json
import string
import random

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/get_presigned_url", methods=["GET"])
def get_presigned_url():
    try:
        bucket_name = current_app.config["AWS_BUCKET_NAME"]
        key = ''.join(random.choice(string.ascii_uppercase \
            + string.ascii_lowercase + string.digits) for _ in range(10))

        s3 = create_s3()    
        url = s3.generate_presigned_post(Bucket=bucket_name, Key=key, ExpiresIn=36000)
        return url

    except Exception as e:
        return e.__str__()

@api_blueprint.route("/post_file_details", methods=["POST"])
def post_file_details():
    try:
        uploaded_file = request.get_json()
        if not uploaded_file:
            uploaded_file = dict(request.form)

        file_name = uploaded_file.get("file_name", "N/A")
        file_size = uploaded_file.get("file_size", "N/A")
        file_upload_start = uploaded_file.get("start", "N/A")
        file_upload_complete = uploaded_file.get("finish", "N/A") 

        entry = "file_name : " + file_name + '\n' + "file_size : " + file_size +\
            ' B' + '\n' + "file_upload_start : " + file_upload_start + '\n' + "file_upload_complete : "\
                + file_upload_complete + '\n' + '**' * 20 + '\n' * 2


        with open("./logs/uploaded_files.log", "a") as log:
            log.write(entry)

        print(entry)
        return json.dumps(uploaded_file)

    except Exception as e:
        print(e.__str__())
        return e.__str__()