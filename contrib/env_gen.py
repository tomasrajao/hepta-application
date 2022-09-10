"""
Python SECRET_KEY generator.
"""
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()

CONFIG_STRING = f"""SECRET_KEY={secret_key}
DEBUG=True
DATABASE_URL=postgres://root:root@localhost:5434/todo_database"""

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')
