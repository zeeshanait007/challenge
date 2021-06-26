import sys
import json
from account.account import AccountValidator
from account.account_validator_constraint import AccountValCheck
from account.account_validator_first_row_constraint import AccountValFirstRowCheck
from transaction.transaction import TransactionValidator
from transaction.transaction_amount_checker import TransactionAmntCheck

class InputData(object):

    def __init__(self, account_json_array=[], trans_json={}, first_data_json=None):
        self.account_json_array = account_json_array
        self.trans_json = trans_json
        self.first_data_json = first_data_json

    def input_json_object(self):
        trans_json_array = []
        for i, line in enumerate(sys.stdin):
            if '' == line.rstrip():
                break
            if i == 0:
                self.first_data_json = json.loads(line)
            data = json.loads(line)

            if "account" in data:
                self.account_json_array.append(data["account"])
            if "transaction" in data:
                trans_json_array.append(data["transaction"])
        self.trans_json['transaction'] = trans_json_array
        self.trans_json['last_account'] = self.account_json_array[-1]
        return InputData(self.account_json_array, self.trans_json, self.first_data_json)
