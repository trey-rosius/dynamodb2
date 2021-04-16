from decimal import Decimal
from pprint import pprint
import boto3


def update_product(id,name,description, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    response = table.update_item(
        Key={
            'id': id,
            'name': name
        },
        UpdateExpression="set rating=:r, description=:p",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': description
            
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_product(
        1001,"Laptops","an updated description", 6.5)
    print("Product Successfully updated:")
    pprint(update_response, sort_dicts=False)