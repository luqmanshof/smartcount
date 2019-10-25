from django.shortcuts import render,redirect,get_object_or_404
from smartsetup.forms import (
    SignUpForm,EditProfileForm,UserProfileForm,ChartCategoryForm,
    ChartSubCategoryForm,SetupInventoryItemsForm,SetupClientsForm,
    SetupVendorsForm,ReceiptMainForm,ReceiptDetailsForm
)
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from smartsetup.models import (
    UserProfile,ChartCategory,ChartSubCategory,SetupClients,SetupVendors,
    SetupInventoryCategory,SetupInventoryItems,SetupClients,SetupVendors,
    ReceiptMain,ReceiptDetails
)
from django.forms.models import model_to_dict
from django.views import generic
from django.urls import reverse_lazy



@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # userprofile_form = UserProfileForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            user = form.save()
            # user = userprofile_form.save( instance=request.user.userprofile)

            # login immediately with the created user profile
            # login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('dashboard')
    else:
        form = SignUpForm()
        # userprofile_form = UserProfileForm()
        args = {'form':form}
        return render(request,'smartsetup/signup.html',args)

@login_required
def list_signup(request):
    users = User.objects.all()
    # fields = model_to_dict(user,fields=['username','first_name','last_name','email'])
    fieldCols = ['User Name','First Name','Last Name','E-Mail']
    return render(request, 'smartsetup/list_signup.html',{'fieldCols':fieldCols,'users':users})

#RECEIPT TRANSACTION
@login_required
def receipt_list(request, pk=None):
    receipts = ReceiptMain.objects
    fieldCols = ['Date','Receipt No.','Description']
    args ={'fieldCols':fieldCols,'receipts':receipts}
    return render(request, 'account/receipt_list.html',args)

@login_required
def receipt(request,pk=None):
    if request.method == 'POST':
        receiptmain_form = ReceiptMainForm(request.POST, instance=request.receiptmain)
        receiptdetails_form = ReceiptDetailsForm(request.POST, instance=request.receiptmain.receiptdetails)

        if receiptmain_form.is_valid() and receiptdetails_form.is_valid():
            receiptmain_form.save()
            receiptdetails_form.save()
            # return redirect('home')
            receipts = ReceiptMain.objects
            receiptdetails = ReceiptMain.ReceiptDetails.objects
            return render(request, 'account/receipt.html',{'receipts':receipts})
    else:
        # receiptmain = request.receiptmain
        receiptmain_form = ReceiptMainForm()
        # latest_receiptno = ReceiptMain.objects.latest('receipt_number') + 1
        receiptdetails_form = ReceiptDetailsForm()
        args = {
            'receiptmain_form':receiptmain_form,'receiptdetails_form':receiptdetails_form
            }
        return render(request,'account/receipt.html',args)


