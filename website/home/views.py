from email.errors import MessageError
from pprint import pprint
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import clsUser,clsItem
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        strUserName = request.POST.get('txtUserName')
        strActualName = request.POST.get('txtActualName')
        strPassword = request.POST.get('txtPassword')

        # // User Already Exist Checking
        tbmUser = clsUser.objects.filter(Q(vhr_user_name__iexact=strUserName))
        try:
            if tbmUser[0]:
                print('User Already Exists!') 
        except Exception as err:
            # // Save New User
            tbmUser = clsUser()
            tbmUser.vhr_user_name = strUserName
            tbmUser.vhr_actual_name = strActualName
            tbmUser.vhr_password = strPassword
            tbmUser.save()

        return redirect('signin')
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        strUserName = request.POST.get('txtUserName')
        strPassword = request.POST.get('txtPassword')

        # // Check User Authentication
        tbmUser = clsUser.objects.filter(Q(vhr_user_name__iexact=strUserName),Q(vhr_password=strPassword))
        try:
            if tbmUser[0]:
                request.session['intLoginUserId'] = tbmUser[0].pk_user_id
                request.session['strLoginUserName'] = tbmUser[0].vhr_user_name
                request.session['strLoginActualName'] = tbmUser[0].vhr_actual_name
                messages.success(request,'Signin Success!')
                return redirect('additems')
        except Exception as err:
            return redirect('signin')
    else:
        return render(request,'signin.html')

def additems(request):
    if request.method == 'POST':
        strItemName = request.POST.get('txtItemName')
        strItemCategory = request.POST.get('cmbItemCategory')
        strItemDescription = request.POST.get('txaItemDescription')
        fltPrice = request.POST.get('txtItemPrice')

        # // Item Already Exist Checking
        tbmItem = clsItem.objects.filter(Q(vhr_item_name__iexact=strItemName))
        try:
            if tbmItem[0]:
                messages.success(request,'Item Already Exists.Please Choose Another Name!')
        except Exception as err:
            tbmItem = clsItem()
            tbmItem.vhr_item_name = strItemName
            tbmItem.vhr_item_category = strItemCategory
            tbmItem.txt_item_description = strItemDescription
            tbmItem.dbl_price = fltPrice
            tbmItem.save()
            messages.success(request,'Item added successfully!')
        return render(request,'additems.html')
    else:
        return render(request,'additems.html')

def viewitems(request):
    tbmItems = clsItem.objects.all()
    lstAllItems = []
    for tbmEachItem in tbmItems:
        dctAllItems = {}
        dctAllItems['intPkItemId'] = tbmEachItem.pk_item_id
        dctAllItems['strItemName'] = tbmEachItem.vhr_item_name
        dctAllItems['strItemDescription'] = tbmEachItem.txt_item_description
        dctAllItems['fltItemPrice'] = tbmEachItem.dbl_price
        lstAllItems.append(dctAllItems)

    return render(request,'viewitems.html',{'lstAllItems':lstAllItems})

def signout(request):
    request.session['intLoginUserId'] = None
    request.session['strLoginUserName'] = ''
    request.session['strLoginActualName'] = ''
    messages.success(request,'Signout Success!')
    return redirect('index')

    

