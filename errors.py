class SuiError:
    def __init__(self, error_number: int):
        self.error_number = error_number

        if self.error_number == -32000:
            raise Exception('Not enough money to pay for gas')