@login_required
def edit_signup(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        # userprofile_obj = UserProfile.objects.all()

        if form.is_valid() and userprofile_form.is_valid():
            form.save()
            userprofile_form.save()
            # return redirect('home')
            users = User.objects
            return render(request, 'smartsetup/list_signup.html',{'users':users})
    else:
        user = request.user
        form = EditProfileForm(instance=user)
        userprofile_form = UserProfileForm(instance=user.userprofile)
        # form = EditProfileForm(instance=request.user)
        # userprofile_form = UserProfileForm(instance=request.user.userprofile)

        args = {'form':form,'userprofile_form':userprofile_form}
        return render(request,'smartsetup/edit_signup.html',args)

@login_required
@permission_required('smartsetup.can_change_user_profile', raise_exception=True)
def edit_signup_with_pk(request, pk=None):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        userprofile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        # userprofile_obj = UserProfile.objects.all()

        if form.is_valid() and userprofile_form.is_valid():
            form.save()
            userprofile_form.save()
            # return redirect('home')
            users = User.objects
            return render(request, 'smartsetup/list_signup.html',{'users':users})

    else:
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        form = EditProfileForm(instance=user)
        # userprofile_form = UserProfileForm(instance=userprofile)
        userprofile_form = UserProfileForm(instance=user.userprofile)

        args = {'form':form,'userprofile_form':userprofile_form}
        return render(request,'smartsetup/edit_signup.html',args)

#SETUP CHART CATEGORY
@login_required
def chartcategory_list(request, pk=None):
    chartcategories = ChartCategory.objects
    fieldCols = ['Category Code','Category Name']
    args ={'fieldCols':fieldCols,'chartcategories':chartcategories}
    return render(request, 'smartsetup/chartcategory_list.html',args)

@login_required
def chartcategory(request, pk=None):
    if request.method == 'POST':
        if pk:
            chartcategory = ChartCategory.objects.get(pk=pk)
            form = ChartCategoryForm(request.POST, instance=chartcategory)
        else:
            form = ChartCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('chartcategory_list')
    else:
        if (pk != 0):
            chartcategory = ChartCategory.objects.get(pk=pk)
            form = ChartCategoryForm(instance=chartcategory)
        else:
            form = ChartCategoryForm()

        args = {'form':form,'title':'Setup Chart category'}
        return render(request,'smartsetup/form.html',args)

class ChartCategoryDetail(generic.DetailView):
    model = ChartCategory
    template_name = 'smartsetup/chartcategory_detail.html'

class ChartCategoryDelete(generic.DeleteView):
    model = ChartCategory
    template_name = 'smartsetup/chartcategory_delete.html'
    success_url = reverse_lazy('chartcategory_list')

##SETUP CHART SUB-CATEGORY (ACCOUNT ITEMS)
@login_required
def chartsubcategory_list(request, pk=None):
    chartcategories = ChartSubCategory.objects
    fieldCols = ['Account Code','Account Name','Notes','Category']
    args ={'fieldCols':fieldCols,'chartcategories':chartcategories}
    return render(request, 'smartsetup/chartsubcategory_list.html',args)

@login_required
def chartsubcategory(request, pk=None):
    if request.method == 'POST':
        if pk:
            chartsubcategory = ChartSubCategory.objects.get(pk=pk)
            form = ChartSubCategoryForm(request.POST, instance=chartsubcategory)
        else:
            form = ChartSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chartsubcategory_list')
    else:
        if (pk != 0):
            chartsubcategory = ChartSubCategory.objects.get(pk=pk)
            form = ChartSubCategoryForm(instance=chartsubcategory)
        else:
            form = ChartSubCategoryForm()
    return render(request,'smartsetup/form.html',{'form':form,'title':'Setup Chart category'})

class ChartSubCategoryDetail(generic.DetailView):
    model = ChartSubCategory
    template_name = 'smartsetup/chartsubcategory_detail.html'

class ChartSubCategoryDelete(generic.DeleteView):
    model = ChartSubCategory
    template_name = 'smartsetup/chartsubcategory_delete.html'
    success_url = reverse_lazy('chartsubcategory_list')

#SETUP INVENTORY CATEGORY
@login_required
def setupinventorycat_list(request, pk=None):
    setupinventorycategory = SetupInventoryCategory.objects
    fieldCols = ['Category Code','Category Name']
    args ={'fieldCols':fieldCols,'setupinventorycategory':setupinventorycategory}
    return render(request, 'smartsetup/setupinvetorycat_list.html',args)

class SetupInventoryCat(generic.CreateView):
    model = SetupInventoryCategory
    fields = ['inventory_category_code','inventory_category_name']
    template_name = 'smartsetup/SetupInventoryCat.html'
    success_url = reverse_lazy('setupinventorycategory_list')

class SetupInventoryCatUpdate(generic.UpdateView):
    model = SetupInventoryCategory
    fields = ['inventory_category_code','inventory_category_name']
    template_name = 'smartsetup/SetupInventoryCat.html'
    success_url = reverse_lazy('setupinventorycategory_list')

class SetupInventoryCatDetail(generic.DetailView):
    model = SetupInventoryCategory
    template_name = 'smartsetup/setupinvetorycat_detail.html'

class SetupInventoryCatDelete(generic.DeleteView):
    model = SetupInventoryCategory
    template_name = 'smartsetup/setupinvetorycat_delete.html'
    success_url = reverse_lazy('setupinventorycategory_list')

#SETUP INVENTORY ITEMS
@login_required
def setupinventoryitems_list(request, pk=None):
    setupinventoryitems = SetupInventoryItems.objects
    fieldCols = ['Inventory Code','Inventory Name','Description','Category']
    args ={'fieldCols':fieldCols,'setupinventoryitems':setupinventoryitems}
    return render(request, 'smartsetup/setupinventoryitems_list.html',args)

@login_required
def setupinventoryitems(request, pk=None):
    if request.method == 'POST':
        if pk:
            setupinventoryitems = SetupInventoryItems.objects.get(pk=pk)
            form = SetupInventoryItemsForm(request.POST, instance=setupinventoryitems)
        else:
            form = SetupInventoryItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setupinventoryitems_list')
    else:
        if (pk != 0):
            setupinventoryitems = SetupInventoryItems.objects.get(pk=pk)
            form = SetupInventoryItemsForm(instance=setupinventoryitems)
        else:
            form = SetupInventoryItemsForm()
    return render(request,'smartsetup/form.html',{'form':form,'title':'Setup Inventory Items'})

class SetupInventoryItemsDetail(generic.DetailView):
    model = SetupInventoryItems
    template_name = 'smartsetup/setupinventoryitems_detail.html'

class SetupInventoryItemsDelete(generic.DeleteView):
    model = SetupInventoryItems
    template_name = 'smartsetup/setupinventoryitems_delete.html'
    success_url = reverse_lazy('setupinventoryitems_list')


#SETUP CLIENTS
@login_required
def setupclients_list(request, pk=None):
    setupclients = SetupClients.objects
    fieldCols = ['Client Name','Address','Phone','Account Officer']
    args ={'fieldCols':fieldCols,'setupclients':setupclients}
    return render(request, 'smartsetup/setupclients_list.html',args)

@login_required
def setupclients(request, pk=None):
    if request.method == 'POST':
        if pk:
            setupclients = SetupClients.objects.get(pk=pk)
            form = SetupClientsForm(request.POST, instance=setupclients)
        else:
            form = SetupClientsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('setupclients_list')
    else:
        if (pk != 0):
            setupclients = SetupClients.objects.get(pk=pk)
            form = SetupClientsForm(instance=setupclients)
        else:
            form = SetupClientsForm()

        args = {'form':form,'title':'Setup Client Account'}
        return render(request,'smartsetup/form.html',args)

class SetupClientsDetail(generic.DetailView):
    model = SetupClients
    template_name = 'smartsetup/setupclients_detail.html'

class SetupClientsDelete(generic.DeleteView):
    model = SetupClients
    template_name = 'smartsetup/setupclients_delete.html'
    success_url = reverse_lazy('setupclients_list')



#SETUP VENDORS
@login_required
def setupvendors_list(request, pk=None):
    setupvendors = SetupVendors.objects
    fieldCols = ['Vendor Name','Address','Phone','Website']
    args ={'fieldCols':fieldCols,'setupvendors':setupvendors}
    return render(request, 'smartsetup/setupvendors_list.html',args)

@login_required
def setupvendors(request, pk=None):
    if request.method == 'POST':
        if pk:
            setupvendors = SetupVendors.objects.get(pk=pk)
            form = SetupVendorsForm(request.POST, instance=setupvendors)
        else:
            form = SetupVendorsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('setupvendors_list')
    else:
        if (pk != 0):
            setupvendors = SetupVendors.objects.get(pk=pk)
            form = SetupVendorsForm(instance=setupvendors)
        else:
            form = SetupVendorsForm()

        args = {'form':form,'title':'Setup Vendor Account'}
        return render(request,'smartsetup/form.html',args)

class SetupVendorsDetail(generic.DetailView):
    model = SetupVendors
    template_name = 'smartsetup/setupvendors_detail.html'

class SetupVendorsDelete(generic.DeleteView):
    model = SetupVendors
    template_name = 'smartsetup/setupvendors_delete.html'
    success_url = reverse_lazy('setupvendors_list')



#REPORTS
@login_required
def financialperformance(request):
    revenues = ChartSubCategory.objects.filter(category_code_id=1)
    expenses = ChartSubCategory.objects.filter(category_code_id=2)

    args = {'revenues':revenues,'expenses':expenses}
    return render (request, 'smartsetup/financialperformance.html',args)
# 
# @login_required
# def financialperformanceprint(request):
#     revenues = ChartSubCategory.objects.filter(category_code_id=1)
#     expenses = ChartSubCategory.objects.filter(category_code_id=2)
#
#     args = {'revenues':revenues,'expenses':expenses}
#     return render (request, 'smartsetup/financialperformance_print.html',args)

@login_required
def financialposition(request, pk=None):
    curr_assets = ChartSubCategory.objects.filter(category_code_id=3)
    curr_liabilities = ChartSubCategory.objects.filter(category_code_id=5)
    noncurr_assets = ChartSubCategory.objects.filter(category_code_id=4)
    noncurr_liabilities = ChartSubCategory.objects.filter(category_code_id=6)

    args = {'curr_assets':curr_assets,'curr_liabilities':curr_liabilities,
            'noncurr_assets':noncurr_assets,'noncurr_liabilities':noncurr_liabilities}
    return render (request, 'smartsetup/financialposition.html',args)
