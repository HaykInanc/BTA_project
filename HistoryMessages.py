class HistoryMessages:
    @staticmethod
    def deposit(status, amount, total_balance):
        return {
            "operation_type": "deposit",
            "status": status,
            "amount_of_deposit": amount,
            "total_balance": total_balance
        }
    
    def debit(status, amount, total_balance):
        return {
            "operation_type": "debit",
            "status": status,
            "amount_of_deposit": amount,
            "total_balance": total_balance
        }
    
    def exchange(status, amount, exchange_amount, currency_from, currency_to):
        return {
            "operation_type": "exchange",
            "status": status,
            "pre_exchange_amount": amount,
            "exchange_amount": exchange_amount,
            "currency_from": currency_from,
            "currency_to": currency_to
        }