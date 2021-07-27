"""
You are given a list of email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores: a-z, A-Z, 0-9, _, -
The website name can only have letters and digits: a-z, A-Z, 0-9
The extension can only contain letters: a-z, A-Z.
The maximum length of the extension is: 3.
"""

def is_valid_username(username: str):
    return username.replace('_', '').replace('-', '').isalnum()

def is_valid_website(website: str):
    return website.isalnum()

def is_valid_extension(extension: str):
    return extension.isalpha() and len(extension) == 3

def is_valid_email_address(email_address: str):

    user_name = email_address.split('@')[0]
    website = email_address.split('.')[0]
    extension = email_address.split('.')[-1]

    return is_valid_username(user_name) or is_valid_website(website) or is_valid_extension(extension)


def get_valid_emails(email_addresses):

    valid_email_addresses = []
    for email_address in email_addresses:
        if is_valid_email_address(email_address):
            valid_email_addresses.append(email_address)
    return valid_email_addresses



def test_get_valid_emails():

    email_addresses = ['name@website.com']
    valid_emails = get_valid_emails(email_addresses)
    assert valid_emails == ['name@website.com']

    # Check that the list is sorted is lexicographical order
    email_addresses = ['name@website.com', 'age@whatevs.com']
    assert get_valid_emails(email_addresses) == ['age@whatevs.com', 'name@website.com']

    # When one address is not valid, omit it from the return
    email_addresses = ['a_1@website.com', 'b_2@website.com', 'c_3_BADEMAIL']
    assert get_valid_emails(email_addresses) == ['a_1@website.com', 'b_2@website.com']

    # When there is two usernames, is invalid email
    email_addresses = ['a_1@b_1@website.com']
    assert get_valid_emails(email_addresses) == []

    # When there are two extensions, is invalid email
    email_addresses = ['a_1@website.com.edu']
    assert get_valid_emails(email_addresses) == []

    # When there is no username, is invalid
    email_addresses = ['website.com']
    assert get_valid_emails(email_addresses) == []

def test_is_valid_extension():
    # Check some extensions
    assert is_valid_extension('a_name@website.CoR')
    assert is_valid_extension('b_name@website.co')
    assert not is_valid_extension('c_name@website.com4')

def test_is_valid_website():
    assert is_valid_website('website')
    assert not is_valid_website('website!!!')
    assert not is_valid_website('   ')