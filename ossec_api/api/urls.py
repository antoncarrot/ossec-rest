from rest_framework import routers

from .views import AlertsView, LocationsView, RuleViewView, CategoryViewView

router = routers.DefaultRouter()
router.register(r'alerts', AlertsView)
router.register(r'locations', LocationsView)
router.register(r'rules', RuleViewView)
router.register(r'categories', CategoryViewView)
urlpatterns = router.urls
