import pendulum

date1 = "26/06/24"
date2 = pendulum.now("UTC")


def find_time_diff(start_date: str, end_date: pendulum.DateTime):
    # Convert date 1 to datetime object
    start_date = pendulum.from_format(date1, "DD/MM/YY")
    # Find difference between date2 and date1
    dt_diff = start_date.diff(end_date).in_days()
    # dt_diff = start_date.diff_for_humans(end_date)
    # Print result
    return dt_diff


date_difference = find_time_diff(date1, date2)

# dt1 = pendulum.from_format(date1, "DD/MM/YYYY")
# print(find_time_diff(date1, date2))
print(f"The difference between {date1} and {date2} is {date_difference}")



