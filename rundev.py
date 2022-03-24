import os
import sys

py_cmd = 'python3' if 'linux' in sys.platform else 'python'

script = f"""
npm run postcss-dev
{py_cmd} manage.py runserver
"""

for line in script.splitlines():
    os.system(line)