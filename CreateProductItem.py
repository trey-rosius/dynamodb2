from pprint import pprint
import boto3
from decimal import Decimal

def put_product(id, name,description, price,rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')
    response = table.put_item(
       Item={
            'id': id,
            'name': name,
            'description':description,
            'price': Decimal(price),
            'rating':Decimal(rating)
        }
    )
    return response


if __name__ == '__main__':
    product_response = put_product(1001,"Laptops",
                           "Any good description", "25.9", "4.5")
    print("Put product succeeded:")
    pprint(product_response, sort_dicts=False)