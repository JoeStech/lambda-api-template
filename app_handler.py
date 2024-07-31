import psycopg2
import json

def handler(event, context):
    print(event)
    if request_method == 'POST':
        body = event.get('body')
    elif request_method == 'GET':
        query_params = event.get('queryStringParameters')

    return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json',
            },
            'body': '{"status":"test success"}'
    
    
if __name__ == "__main__":
    # FOR LOCAL TESTING ONLY
    event = {'httpMethod': 'GET', 'queryStringParameters': 'none'}
    print(handler(event,{}))