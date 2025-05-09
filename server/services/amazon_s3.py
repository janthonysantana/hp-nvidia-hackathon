import os
import boto3
from botocore.exceptions import NoCredentialsError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AmazonS3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.bucket_name = os.getenv('AWS_S3_BUCKET_NAME')

    def upload_file(self, file, object_name):
        """Uploads a file to the S3 bucket."""
        try:
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                object_name,
                
            )
            s3_url = f"https://{self.bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{object_name}"
            logger.info(f"File uploaded successfully to {s3_url}")
            return s3_url
        except NoCredentialsError:
            logger.error("AWS credentials not available.")
            raise
        except Exception as e:
            logger.error(f"Error uploading file to S3: {str(e)}")
            raise
