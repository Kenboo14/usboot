import asyncio
import shlex
import socket
from typing import Tuple

import dotenv
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError


HAPP = None
