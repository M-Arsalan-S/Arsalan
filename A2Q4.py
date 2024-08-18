# import datetime
# today = datetime.date.today()
#
# # months = {
# #     1: "January",
# #     2: "February",
# #     3: "March",
# #     4: "April",
# #     5: "May",
# #     6: "June",
# #     7: "July",
# #     8: "August",
# #     9: "September",
# #     10: "October",
# #     11: "November",
# #     12: "December"
# # }
#
# yr = today.year
# mon = today.month
# day = today.day
# print(datetime.datetime.now())

from datetime import datetime
import pytz  # python time zone

# timezone
tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
formatted_date = now.strftime('%a %B %d %H:%M:%S IST %Y')
print(formatted_date)

