
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

admin.site.site_header = "SCS Super Admin"
admin.site.site_title = "SCS Super Admin"
admin.site.index_title = "Welcome to SCS Super Admin"

schema_view = get_schema_view(
    openapi.Info(
        title="SCS API",
        default_version='v1',
        description="Join our platform to receive personalized suggestions, funding advice, and more based on your unique profile. Let's help you achieve your academic goals!",
        terms_of_service="",
        contact=openapi.Contact(email="kallolnaha@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/defender/', include('defender.urls')), 
    path("admin/", admin.site.urls),
    path('api/', include('auth_app.urls')),
    path('api/', include('educational_organizations_app.urls')),
    path('api/', include('campus_app.urls')),
    path('api/', include('college_app.urls')),
    path('api/', include('department_app.urls')),
    path('api/', include('faculty_members_app.urls')),
    path('api/', include('university_app.urls')),
    path('api/', include('common.urls')),
    path('api/', include('profile_app.urls')),
    path('api/', include('security.urls')), 
    path("api/", include("contact_app.urls")),
    path('logs/', include('log_viewer.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('api/', include('user_app.urls')),
]
 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
