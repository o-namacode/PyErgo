import os
from .fileutils import safedir


PYERGO__LIBRARY_BASEDIR = safedir(os.path.join(os.path.expanduser("~"), ".pyergo"))

PYERGO__LIBRARY_USERSFILE_DIR = safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, "users"))
PYERGO__LIBRARY_USERS_FILE_EXT = ".umf"
PYERGO__LIBRARY_USERS_DATASTORE_DIR = safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, "__usersstore__"))