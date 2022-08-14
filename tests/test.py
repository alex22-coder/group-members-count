from main_program.parser import (divide_users_into_two_groups, get_all_members, is_staff,
                                 open_file, write_result_in_file)

import pytest

from tests.conftest import (ALL_USERS_LIST, HTML_ALL_USERS,
                            HTML_WITH_DUPLICATE_USERS, STAFF, STUDENTS,
                            TEST_USER_IS_STAFF_WORD, TEST_USER_NOT_STAFF_WORD)


@pytest.mark.parametrize("word", TEST_USER_IS_STAFF_WORD)
def test_user_is_staff(word):
    """проверка является ли пользователь сотрудником ЯПрактикума"""
    assert is_staff(word)


@pytest.mark.parametrize("word", TEST_USER_NOT_STAFF_WORD)
def test_user_is_not_staff(word):
    """проверка что пользователь не является сотрудником ЯПрактикума"""
    assert not is_staff(word)


def test_read_html_from_file():
    """проверяем чтение из файла"""
    assert open_file('tests/for_test.html') == HTML_ALL_USERS


def test_write_to_txt_file():
    """проверяем запись в файл"""
    write_result_in_file(['test', 'write', 'read'], 'tests/test')

    assert open_file('tests/test.txt') == 'test\nwrite\nread'


def test_get_members_from_html():
    """получаем всех пользователей группы из HTML"""
    assert get_all_members(HTML_ALL_USERS) == {'test_user_2', 'test_user_1'}


def test_remove_duplicate_from_html():
    """удаляются ли дубликаты юзеров из HTML"""
    assert get_all_members(HTML_WITH_DUPLICATE_USERS) == {'test_user_1'}


def test_divide_users_by_groups():
    """делим пользователей на две группы, студенты и сотрудники"""
    assert divide_users_into_two_groups(ALL_USERS_LIST) == (STUDENTS, STAFF)
