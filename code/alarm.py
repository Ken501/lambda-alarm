import os
import boto3
import datetime

# Variables

topic = os.environ["SNS_ARN"]
role = os.environ["ROLE_ARN"]
link = os.environ["LINK"]
emailBody = "{} it's your turn this week!\n\nFollow the link to update call forwarding: {}.\n\nEnsure it is done before end of day. \n\n\n\nRotation information: \nuser: {} \nindex_value = {}\nemail: {} \nTimestamp: {}"
emailSubject = "Team Weekly Shift Change reminder"
currentDate = datetime.datetime.now()

# Update index value function

def update_index(x):
    x = int(x)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alarm-table')
    response = table.update_item(
                Key={
                    'index': 0,
                    'turn': 0
                },
                UpdateExpression='SET index_value = :val',
                ExpressionAttributeValues={
                    ':val': x
                }
            )

def add_user():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alarm-table')
    table.put_item(
      Item={
            'index': 4,
            'turn': 4,
            'user': '',
            'email': ''
        },
        # ReturnValues='UPDATED_NEW'
        
    )
    
# get index value function

def get_index():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alarm-table')
    response = table.get_item(
      Key={
            'index': 0,
            'turn': 0
        },
        ProjectionExpression='index_value'
    )
    item = response['Item']
    return item
    
# get user function

def get_user(x):
    x = int(x)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alarm-table')
    response = table.get_item(
      Key={
            'index': x,
            'turn': x
        },
        # ProjectionExpression='user'
    )
    user = response['Item']
    return user
    
# get email function

def get_email(x):
    x = int(x)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('alarm-table')
    response = table.get_item(
      Key={
            'index': x,
            'turn': x
        },
        ProjectionExpression='email'
    )
    email = response['Item']
    return email
    

# # Send sns function

def send_sns(message, subject):
    sns = boto3.client("sns")
    topic_arn = topic
    sns.publish(
        TopicArn=topic_arn, Message=message, Subject=subject)

# Lambda handler

def lambda_handler(event, context):
    
    # Retrive index value
    indexValue = get_index()
    indexValue = indexValue.get('index_value')
    
    # Get user
    user = get_user(indexValue)
    user = user.get('user')
    
    # Get email
    email = get_email(indexValue)
    email = email.get('email')
    
    # Send Message
    message = emailBody.format(user, link, user, indexValue, email, currentDate)
    subject = emailSubject
    send_sns(message, subject)
    
    # Update index value
    if indexValue == 3:
        indexValue = 1
    else:
        indexValue += 1
    update_index(indexValue)