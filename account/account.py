from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def execute(self, input_obj):
        pass


class AccountValidator(object):
    def __init__(self, validate, account_data_obj):
        self.validate = validate
        self.account_data_obj = account_data_obj

    def execute_validator(self):
        print("InputValidator")
        print(self.validate)
        return self.validate.execute(self, self.account_data_obj)
