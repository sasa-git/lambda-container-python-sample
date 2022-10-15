from os.path import join, dirname
from dotenv import load_dotenv
import os
import json
from aws_lambda_powertools import Logger

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

logger = Logger(level='INFO', service='sample-lambda')

def handler(event, context):
  logger.info(event)

  return {
    'statusCode': 200,
    'headers': {"Content-Type": "application/json"},
    'body': json.dumps(event),
    'isBase64Encoded': False
  }
