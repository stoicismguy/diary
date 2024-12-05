from .models import User
from book.models import UserBook
import calendar

from django.db.models import F, Sum, Count, Q
import datetime

class UserDAL:
    @staticmethod
    def get_user_by_username(username: str):
        try:
            user = User.objects.get(username=username)
            return user
        except:
            raise Exception(f"Found no  user with this username: {username}")            
        
    
    @staticmethod
    def get_user_by_uuid(uuid: str):
        user = User.objects.get(id=uuid)
        if user is None:
            raise Exception(f"Found no  user with this uuid: {uuid}")
        return user
    
    @staticmethod
    def get_stat(user):
        books = UserBook.objects.filter(user=user)
        schedule = get_schedule(user)
        if len(books) == 0:
            return {
            'per_day': 0,
            'per_month': 0,
            'per_year': 0,
            'anytime': 0,
            'schedule': schedule
        }
        time_per_day = books.annotate(time=F('finish_date')-F('start_date')).aggregate(Sum('time'), Count('time'), Sum('pages'))
        timedays = time_per_day.get('pages__sum') / (time_per_day.get('time__sum').days + time_per_day.get('time__count'))
        date_now = datetime.datetime.now()
        per_month = UserBook.objects.filter(user=user, start_date__gte=datetime.date(date_now.year, date_now.month, 1)).count()
        per_year = UserBook.objects.filter(user=user, start_date__gte=datetime.date(date_now.year, 1, 1)).count()
        all_times = {
            'per_day': int(timedays),
            'per_month': per_month,
            'per_year': per_year,
            'anytime': books.count(),
            'schedule': schedule 
        }

            
        return all_times
    
def get_schedule(user):
    books = UserBook.objects.filter(user=user)
    date_now = datetime.datetime.now()
    schedule = []

    current_month = date_now.month
    months = _get_monthes(current_month, date_now.year)

    for m_index, item in enumerate(months):
        item_month, item_year = item[0], item[1]

        month_info = calendar.monthrange(item_year, item_month)
        start_date = datetime.date(item_year, item_month, 1)
        finish_date = datetime.date(item_year, item_month, month_info[1])

        filtered_books = _get_filtered_books(books, start_date, finish_date)
        
        active_days = _get_active_days(filtered_books, start_date, finish_date, month_info)

        schedule.append({
            'month': item_month,
            'offset': month_info[0],
            'days': month_info[1],
            'active_day': list(active_days)
        })

    return schedule


def _get_active_days(books, start_date, finish_date, month_info):
    active_days = set()
    for book in books:
        start = book.start_date
        finish = book.finish_date

        if start < start_date and finish > finish_date:
            print("WORKS")
            return range(1, month_info[1] + 1)

        if finish > finish_date:
            finish = month_info[1]
            start = start.day
        elif start < start_date:
            start = 1
            finish = finish.day
        else:
            start = start.day
            finish = finish.day

        for day in range(start, finish + 1):
            active_days.add(day)
    return active_days


def _get_filtered_books(books, start_date, finish_date):
    query_range = (start_date, finish_date)
    q_start = Q(start_date__range=query_range)
    q_finish = Q(finish_date__range=query_range)

    filtered_books = books.filter((q_start | q_finish) | Q(start_date__lte=start_date, finish_date__gte=finish_date))
    return filtered_books

def _get_monthes(cur, year):
    
    res = []
    for x in range(5, -1, -1):
        m = cur - x
        if m <= 0:
            res.append((12 + m, year - 1))
        else:
            res.append((m, year))
    return res

