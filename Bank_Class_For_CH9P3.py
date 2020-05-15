import pickle
from account import Account
class Bank(object):
    def __init__(self, fileName = None):
        self._accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except(EOFError):
                    fileObj.close()
                    break
    def __str__(self):
        lyst = list(self._accounts.values())
        lyst.sort()
        return '\n'.join(map(str, lyst))
    def make_key(self, name, pin):
        return "%s/%s" %(name, pin)
    def add(self, account):
        key = self.make_key(account.get_name(), account.get_pin())
        self._accounts[key] = account
    def remove(self, name, pin):
        key = self.make_key(name, pin)
        return self._accounts.pop(key, None)
    def get(self, name, pin):
        key = self.make_key(name, pin)
        return self._accounts.get(key, None)
    def compute_interest(self):
        total = 0.0
        for account in self._accounts.values():
            total += account.compute_interest()
        return total
    def save(self, fileName = None):
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self._accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
