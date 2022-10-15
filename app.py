import subprocess
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

def handler(event, context):
  print(f"CUSTOM_ENV: {os.getenv('CUSTOM_ENV')}")

# eks 上のクラスタにアクセスする
  eks_cluster_name = 'sample-cluster'
  subprocess.run(['aws', 'eks', '--region', 'ap-northeast-1', 'update-kubeconfig', '--name', eks_cluster_name, '--kubeconfig', '/tmp/kubeconfig'], text=True)
  subprocess.run(['kubectl', 'get', 'node', '--kubeconfig', '/tmp/kubeconfig'], text=True)

  return event
