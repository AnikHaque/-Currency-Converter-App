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