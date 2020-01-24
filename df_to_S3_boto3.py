import boto3
from io import StringIO

def send_dataframe_to_S3(df, foldername, filename):

    #S3 file path including existing folder
    filenamepath = 'existing-folder-name/%s/%s.csv' % (foldername, filename)

    #S3 bucket
    bucketName = 'bucket-name' 
    print("WRITING", filename, "to S3 bucket path", filenamepath)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    client = boto3.client('s3')
    
    try:
        client.put_object(
              Body=csv_buffer.getvalue()
            , Bucket=bucketName
            , Key=filename)
        print("SUCCESSFUL WRITE to the S3 BUCKET")
        
    except Exception as e:
        print ("UNSUCCESSFUL write to S3 BUCKET ")
        print("ERROR:", e)


def main():
    send_dataframe_to_S3(df, foldername, filename)


if __name__ == '__main__':
    main()