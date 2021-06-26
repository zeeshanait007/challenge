from account.account import Account
from common.common import CommonObject

class AccountValCheck(Account):

    def __init__(self):
        pass

    def execute(self, input_obj):
        violation = []
        actual = []
        status = []
        for data in input_obj.account_json:
            if not bool(data["active-card"]):
                violation.append([])
                status.append('Account Not Valid')
            else:
                violation.append([])
                status.append(None)
        return CommonObject(input_obj.account_json, violation, status)

