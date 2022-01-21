from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from System.part import views as part_view
from .views import companyadd, supplieradd, spensesadd, userlist, index, userinformation, userinformation_update, companylist, banklist, bankadd, bankdetail, bankupdate, category, categoryadd, categoryupdate, statistic
from .views import companyupdate, supplierupdate, spensesupdate
from .views import repeatsupdate

from django.contrib.auth.views import PasswordResetView 
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView

from .views import LoginView
from .views import LogoutView

handler404 = part_view.handler404
handler500 = part_view.handler500

urlpatterns = [

    path('', part_view.home, name='home' ),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    path('signup/', part_view.register, name='signup'),
    url(r'^index/$', index.as_view(), name='index'),
    url(r'^companylist/$', companylist.as_view(), name='companylist'),
    url(r'^companyadd/$', companyadd.as_view(), name='companyadd'),
    url(r'^companyupdate/(?P<pk>\d+)/$', companyupdate.as_view(), name='companyupdate'),
    url(r'^delete_company/$', part_view.delete_company, name='delete_company'),
    path('supplier/', part_view.supplier, name='supplier'),
    url(r'^supplieradd/$', supplieradd.as_view(), name='supplieradd'),
    url(r'^supplierupdate/(?P<pk>\d+)/$', supplierupdate.as_view(), name='supplierupdate'),
    url(r'^delete_supplier/$', part_view.delete_supplier, name='delete_supplier'),
    
    path('spensesnon/', part_view.spensesnon, name='spensesnon'),
    path('spenses/', part_view.spenses, name='spenses'),
    url(r'^spensesadd/$', spensesadd.as_view(), name='spensesadd'),
    url(r'^spensesupdate/(?P<pk>\d+)/$', spensesupdate.as_view(), name='spensesupdate'),
    url(r'^delete_spense/$', part_view.delete_spense, name='delete_spense'),
    
    path('repeats/', part_view.repeats, name='repeats'),
    url(r'^repeatsupdate/(?P<pk>\d+)/$', repeatsupdate.as_view(), name='repeatsupdate'),
    url(r'^delete_repeat/$', part_view.delete_repeat, name='delete_repeat'),

    path('category/', category.as_view(), name='category'),
    path('categoryadd/', categoryadd.as_view(), name='categoryadd'),
    url(r'^delete_category/$', part_view.delete_category, name='delete_category'),
    url(r'^categoryupdate/(?P<pk>\d+)/$', categoryupdate.as_view(), name='categoryupdate'),
    url(r'^userlist/$', userlist.as_view(), name='userlist'),
    url(r'^delete_user/$', part_view.delete_user, name='delete_user'),
    url(r'^detect_new_user/$', part_view.detect_new_user, name='detect_new_user'),
    url(r'^reset/password/$', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset_email.html'), name='password_reset'),
    url(r'^reset/password/reset/done/$', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    url(r'^change/password/(?P<pk>[0-9]+)/$', PasswordChangeView.as_view(template_name='password_change.html', success_url='/'), name='change_password'),
    url(r'^personallist/(?P<pk>\d+)/$', userinformation.as_view(), name='userinformation'),
    url(r'^personallist_update/(?P<pk>\d+)/$', userinformation_update.as_view(), name='userinformation_update'),
    url(r'^banklist/$', banklist.as_view(), name='banklist'),
    url(r'^bankadd/$', bankadd.as_view(), name='bankadd'),
    url(r'^bankdetail/(?P<pk>\d+)$', bankdetail.as_view(), name='bankdetail'),
    url(r'^add_bank_flag/$', part_view.add_bank_flag, name='add_bank_flag'),
    url(r'^delete_bank/$', part_view.delete_bank, name='delete_bank'),
    url(r'^bank_update/(?P<pk>\d+)/$', bankupdate.as_view(), name='bankupdate'),
    url(r'^statistic/$', statistic.as_view(), name='statistic'),
    url(r'^ajax/stat_category$', part_view.get_stat_category, name='ajax_stat_category'),
    url(r'^ajax/confirm_spense$', part_view.confirm_spense, name='ajax_confirm_spense'),
    url(r'^ajax/cancel_spense$', part_view.cancel_spense, name='ajax_cancel_spense'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




