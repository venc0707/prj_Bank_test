def filter_by_state(new_list: list[dict], state='EXECUTED') -> list[dict]:
    """ Функция фильтрует список словарей и возвращает по ключу 'state' """
    filter_list = list()
    for dict_ in new_list:
        if dict_.get('state') == state:
            filter_list.append(dict_)
    return filter_list


def sort_by_date(new_list: list[dict], reverse=True) -> list[dict]:
    """Функция сортирует по дате"""
    # for dict_ in new_list:
    #     print(dict_.get('data'))
    sorted_list = sorted(new_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list


if __name__ == '__main__':
    new_list = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print(filter_by_state(
        new_list))  # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'} {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}]

    print(sort_by_date(
        new_list))  # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
