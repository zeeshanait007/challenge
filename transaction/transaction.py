from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def execute(self, input_obj):
        pass

class TransactionValidator(object):
    def __init__(self, validate, trans_data_json):
        self.validate = validate
        self.trans_data_json = trans_data_json

    def execute_validator(self):
        print("InputValidator")
        print(self.validate)
        return self.validate.execute(self, self.trans_data_json)
