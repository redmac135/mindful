from calendar import HTMLCalendar

from .choices import FEELING_ICONS


class ReflectionCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(ReflectionCalendar, self).__init__()

    def formatday(self, day, events, today):
        reflections_per_day = events.filter(date__day=day)
        feeling_icons = FEELING_ICONS
        d = "".join(
            f'<button onclick="getDetails({event.get_absolute_url().rsplit("/", 1)[-1]})"><img src="/static/{feeling_icons[event.feeling - 1]}" alt=""></button>'
            for event in reflections_per_day
        )

        if day != 0:
            if today == None:
                class_ = ''
            else:
                class_ = ' class="istoday"' if day == today.day else ''
            return f"<td{class_}><div class='date'>{day}</div><ul class='feeling-icon'> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events, today):
        week = "".join(self.formatday(d[0], events, today) for d in theweek)
        return f"<tr> {week} </tr>"

    def formatmonth(self, entries, today, withyear=True):
        events = entries

        if not self.month == today.month:
            today = None

        cal = '<table border="1" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events, today)}\n"
        return cal
