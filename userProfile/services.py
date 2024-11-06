from .models import User
from book.models import UserBook

from django.db.models import F, Sum, Count
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
        if len(books) == 0:
            return {
            'per_day': 0,
            'per_month': 0,
            'per_year': 0,
            'anytime': 0
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
            'anytime': books.count()
        }
        return all_times
