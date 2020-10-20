from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Alert, Category, Location, RuleView, CategoryView
from .serializers import AlertSerializer, CategorySerializer, LocationSerializer, RuleViewSerializer, CategoryViewSerializer
from .filters import RuleViewFilter, CategoryViewFilter


class AlertsView(viewsets.ReadOnlyModelViewSet):
    queryset = Alert.objects.select_related('location').order_by('-timestamp')
    serializer_class = AlertSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
        'id': ['exact', 'gt', 'lt'],
        'rule_id': ['exact'],
        'level': ['exact', 'gt', 'lt'],
        'timestamp': ['exact', 'gt', 'lt'],
        'location__id': ['exact'],
        'location__name': ['exact', 'contains'],
        'src_ip': ['exact', 'contains'],
        'dst_ip': ['exact', 'contains'],
        'src_port': ['exact', 'gt', 'lt'],
        'dst_port': ['exact', 'gt', 'lt'],
        'user': ['exact'],
        'full_log': ['contains'],
    }


class CategoriesView(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('cat_id', 'cat_name')


class LocationsView(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {'server_id': ['exact'], 'name': ['exact', 'contains']}


class RuleViewView(viewsets.ReadOnlyModelViewSet):
    queryset = RuleView.objects.all()
    serializer_class = RuleViewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = RuleViewFilter


class CategoryViewView(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryView.objects.all()
    serializer_class = CategoryViewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CategoryViewFilter
