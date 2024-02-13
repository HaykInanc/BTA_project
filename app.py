from Account import Account
from CurrencyExchange import CurrencyExchange
from TerminalInterface import TerminalInterface

def main():
    user_account = Account()
    exchange = CurrencyExchange()

    while True:
        TerminalInterface.show_commands()
        choice = input("Set command: ")

        if choice == "0":
            return
        elif choice == "1":
            print(f"Current Balance: {user_account.get_balance()}")
        elif choice == "2":
            deposit_amount = input("Enter deposit amount: ")
            user_account.deposit(deposit_amount)
        elif choice == "3":
            withdraw_amount = input("Enter deposit amount: ")
            user_account.debit(withdraw_amount)
        elif choice == "4":
            history = user_account.get_history()
            print(history)
        elif choice == "5":
            available_currency = " ".join(exchange.get_exchange_rates().keys())
            print(f"Select a currency from the available currencies: {available_currency}")
            source_currency = input("Enter source currency: ")
            target_currency = input("Enter target currency: ")
            exchange_amount = input("Enter target currency: ")

            result = exchange.exchange_currency(source_currency, target_currency, exchange_amount)
            if result is not None:
                print(f"Converted amount: {result} {target_currency}")

if __name__ == "__main__":
    main()