from django.contrib import admin

from django.urls import path

from home import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup',views.signup),
    path('account',views.account),
    path('home',views.itrhome),
    path('itrdetails',views.formtesting2),
    path('itrsubmit',views.itrsubmit),
    path('paymentstart',views.payment),
    path('payment_status',views.payment_status),
    path('invoice',views.invoice),
    path('testing',views.testing),
    path('test',views.formtesting),
    path('test2',views.formtesting2)
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
