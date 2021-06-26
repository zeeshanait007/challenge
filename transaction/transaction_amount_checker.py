from transaction.transaction import Transaction
from common.common import CommonObject


class TransactionAmntCheck(Transaction):

    def __init__(self):
        pass

    def execute(self, trans_data_json):
        violation = []
        transaction = []
        status = []
        if not bool(trans_data_json['last_account']['active-card']):
            transaction.append(trans_data_json['transaction'][0])
            violation.append("account-not-initialized")
            status.append("account-not-initialized")
            return CommonObject(transaction, violation, status)

        for trans in trans_data_json['transaction']:

            if trans_data_json['last_account']['available-limit'] < trans["amount"]:
                transaction.append(trans)
                violation.append("insufficient-limit")
                status.append("insufficient-limit")
                return CommonObject(transaction, violation, status)

            actual_amount = trans_data_json['last_account']['available-limit']
            after_trans_amount = actual_amount-trans["amount"]
            trans['amount'] = after_trans_amount
            transaction.append(trans)
            violation.append([])
            status.append("transaction-done")
            trans_data_json['last_account']['available-limit'] = after_trans_amount

        return CommonObject(transaction, violation, status)

