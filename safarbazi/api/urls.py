from django.urls import path, include

urlpatterns = [
    path('auth/', include(('safarbazi.authentication.urls', 'auth'))),
    path('users/', include(('safarbazi.users.urls', 'users'))),
    path('residence/', include(('safarbazi.residence.urls', 'residence'))),
]
