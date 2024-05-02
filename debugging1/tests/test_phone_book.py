from lib.phone_book import PhoneBook

def test_for_no_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []

def test_for_no_phone_numbers_added():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is not relevant here")
    assert phone_book.list_numbers() == []

def test_extracts_number_for_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 07800000000")
    assert phone_book.list_numbers() == ["07800000000"]

def test_extracts_all_numbers():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sarah's number is 07800000003")
    phone_book.extract_numbers("Geoff's number is 07800000001")
    phone_book.extract_numbers("Alex's number is 07800000002")
    assert phone_book.list_numbers() == ["07800000003", "07800000001", "07800000002"]

def test_extracts_all_numbers_from_one_extract():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sarah's number is 07800000000 and Geoff's number is 07800000001")
    assert phone_book.list_numbers() == ["07800000000", "07800000001"]


def test_for_numbers_not_starting_with_zero():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 78000000000")
    assert phone_book.list_numbers() == []

def test_for_numbers_not_11():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 0780000 or 07800000000000")
    assert phone_book.list_numbers() == []