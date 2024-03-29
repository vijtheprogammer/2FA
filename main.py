#pre-requisite: pip install pyotp

'''
File: main.py
Author: Aryan Vij
Description: This is a Two-Factor Authentication (2FA) System developed in Python.
''' 

import pyotp
import qrcode

#only the service provider should have this
#if someone has the same key as you they can generate the same number as you

key = pyotp.random_base32() 

totp = pyotp.TOTP(key)
#print(totp.now())
# .now() - generates the current time OTP

# .verify() - verifies OTP passed in against current time OTP
uri = pyotp.totp.TOTP(key).provisioning_uri(name="vij1"
    , issuer_name="AryanVij App")
print(uri)
qrcode.make(uri).save("totp.png")


while True:
    print(totp.verify(input("Enter One-time Passcode: ")))
