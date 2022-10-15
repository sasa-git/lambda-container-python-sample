from os.path import join, dirname
from dotenv import load_dotenv
import os
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def handler(event, context):
  print(os.environ)

  return {
    'statusCode': 200,
    'headers': {"Content-Type": "application/json"},
    'body': json.dumps(event),
    'isBase64Encoded': False
  }
