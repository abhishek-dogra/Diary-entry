from django.urls import path

from . import views

urlpatterns=[
path('',views.homepage),
path('login',views.login_page),
path('register',views.register_page),
path('reg_entry',views.check_reg),
path('log_check',views.check_log),
path('makeEntry',views.make_entry),
path('saveEntry',views.save_entry),
path('viewEntry/<int:qid>',views.view_entry),
path('logout',views.logout),
path('editEntry/<int:qid>',views.edit_entry),
path('saveEdits/<int:qid>',views.save_edits),
path('deleteEntry/<int:qid>',views.delete_entry)
#path('entries',views.all_entries),
#path('read',views.read_entry),
#path('edit',views.edit_entry)
]
