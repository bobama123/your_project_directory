from datetime import datetime
from lib.user_birthday import UserBirthday

def test_for_empty_list():
    user_birthday = UserBirthday()
    result = user_birthday.records

    assert result == []

def test_add_for_two_people():
    user_birthday = UserBirthday()
    user_birthday.add("Bobby", "25-11-1998")
    user_birthday.add("Dom", "28-1-1992")

    result = user_birthday.records

    assert result == [{'name': "Bobby", 'birthdate': datetime(1998, 11, 25, 0, 0), 'card_sent': False}, {'name': "Dom", 'birthdate': datetime(1992, 1, 28, 0, 0), 'card_sent': False}]

def test_update_date_updates_date_for_person():
    user_birthday = UserBirthday()
    user_birthday.add("Bobby", "25-11-1998")
    user_birthday.add("Dom", "28-1-1992")
    user_birthday.update_date("Bobby", "18-5-2000")

    result = user_birthday.records

    assert result == [{'name': "Bobby", 'birthdate': datetime(2000, 5, 18, 0, 0), 'card_sent': False}, {'name': "Dom", 'birthdate': datetime(1992, 1, 28, 0, 0), 'card_sent': False}]

def test_update_name_updates_name_for_person():
    user_birthday = UserBirthday()
    user_birthday.add("Bobby", "25-11-1998")
    user_birthday.add("Dom", "28-1-1992")
    user_birthday.update_name("Dom", "Maximillian")

    result = user_birthday.records

    assert result == [{'name': "Bobby", 'birthdate': datetime(1998, 11, 25, 0, 0), 'card_sent': False}, {'name': "Maximillian", 'birthdate': datetime(1992, 1, 28, 0, 0), 'card_sent': False}]

def test_if_reminder_returns_only_close_birthdays_for_current_date():
    user_birthday = UserBirthday()
    user_birthday.add("Bobby", "25-11-1998")
    user_birthday.add("Dom", "28-1-1992")
    result = user_birthday.reminder("16-11-2021")

    assert result == [{'name': "Bobby", 'birthdate': datetime(1998, 11, 25, 0, 0), 'card_sent': False}]

def test_if_age_returns_age_of_users_from_reminder():
    user_birthday = UserBirthday()
    user_birthday.add("Bobby", "25-11-1998")
    user_birthday.add("Dom", "28-1-1992")
    user_birthday.reminder("16-11-2021")
    result = user_birthday.age("16-11-2021")

    assert result == "Upcoming birthday of Bobby, age is 23"
