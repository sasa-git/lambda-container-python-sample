from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def handler(event, context):
  print(f"CUSTOM_ENV: {os.getenv('CUSTOM_ENV')}")

  file_path = f'/tmp/sample.txt'

  with open(file_path, 'w') as f:
    f.write("hello, SRE Sunday!")

  with open(file_path) as f:
    s = f.read()

  print(s)

  return event
