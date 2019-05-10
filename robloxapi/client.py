from .utils.request import request
from .User import User
from .Group import Group
from .Trade import Trade
from .util.xcsrf import get_xcsrf as xcsrf
class client:
    def __init__(self, cookie=''):
        self.request_client = request(cookie)
        self.Group = Group(self.request_client)
        self.User = User(self.request_client)
        self.Trade = Trade(self.request_client)
    
    def get_xcsrf(self):
        return xcsrf()
