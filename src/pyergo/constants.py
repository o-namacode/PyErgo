import os
from .fileutils import safedir


PYERGO__LIBRARY_BASEDIR = safedir(os.path.join(os.path.expanduser("~"), ".pyergo"))
def pyergo_lib__project_basedir(project_dir : str):
    return safedir(os.path.join(os.path.expanduser("~"), project_dir))


PYERGO__LIBRARY_USERSFILE_DIR = safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, "users"))
def pyergo_lib__usersfile_dir(project_dir : str):
    return safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, project_dir, "users"))

PYERGO__LIBRARY_USERS_FILE_EXT = ".umf"
PYERGO__LIBRARY_USERS_DATASTORE_DIR = safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, "__usersstore__"))
def pyergo_lib__users_datastore_dir (project_dir : str):
    return safedir(os.path.join(PYERGO__LIBRARY_BASEDIR, project_dir, "__usersstore__"))


