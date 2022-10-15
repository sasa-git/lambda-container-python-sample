from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def handler(event, context):
  print(f"CUSTOM_ENV: {os.getenv('CUSTOM_ENV')}")

  return event
