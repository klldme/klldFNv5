import asyncio
import os
import sys

env_vars = {}
if os.path.isfile('.device'):
    with open('.device') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.replace("\"", "")
else:
  print("error device in the file")
  sys.exit()

os.system('pip install klldv5')
os.system('clear')

import klldv5

client = klldv5.klldv5(
  device_id=env_vars['DEVICE_ID'],
  account_id=env_vars['ACCOUNT_ID'],
  secret=env_vars['SECRET']
)
