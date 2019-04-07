

import sys
import pathlib

# If we are running from a wheel, add the wheel to sys.path
# This allows the usage python rxbuilder *
if __package__ == '':
    # first dirname call strips of '/__main__.py', second strips off '/pip'
    # Resulting path is the name of the wheel itself
    # Add that to sys.path so we can import pip
    path = pathlib.Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(path))
    #from rxbuilder import CmdWindows

else:
    from . import CmdWindows

if __name__ == '__main__':
    sys.exit(CmdWindows())