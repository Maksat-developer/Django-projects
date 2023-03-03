from rest_framework import routers


from app_shop.views import ProductViewSet, CategoryViewSet
from app_news.views import ActionViewSet


router = routers.SimpleRouter()

router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('action', ActionViewSet)

# router.register('sub-category', SubCategoryViewSet)

urlpatterns = []

urlpatterns += router.urls

