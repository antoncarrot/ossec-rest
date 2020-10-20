from django_filters.rest_framework import filters, filterset

from .models import RuleView, CategoryView


class _ArrayNumberFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class _ArrayCharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class RuleViewFilter(filterset.FilterSet):
    rule_id = filters.NumberFilter(lookup_expr='exact')
    categories = _ArrayCharFilter(lookup_expr='contains')

    class Meta:
        model = RuleView
        fields = '__all__'


class CategoryViewFilter(filterset.FilterSet):
    cat_id = filters.NumberFilter(lookup_expr='exact')
    cat_name = filters.CharFilter(lookup_expr='exact')
    rules = _ArrayNumberFilter(lookup_expr='contains')

    class Meta:
        model = CategoryView
        fields = '__all__'
