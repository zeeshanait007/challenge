from account.account import Account
from common.common import CommonObject

class AccountValFirstRowCheck(Account):

    def __init__(self):
        pass

    def execute(self, input_obj):
        violation = []
        actual = []
        status = []
        if "account" in input_obj.first_data_json:
            actual.append(input_obj.first_data_json)
            status.append("Correct Data")
        else:
            actual.append({})
            violation = ["Account Not Initialized"]
            status.append(None)

        return CommonObject(actual, violation, status)
