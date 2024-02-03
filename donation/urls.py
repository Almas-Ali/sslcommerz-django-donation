from django.urls import path

from donation import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success", views.success_donation, name="success_donation"),
    path("cancel", views.cancel_donation, name="cancel_donation"),
    path("fail", views.fail_donation, name="fail_donation"),
]
