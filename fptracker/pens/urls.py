from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name = "index"),
    
    path('pens/add', views.edit_pen, name = 'add_pen'),
    path('pens/edit/<int:pen_id>', views.edit_pen, name = 'edit_pen'),
    path('pens/d/<int:pen_id>', views.delete_pen, name = 'delete_pen'),
    
    path('ink/add', views.edit_ink, name = 'add_ink'),
    path('ink/edit/<int:ink_id>', views.edit_ink, name = 'edit_ink'),
    path('ink/d/<int:ink_id>', views.delete_ink, name = 'delete_ink'),
    path('brand-<str:pen_brand>/ink-<int:current_ink>', views.index, name = 'index'),
    path('brand-<str:pen_brand>', views.index, name = 'index'),
    path('ink-<int:current_ink>', views.index, name = 'index'),

]
