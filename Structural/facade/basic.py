import boto3
import random
import datetime
import pymysql

class OtpGenerator:
    @staticmethod
    def generate_otp():
        return random.randint(100000, 999999)

class DatabaseManager:
    def __init__(self, connection):
        self.connection = connection

    def store_otp(self, member_id, otp):
        with self.connection.cursor() as cursor:
            expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
            sql = "INSERT INTO otp_table (member_id, otp, expiration_time) VALUES (%s, %s, %s)"
            cursor.execute(sql, (member_id, otp, expiration_time))
            self.connection.commit()

class EmailService:
    @staticmethod
    def send_email(recipient_email, otp):
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

class OtpFacade:
    def __init__(self, db_connection):
        self.db_manager = DatabaseManager(db_connection)
        self.email_service = EmailService()

    def generate_and_send_otp(self, member_id, email):
        otp = OtpGenerator.generate_otp()
        self.db_manager.store_otp(member_id, otp)
        self.email_service.send_email(email, otp)

def lambda_handler(event, context):
    member_id = event['member_id']
    recipient_email = event['email']

    connection = pymysql.connect(host='rds-endpoint',
                                 user='user',
                                 password='a7s9df79@s97df',
                                 db='otp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    otp_facade = OtpFacade(connection)
    otp_facade.generate_and_send_otp(member_id, recipient_email)

    return {
        'statusCode': 200,
        'body': 'OTP sent successfully'
    }
