from .base import *
from decouple import config

if config('DEBUG', cast=bool):
    from .local import *
else:
    from .production import *
