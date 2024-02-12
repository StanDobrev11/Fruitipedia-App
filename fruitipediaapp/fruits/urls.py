from django.urls import path, include

from fruitipediaapp.fruits.views import create_fruit, details_fruit, delete_fruit, edit_fruit

urlpatterns = [
    path('', create_fruit, name='create fruit'),

    path(
        '<int:fruit_id>/',
        include([
            path('details/', details_fruit, name='details fruit'),
            path('delete/', delete_fruit, name='delete fruit'),
            path('edit/', edit_fruit, name='edit fruit'),
        ]),
    ),
]
