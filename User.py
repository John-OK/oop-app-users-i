class User:
    def __init__(self, name, email_address, driver_license_number, you_name_it = "I named it!"):
        self.name = name.lower()
        self.email_address = email_address.lower()
        self.driver_license_number = str(driver_license_number).lower()
        self.you_name_it = str(you_name_it).lower()

bob = User('Bob', 'BobMartin@supergeek.org', 'A1234567')
sue = User('Sue', 'suziq@aboynamedsue.com', 'B9876543', 'Anything but "Sue!"')
jesus = User('DaJesus', 'dajesus@weroll.net', 'Z4682467', 'Nobody messes wit da Jesus!')

print(bob.name, sue.email_address, jesus.you_name_it)