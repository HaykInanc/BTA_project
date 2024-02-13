from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        pass 
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        # self.file_manager 

    def get_exchange_rates(self):
        pass
        # Implement a process that sends a get request to a <link> link 
        # and returns the resulting dictionary.
    
    def exchange_currency(self, currency_from, currency_to, amount):
        pass

        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency

        # with a positive outcome, the record of history looks like this 
        # history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        # self.write_to_history(history_message)
        
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number
        # history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        # self.write_to_history(history_message)