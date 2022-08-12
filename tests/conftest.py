TEST_USER_IS_STAFF_WORD = ('куратор', 'наставник', 'менеджер', 'ревью',
                           'продюсер сообществ', 'manager', 'support')

TEST_USER_NOT_STAFF_WORD = ('обычный Вася', 'другой юзер', 'Сергей Шнуров')

HTML_ALL_USERS = """<div class="p-ia_details_popover__members_list_item">
                    <div><div aria-label="test_user_1"></div></div></div>
                    <div class="p-ia_details_popover__members_list_item"><div>
                    <div aria-label="test_user_2"></div></div></div>"""

HTML_WITH_DUPLICATE_USERS = """<div class="p-ia_details_popover__members_list_item">
                               <div><div aria-label="test_user_1"></div></div></div>
                               <div class="p-ia_details_popover__members_list_item"><div>
                               <div aria-label="test_user_1"></div></div></div>"""

ALL_USERS_LIST = ['Виктор Цой', 'Юра Шатунов', 'Наставник Николай',
                  'Ревьювер Вова', 'Майкл Джексон', 'manager Roma']

STUDENTS = ['Виктор Цой', 'Юра Шатунов', 'Майкл Джексон']

STAFF = ['Наставник Николай', 'Ревьювер Вова', 'manager Roma']
