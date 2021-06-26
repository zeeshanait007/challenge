from account.account import AccountValidator
from account.account_validator_constraint import AccountValCheck
from account.account_validator_first_row_constraint import AccountValFirstRowCheck
from transaction.transaction import TransactionValidator
from transaction.transaction_amount_checker import TransactionAmntCheck
from input.input_data import InputData
from transaction.transaction_per_2mins_checker import Transaction2MinsCheck
if __name__ == "__main__":

    inp = InputData()
    obj = inp.input_json_object()
    print('first_data', obj.first_data_json)
    print('account_json', obj.account_json_array)
    print('trans_json', obj.trans_json)

    #
    # is_input_good = AccountValidator(AccountValFirstRowCheck, obj).execute_validator()
    # is_account_active = AccountValidator(AccountValCheck, obj).execute_validator()
    #
    # print("is_input_good", is_input_good.actual)
    # print("is_input_v", is_input_good.violation)
    # print("is_input_s", is_input_good.status)
    #
    # print("---------------------------------------")
    # print("is_account_active", is_account_active.actual)
    # print("is_account_v", is_account_active.violation)
    # print("is_account_s", is_account_active.status)
    #
    #
    # is_transaction_good = TransactionValidator(TransactionAmntCheck, obj.trans_json).execute_validator()
    #
    # print("is_transaction_success", is_transaction_good.actual)
    # print("is_transaction_good_v", is_transaction_good.violation)
    # print("is_transaction_good_s", is_transaction_good.status)


    is_transaction_good = TransactionValidator(Transaction2MinsCheck, obj.trans_json).execute_validator()

    print("is_transaction_success", is_transaction_good.actual)
    print("is_transaction_good_v", is_transaction_good.violation)
    print("is_transaction_good_s", is_transaction_good.status)
    #is_account_active = AccountValidator(AccountValCheck, obj.trans_json).execute_validator()
