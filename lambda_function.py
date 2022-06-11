import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('STUDENT')

def lambda_handler(event, context):
    # TODO implement
    table.put_item(Item=event)
    return {
        'Code': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://www.example.com',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': 'successfull!'
    }
