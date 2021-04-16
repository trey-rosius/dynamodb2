from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_product(id, name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    try:
        response = table.get_item(Key={'id': id, 'name': name})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    product = get_product(1001,"Laptops")
    if product:
        print("Successfully got the product:")
        pprint(product, sort_dicts=False)