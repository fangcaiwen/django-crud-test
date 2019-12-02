from django.urls import path, include
import user.views

urlpatterns = [
    path('list', user.views.get_user_list),
    path('add', user.views.add_user),
    path('edit/<int:user_id>', user.views.edit_user),
    path('delete/<int:user_id>', user.views.delete_user),
    path('search/<int:user_id>', user.views.search_user),
]
