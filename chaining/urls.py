from django.urls import path
from . import views

urlpatterns = [
    path('chain/', views.full_chain, name="get the full chain"),
    path('mine/', views.mine, name="mine a block"),
    path('transactions/new/', views.new_transaction, name="add a new transaction"),
    path('nodes/register/', views.register_nodes, name="register a new node"),
    path('nodes/resolve/', views.consensus, name="consensus(check consistency)"),
]