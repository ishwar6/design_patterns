import boto3
import random
import datetime
import pymysql

def generate_otp():
    return random.randint(100000, 999999)

def store_otp_in_db(member_id, otp, connection):
    with connection.cursor() as cursor:
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=5)  # OTP expires in 5 minutes
        sql = "INSERT INTO otp_table (member_id, otp, expiration_time) VALUES (%s, %s, %s)"
        cursor.execute(sql, (member_id, otp, expiration_time))
        connection.commit()

def send_email_via_ses(recipient_email, otp):
    client = boto3.client('ses')
    subject = 'Your OTP'
    body = f'Your OTP is: {otp}'
    client.send_email(
        Source='your-email@example.com',
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

def lambda_handler(event, context):
    member_id = event['member_id']
    recipient_email = event['email']
    otp = generate_otp()

    
    connection = pymysql.connect(host='rds-endpoint',
                                 user='user',
                                 password='98a7sd9f79sdf',
                                 db='otp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

  
    store_otp_in_db(member_id, otp, connection)
 
    send_email_via_ses(recipient_email, otp)

    return {
        'statusCode': 200,
        'body': 'OTP sent successfully'
    }
