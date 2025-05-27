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
     
        # ইনস্ট্যান্স অ্যাট্রিবিউট সেট করা হচ্ছে
    
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
        self.logger = logger  # Association - Logger ক্লাসের অবজেক্ট ইনপুট হিসেবে নিচ্ছে
