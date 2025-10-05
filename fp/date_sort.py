def sort_dates(dates):
    working_list = dates.copy()
    md_array = list(map(lambda x: x.split("-"), working_list))
    sorted_md_array = sorted(md_array, key=lambda x: (x[2], x[0], x[1]))
    return list(map(lambda x: "-".join(x), sorted_md_array))


# the following would have been a lot better...


def better_sort_dates(dates):
    return sorted(dates, key=format_date)


def format_date(date):
    month, day, year = date.split("-")
    return year + month + day
