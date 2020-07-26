#!c:\users\k1526\downloads\helpinghands\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bower.py==1.0','console_scripts','bower.py'
__requires__ = 'bower.py==1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bower.py==1.0', 'console_scripts', 'bower.py')()
    )
