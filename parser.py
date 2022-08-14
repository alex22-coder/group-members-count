from typing import Tuple, Set, List, Union

from bs4 import BeautifulSoup

from exceptions import NotFile, ParsingError
from log.config_logger import logger

STAFF_WORDS = ('куратор', 'наставник', 'менеджер', 'ревью',
               'продюсер сообществ', 'manager', 'support')


def is_staff(user: str) -> bool:
    """checks if the user is an employee"""
    user = user.lower()

    for word in STAFF_WORDS:
        if word in user:
            return True
    return False


def open_file(file_name='slack_members.html') -> str:
    """gets HTML from file"""
    try:
        with open(file_name) as file:
            html = file.read()

        logger.debug('получили HTML из файла "slack_members.html"')

        return html

    except FileNotFoundError:
        raise NotFile('проверьте файл "slack_members.html"')


def get_all_members(html: str) -> set:
    """gets all users from HTML, delete duplicates and return set of users"""
    slack_members = []

    soup = BeautifulSoup(html, 'html.parser')
    user_source = soup.find_all(class_='p-ia_details_popover__members_list_item')

    if len(user_source) == 0:
        raise ParsingError('в HTML нет класса "p-ia_details_popover__members_list_item"')

    for page_element in user_source:
        try:
            slack_members.append(page_element.div.div['aria-label'])
        except Exception as err:
            ParsingError(f'нет атрибута "aria-label" - {err}')

    users = set(slack_members)

    return users


def divide_users_into_two_groups(users: Union[Set[str], List[str]]) -> Tuple[list, list]:
    """returns two lists of employees and students"""
    staff = []
    students = []
    staff_count = students_count = 0

    for user in users:
        if is_staff(user):
            staff_count += 1
            staff.append(user)
        else:
            students_count += 1
            students.append(user)

    logger.debug(f'успешно разделили пользователей на две группы,'
                 f' студентов = {students_count}, сотрудников ЯП = {staff_count}')

    return students, staff


def write_result_in_file(users: list[str], file_name: str) -> None:
    """writes the result to a file"""
    with open(f'{file_name}.txt', 'w') as file:
        file.write('\n'.join(users))

    logger.info(f'успешно записали файл {file_name}.txt')


def main():
    """main program logic"""
    try:
        html = open_file()
        users = get_all_members(html)
        students, staff = divide_users_into_two_groups(users)
        write_result_in_file(staff, 'staff')
        write_result_in_file(students, 'students')
    except NotFile:
        logger.error('нет файла slack_members.html')
    except (Exception, ParsingError) as err:
        logger.error(f'Сбой в работе программы - {err}')


if __name__ == '__main__':
    main()
