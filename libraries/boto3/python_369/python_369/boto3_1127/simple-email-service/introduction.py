import boto3, configparser, pathlib


'''
The configparser class requires that ini files have headers
- Keys are case-insensitive and stored in lowercase
- Sections are case-sensitive
- The [DEFAULT] section is special to configparser
    - Values in this section take precedence if the same key is found in another section
'''


def get_sender_and_receiver():
    config = configparser.ConfigParser()
    path = (pathlib.Path(__file__).parent / 'secret' / 'emails.ini').resolve()
    config.read(pathlib.Path(path))
    return (config['verified senders']['1'], config['verified receivers']['1'])


def get_pubkey_seckey_region():
    config = configparser.ConfigParser()
    path = (pathlib.Path(__file__).parent / 'secret' / 'credentials').resolve()
    config.read(pathlib.Path(path))
    section = config['default']
    return (section['aws_access_key_id'], section['aws_secret_access_key'], section['region'])


def send_email_():
    '''
    This is the most basic form of an email that can be sent
    - If I'm getting AccessDenied errors, make sure my public key and private key are those of the proper user with the necessary SES access
    '''
    pub_key, sec_key, region = get_pubkey_seckey_region()
    client = boto3.client('ses', aws_access_key_id=pub_key, aws_secret_access_key=sec_key, region_name=region)
    sender, receiver = get_sender_and_receiver()
    email_content = {
        'Source': sender,
        'Destination': {
            'ToAddresses': [receiver]
        },
        'Message': {
            'Subject': {
                'Data': 'boto3 introduction email',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': 'Hello from boto3 Python tutorial!!!',
                    'Charset': 'UTF-8'
                },
            }
        }
    }
    #print('Success!')
    response = client.send_email(**email_content)
    # Success
    #{'MessageId': '0100016f2529c12a-9496d597-bc33-478e-b972-acbc6bdb496e-000000', 'ResponseMetadata': {'RequestId':
    #'e558c787-4614-420e-a5ad-1cd8641de9b4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e558c787-4614-420e-a5ad-1cd8641de9b4',
    #'content-type': 'text/xml', 'content-length': '326', 'date': 'Fri, 20 Dec 2019 21:14:51 GMT'}, 'RetryAttempts': 0}}
    # Failure
    # botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the SendEmail operation: User
    # `arn:aws:iam::996006054112:user/ecs-tutorial' is not authorized to perform `ses:SendEmail' on resource
    # `arn:aws:ses:us-east-1:996006054112:identity/uif93194@gmail.com'
    print(response)


if __name__ == '__main__':
    send_email_()