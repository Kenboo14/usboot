from glob import glob
from os.path import basename, dirname, isfile

from config import *
from BdrlMusic import *
from BdrlMusic.Helpers import *
from BdrlMusic.utils import *

def loadModule():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )
