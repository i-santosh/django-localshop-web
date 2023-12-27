"""
URL configuration for localshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup',views.SignUp.signupGetData,name='signupGetData'),
    path('accounts/signup/verify',views.SignUp.signupFinishByVerifyCode,name='signupFinishByVerifyCode'),
    path('accounts/signin',views.signin,name='signin'),
    path('accounts/signout',views.signout,name='signout'),
    path('accounts/signup/sendVerificationCode',views.sendVerificationCode,name='sendVerificationCode'),
    path('accounts/signup/resendCode',views.SignUp.resendCode,name='resendCode'),
    path('',views.index,name="home"),
    path('accounts/settings',views.account,name="account"),
    path('accounts/user/orders',views.orders,name="orders"),
    path('accounts/user/subscribeAndSave',views.subscribeAndSave,name='subscribeAndSave'),
    path('accounts/user/editProfile',views.editProfile,name='editProfile'),
    path('accounts/user/manageAddresses',views.manageAddresses,name='manageAddresses'),
    path('accounts/user/purchaseSettings',views.purchaseSettings,name='purchaseSettings'),
    path('accounts/user/emailAlertPreferences',views.emailAlertPreferences,name='emailAlertPreferences'),
    path('accounts/user/deleteMyAccount',views.deleteMyAccount,name='deleteMyAccount'),
    path('accounts/user/contactUs',views.contactUs,name='contactUs'),
    path('accounts/user/feedback',views.feedback,name='feedback'),
    path('accounts/user/privacyNotice',views.privacyNotice,name='privacyNotice'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
