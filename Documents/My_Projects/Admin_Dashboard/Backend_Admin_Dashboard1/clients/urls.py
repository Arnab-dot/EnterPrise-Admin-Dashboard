from django.urls import path
from clients.views import ClientListCreateView, ClientListRetrieveUpdateDeleteView, InvoiceListCreateView, InvoiceListRetrieveUpdateDeleteView

urlpatterns = [
    path("clients/", ClientListCreateView.as_view(), name="client-list-create"),
    path("clients/<int:id>/", ClientListRetrieveUpdateDeleteView.as_view(), name="client-list-retrieve-update-delete"),
    path("invoice/", InvoiceListCreateView.as_view(), name="invoice-list-create"),
    path("invoice/<int:id>/", InvoiceListRetrieveUpdateDeleteView.as_view(), name="invoice-list-retrieve-update-delete"),
]
