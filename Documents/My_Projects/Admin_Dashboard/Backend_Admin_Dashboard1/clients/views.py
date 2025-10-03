from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from clients.models import Clients, Invoice
from clients.serializers import ClientSerializer, InvoiceSerializer
from users.permissions import IsAdmin, IsAdminOrStaffOrReadOnly

class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_by__role']  # Fixed: role is from related user
    search_fields = ['username', 'user_address']  # Fixed: use actual model fields
    ordering_fields = ['username', 'created_at']  # Fixed: use actual model fields
    ordering = ['username']  # Fixed: use actual model field

    def get_queryset(self):
        # Only clients in the same organization as the logged-in user
        return Clients.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )

class ClientListRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrReadOnly]
    lookup_field = 'id'

    def get_queryset(self):
        return Clients.objects.filter(organization=self.request.user.organization)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class InvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'client']
    search_fields = ['client__username']  # Fixed: search through related field
    ordering_fields = ['created_at', 'amount']
    ordering = ['-created_at']

    def get_queryset(self):
        return Invoice.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user,
            updated_by=self.request.user
        )

class InvoiceListRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrReadOnly]
    lookup_field = 'id'

    def get_queryset(self):
        return Invoice.objects.filter(organization=self.request.user.organization)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
