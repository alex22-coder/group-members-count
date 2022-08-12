from typing import Tuple, Set, List, Union

from bs4 import BeautifulSoup

STAFF_WORDS = ('куратор', 'наставник', 'менеджер', 'ревью',
               'продюсер сообществ', 'manager', 'support')


def is_staff(user: str) -> bool:
    """checks if the user is an employee"""
    user = user.lower()

    for i in STAFF_WORDS:
        if i in user:
            return True
    return False


def open_file(file_name='slack_members.html') -> str:
    """gets HTML from file"""
    with open(file_name) as file:
        html = file.read()
    return html


def get_all_members(html: str) -> set:
    """gets all users from HTML, delete duplicates and return set of users"""
    slack_members = []

    soup = BeautifulSoup(html, 'html.parser')
    user_source = soup.find_all(class_='p-ia_details_popover__members_list_item')

    for page_element in user_source:
        slack_members.append(page_element.div.div['aria-label'])

    users = set(slack_members)

    return users


def divide_users_into_two_groups(users: Union[Set[str], List[str]]) -> Tuple[list, list]:
    """returns two lists of employees and students"""
    staff = []
    students = []

    for user in users:
        if is_staff(user):
            staff.append(user)
        else:
            students.append(user)

    return students, staff


def write_result_in_file(users: list[str], file_name: str) -> None:
    """writes the result to a file"""
    for user in users:
        with open(f'{file_name}.txt', 'a') as file:
            file.write(user + '\n')


def main():
    """main program logic"""
    html = open_file()
    users = get_all_members(html)
    students, staff = divide_users_into_two_groups(users)
    write_result_in_file(staff, 'staff')
    write_result_in_file(students, 'students')


if __name__ == '__main__':
    main()
