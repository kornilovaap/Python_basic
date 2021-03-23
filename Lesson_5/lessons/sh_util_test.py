import shutil
import sys

shutil.copyfile('person.json', 'test.dir/person.json')

shutil.rmtree('test.dir')

# sys.stdin  # standart input
# sys.stdout  # standart output
# sys.stderr  # standart output error

sys.exit(0)
       