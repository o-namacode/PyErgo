# python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
# python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"


#
#    clearpycache
#
from pathlib import Path
from argparse import ArgumentParser

def clearpycache ():
    argparser = ArgumentParser()

    argparser.add_argument('dir', default='.')

    args = argparser.parse_args()

    cwdir = Path(args.dir)



    files = cwdir.rglob('*.py[co]')
    dirs = cwdir.rglob('__pycache__')

    for fpath in files:
        fpath.unlink(True)
    
    for dpath in dirs:
        dpath.rmdir()