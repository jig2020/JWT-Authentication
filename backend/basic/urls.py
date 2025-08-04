from django.urls import path
from .views import get_notes, CustomTokenObtainPairView, CustomRefreshTokenView, register, logout, is_authenticated

urlpatterns = [
    path('notes/', get_notes, name='get_notes'),
    # JWT Authentication URLs
    # These URLs are used for obtaining and refreshing JWT tokens
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', logout),
    path('authenticated/', is_authenticated),
    path('register/', register)
]