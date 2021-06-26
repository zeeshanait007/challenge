from transaction.transaction import Transaction
from common.common import CommonObject
import datetime
import pandas as pd

class Transaction2MinsCheck(Transaction):

    def __init__(self):
        pass

    def execute(self, trans_data_json):
        violation = []
        actual = []
        status = []
        merchant_list = []
        sum_time_diff = 0
        for i, trans in enumerate(trans_data_json['transaction']):
            if i == 0:
                prev = trans['time']
                prev_time = datetime.datetime.strptime(prev, '%Y-%m-%dT%H:%M:%S.%fZ')
            cur_time = datetime.datetime.strptime(trans['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
            time_diff = cur_time - prev_time
            second_diff=time_diff.seconds
            sum_time_diff += second_diff
            if sum_time_diff > 120:
                actual.append(trans_data_json['transaction'])
                violation.apppend("high-frequency-small-interval")
                status.append("exit")
                return CommonObject(actual, violation, status)

            if sum_time_diff < 120:
                merchant_list.append({"merchant": trans["merchant"], "amount": trans["amount"]})

        trans_list_df=pd.DataFrame(merchant_list)
        trans_list_df_unique = pd.DataFrame(trans_list_df).drop_duplicates().to_dict('records')
        if trans_list_df.shape[0] != trans_list_df_unique.shape[0]:
            actual.append(trans_data_json['transaction'])
            violation.apppend("doubled-transaction")
            status.append("doubled-transaction")
            return CommonObject(actual, violation, status)

        return CommonObject(actual, violation, "Success")
