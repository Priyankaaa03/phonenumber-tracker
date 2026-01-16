'''import phonenumbers
from test import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en")'''

import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_details(number):
    try:
        phone = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(phone):
            print("❌ Invalid phone number")
            return

        country = geocoder.description_for_number(phone, "en")
        service = carrier.name_for_number(phone, "en")
        intl_format = phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national_format = phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.NATIONAL)

        print("\n📞 Phone Number Details")
        print("----------------------")
        print("Country / Location :", country)
        print("Service Provider   :", service)
        print("International No   :", intl_format)
        print("National No        :", national_format)

    except:
        print("❌ Error while processing number")

# Main Program
number = input("Enter phone number with country code (example +919876543210): ")
get_phone_details(number)
