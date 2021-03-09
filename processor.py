import uploader 
import PIL
import boto3

#image is now iside an aws bucket.All we need to do now is to make textract to use that image and give output.

s3BucketName = "riskybucket69"
documentName = "casheet.jpg"

#create textract client
textract = boto3.client('textract')

#call textract to work here
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })

#printing detected text

for x in response["Blocks"]:
    if x["BlockType"]=="LINE":
        print ('\033[94m' +  x["Text"])
        




