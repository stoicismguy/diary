from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(('userProfile.urls', 'profile'), namespace='profile')),
    path('api/books/', include(('book.urls', 'books'), namespace='books')),
    path('api/collections/', include(('collection.urls', 'collection'), namespace='collection')),
]
