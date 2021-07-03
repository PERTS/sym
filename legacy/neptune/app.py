import sys
import os.path

subdirs = [
    ('app',),  # /app, python server code
    ('lib',),  # /lib, python libraries
    ('gae_server',),
    # include subdirectories, e.g. dir1/dir2, like this:
    #('dir1', 'dir2')
]

for path_parts in subdirs:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), *path_parts))

print('python path is:')
print(sys.path)

from local import local

print('Imported local root module:')
print(local)

from local_lib import local_lib

print('Imported local lib module:')
print(local_lib)

from gae import gae_const

print('Imported `gae`')
print(gae_const)
