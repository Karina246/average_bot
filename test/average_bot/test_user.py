from ...src.average_bot.user import User
import pytest

def test_get_average_users_no_users():
    assert User.get_average_users() == '0'

def test_create_user():
    user = User('UGX18G1PV')
    assert user.member_id == 'UGX18G1PV'
    assert user.average == 0.0
    assert user.count == 0

def test_only_one_user_per_member():
    first_user = User('UGX18G1PV')
    second_user = User('UGX18G1PV')
    first_user.add_new_number(5)
    assert first_user.average == 5
    assert first_user.average == second_user.average

def test_add_new_number():
    user = User('UGX4SKU10')
    user.add_new_number(5)
    user.add_new_number(7)
    assert user.count == 2
    assert user.average == 6.0

def test_get_average_str():
    user = User('UGX4SKU10')
    user.add_new_number(8)
    assert user.get_average_str() == '6.67'

def test_get_average_users():
    assert User.get_average_users() == '5.83'
