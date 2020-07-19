import json, boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table('VisitCounter')


def lambda_handler(event, context):
    response=table.update_item(
        Key={"siteURL":"https://bencharlot.com/"},
        UpdateExpression = 'SET visitcount = visitcount + :incr',
        ExpressionAttributeValues ={ ':incr' : 1},


    )
    responseget = table.get_item(
        Key={"siteURL":"https://bencharlot.com/"},
        ProjectionExpression ='visitcount'
    )
    item = responseget['Item']


    return item
