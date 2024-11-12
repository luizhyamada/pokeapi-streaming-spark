import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Uploads a file to an S3 bucket.

    :param file_name: Path to the file to upload
    :param bucket: Name of the bucket where the file will be stored
    :param object_name: Path of the file within the bucket (optional).
                        If not specified, the local file name will be used.
    :return: True if the upload was successful, False otherwise
    """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Upload successful: {file_name} -> s3://{bucket}/{object_name}")
        return True
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except NoCredentialsError:
        print("Error: Credentials not found.")
    except ClientError as e:
        print(f"Error uploading to S3: {e}")
    return False