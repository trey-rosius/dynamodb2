from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_product(id,name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Products')

    try:
        response = table.delete_item(
            Key={
                'id': id,
                'name': name
            }
           
        )
    except ClientError as e:

       
        print(e.response['Error']['Message'])
        
    else:
        return response


if __name__ == '__main__':
  
    delete_response = delete_product(1001,"Laptops")
    if delete_response:
        print("Successfully deleted product")
        pprint(delete_response, sort_dicts=False)