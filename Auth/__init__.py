from .authenticate import login
from .authorize import give_access

# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
    'give_access',
    'login',
]