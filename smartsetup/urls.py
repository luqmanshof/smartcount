from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.admin import AdminSite

# admin.site.site_url = 'localhost'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('list_signup', views.list_signup, name='list_signup'),
    path('edit_signup', views.edit_signup, name='edit_signup'),
    path('edit_signup/(<int:pk>)', views.edit_signup_with_pk,
         name='edit_signup_with_pk'),

    # path('admin/',admin.site.urls),

    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password_form.html'),name='password_change'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/change_password_success.html'), name='password_change_done'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password_form.html'), name='password'),

    path('password_reset', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_page.html'), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_success.html'), name='password_reset_done'),
    path('password_reset_confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_sure.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_completed.html'), name='password_reset_complete'),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),


    path('chartcategory_list', views.chartcategory_list, name='chartcategory_list'),
    path('chartcategory/(<int:pk>)', views.chartcategory, name='chartcategory'),
    path('chartcategory/(<int:pk>)/detail',
         views.ChartCategoryDetail.as_view(), name='chartcategory_detail'),
    path('chartcategory/(<int:pk>)/delete',
         views.ChartCategoryDelete.as_view(), name='chartcategory_delete'),

    path('chartsubcategory_list', views.chartsubcategory_list,
         name='chartsubcategory_list'),
    # path('chartsubcategory',views.chartsubcategory,name='chartsubcategory'),
    path('chartsubcategory/(<int:pk>)',
         views.chartsubcategory, name='chartsubcategory'),
    path('chartsubcategory/(<int:pk>)/detail',
         views.ChartSubCategoryDetail.as_view(), name='chartsubcategory_detail'),
    path('chartsubcategory/(<int:pk>)/delete',
         views.ChartSubCategoryDelete.as_view(), name='chartsubcategory_delete'),

    path('setupinventorycategory_list', views.setupinventorycat_list,
         name='setupinventorycategory_list'),
    path('setupinventorycategory/create',
         views.SetupInventoryCat.as_view(), name='setupinventorycat_create'),
    path('setupinventorycategory/(<int:pk>)/update',
         views.SetupInventoryCatUpdate.as_view(), name='setupinventorycat_update'),
    path('setupinventorycategory/(<int:pk>)/detail',
         views.SetupInventoryCatDetail.as_view(), name='setupinventorycat_detail'),
    path('setupinventorycategory/(<int:pk>)/delete',
         views.SetupInventoryCatDelete.as_view(), name='setupinventorycat_delete'),

    path('setupinventoryitems_list', views.setupinventoryitems_list,
         name='setupinventoryitems_list'),
    path('setupinventoryitems/(<int:pk>)',
         views.setupinventoryitems, name='setupinventoryitems'),
    path('setupinventoryitems/(<int:pk>)/detail',
         views.SetupInventoryItemsDetail.as_view(), name='setupinventoryitems_detail'),
    path('setupinventoryitems/(<int:pk>)/delete',
         views.SetupInventoryItemsDelete.as_view(), name='setupinventoryitems_delete'),

    # SETUP CLIENT
    path('setupclients_list', views.setupclients_list, name='setupclients_list'),
    path('setupclients/(<int:pk>)', views.setupclients, name='setupclients'),
    path('setupclients/(<int:pk>)/detail',
         views.SetupClientsDetail.as_view(), name='setupclients_detail'),
    path('setupclients/(<int:pk>)/delete',
         views.SetupClientsDelete.as_view(), name='setupclients_delete'),

    # SETUP VENDORS
    path('setupvendors_list', views.setupvendors_list, name='setupvendors_list'),
    path('setupvendors/(<int:pk>)', views.setupvendors, name='setupvendors'),
    path('setupvendors/(<int:pk>)/detail',
         views.SetupVendorsDetail.as_view(), name='setupvendors_detail'),
    path('setupvendors/(<int:pk>)/delete',
         views.SetupVendorsDelete.as_view(), name='setupvendors_delete'),

    # RECEIPT
    path('receipt_list', views.receipt_list, name='receipt_list'),
    path('receipt/(<int:pk>)', views.receipt, name='receipt'),

    # EXPENSES
    path('expense_list', views.expense_list, name='expense_list'),
    path('expense/(<int:pk>)', views.expense, name='expense'),

    # Reports
    path('financialperformance', views.financialperformance,
         name='financialperformance'),
    # path('financialperformanceprint',views.financialperformanceprint,name='financialperformanceprint'),
    path('financialposition', views.financialposition, name='financialposition'),
]
