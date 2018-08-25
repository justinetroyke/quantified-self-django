from rest_framework.urlpatterns import format_suffix_patterns
from .views import FoodViews

urlpatterns = {
    path('foods/', FoodViews.as_view({'get': 'list', 'post': 'create'})),
}

urlpatterns = format_suffix_patterns(urlpatterns)
