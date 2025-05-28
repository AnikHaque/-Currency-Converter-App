# CurrencyConverter ক্লাস তৈরি করা হয়েছে যেটি মুদ্রা রূপান্তরের কাজ করে

class CurrencyConverter:
    # ক্লাস অ্যাট্রিবিউট: mock exchange rates
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 83.0,
        'BDT': 110.0,
    }




  def __init__(self, amount, from_currency, to_currency, logger):

     """
     ইনস্ট্যান্স অ্যাট্রিবিউট সেট করা হচ্ছে
    """
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
        self.logger = logger  # Association - Logger ক্লাসের অবজেক্ট ইনপুট হিসেবে নিচ্ছে




def convert(self, user):
        """
        এই মেথডটি মূল কনভার্সন সম্পন্ন করে এবং লগ করে
        """
        if not self.is_valid_currency(self.from_currency) or not self.is_valid_currency(self.to_currency):
            raise ValueError("Invalid currency code")

        # রূপান্তরের জন্য প্রথমে USD তে কনভার্ট, তারপর টার্গেট কারেন্সিতে
        usd_amount = self.amount / self.exchange_rates[self.from_currency]
        converted_amount = usd_amount * self.exchange_rates[self.to_currency]

        # রাউন্ড করে ২ দশমিকে আনা হচ্ছে
        converted_amount = round(converted_amount, 2)

        # Logger ব্যবহার করে conversion লগ করা হচ্ছে
        self.logger.log(user, self.amount, self.from_currency, converted_amount, self.to_currency)

        return converted_amount





        @classmethod
    def update_exchange_rate(cls, currency_code, new_rate):
        """
        কারেন্সির এক্সচেঞ্জ রেট আপডেট করার ক্লাস মেথড
        """
        currency_code = currency_code.upper()
        if not cls.is_valid_currency(currency_code):
            raise ValueError("Invalid currency code")
        cls.exchange_rates[currency_code] = new_rate




    @staticmethod
    def is_valid_currency(currency_code):
        """
        কারেন্সি কোড valid কিনা যাচাই করে
        """
        return currency_code.upper() in CurrencyConverter.exchange_rates





        # Logger ক্লাস তৈরি করা হয়েছে, যেটা conversion লগ রাখে
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, user, amount, from_currency, result, to_currency):
        """
        ইউজারের conversion লগ করা হচ্ছে
        """
        entry = f"User: {user} converted {amount} {from_currency} to {result} {to_currency}"
        print("LOG:", entry)  # CLI তে লগ প্রিন্ট করা হচ্ছে
        self.logs.append(entry)



        # CLI Interface
if __name__ == "__main__":
    logger = Logger()
    print("=== Currency Converter CLI App ===")

    try:
        user = input("Enter your name: ")
        amount = float(input("Enter the amount: "))
        from_currency = input("From Currency (e.g. USD): ")
        to_currency = input("To Currency (e.g. EUR): ")

        converter = CurrencyConverter(amount, from_currency, to_currency, logger)
        result = converter.convert(user)

        print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")
    except Exception as e:
        print("Error:", e)