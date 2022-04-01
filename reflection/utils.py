from calendar import HTMLCalendar

from .choices import FEELING_ICONS


class ReflectionCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(ReflectionCalendar, self).__init__()

    def formatday(self, day, events):
        reflections_per_day = events.filter(date__day=day)
        feeling_icons = FEELING_ICONS
        d = "".join(
            f'<button onclick="getDetails({event.get_absolute_url().rsplit("/", 1)[-1]})"><img src="/static/{feeling_icons[event.feeling - 1]}" alt=""></button>'
            for event in reflections_per_day
        )

        if day != 0:
            return f"<td><div class='date'>{day}</div><ul class='feeling-icon'> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, theweek, events):
        week = "".join(self.formatday(d[0], events) for d in theweek)
        return f"<tr> {week} </tr>"

    def formatmonth(self, entries, withyear=True):
        events = entries

        cal = '<table border="1" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal
