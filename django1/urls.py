from django.contrib import admin
from django.urls import path
from core.views import main_view, contacts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('contacts/', contacts_view)

    # path('', test),
    # path('custom/', test2)
]