# fileUpload

### Installation


```sh
$ git clone https://github.com/rajeshagashe/fileUpload.git
$ cd fileUpload
$ pipenv shell
$ pipenv install -r requirements.txt
$ mv env.example .env
Update AWS credentials and bucket name in .env
$ export FLASK_APP=app

```

### Run

```sh
$ flask run
```

### End-Points

1. /file_upload/get_presigned_url
    (generates and return presigned url to upload files to the s3 bucket.)
    method - GET  
  
2. /file_upload/post_file_details    
    method - POST
    (logs data to terminal and ./logs/uploaded_files.log)  
    body - 
    ``` json
    {  
        "file_name" : file_name,
        "file_size" : file_size,
        "start" : start,
        "finish" : finish
    }  
    ```