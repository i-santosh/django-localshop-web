import json
from .sendVerificationCode import generateVerificationCode
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import Product, CUser, CategoriesList, SubCategoriesList
from django.contrib.auth.decorators import login_required

# Create your views here.

def getProductCategories():
    allData = Product.objects.all()
    productCategories = [ cat.category for cat in allData ]
    return productCategories

def getcategoryImage():
    productCategoriesImg = CategoriesList.objects.all()
    return productCategoriesImg

def getSubCategoryImage():
    subCategoryImage = SubCategoriesList.objects.all()
    return subCategoryImage

#@login_required(login_url = "/accounts/signin")
def index(request):
    return render(request,"index.html",context={"productCategories":getProductCategories(),"categoriesImage":getcategoryImage(),"SubCategoriesList":getSubCategoryImage()})


def sendVerificationCode(request=None,userEmail=None):
    if request.user.is_authenticated:
        return index(request)
    if userEmail is None:
        userEmail = request.session.get("email")
        if userEmail is None:
            return redirect("signupGetData")
    else:
        generated = generateVerificationCode(userEmail)
        return generated

class SignUp:
    def signupGetData(request):
        if request.user.is_authenticated:
            return redirect("home")
        if request.method == "POST":
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            username = request.POST.get('username')
            password = request.POST.get('password1')
            alreadAccount = "Looks like you already have an account!"
            if CUser.objects.filter(email=email).exists():
                messages.warning(request,alreadAccount)
                return redirect("signupGetData")
            elif CUser.objects.filter(username=username).exists():
                messages.warning(request,"Username already taken")
                return redirect("signupGetData")
            elif CUser.objects.filter(phone_number=phone).exists():
                messages.warning(request,alreadAccount)
                return redirect("signupGetData")
            else:
                generatedVerificationCode = sendVerificationCode(request=request,userEmail=email)
                request.session["first_name"] = firstname,
                request.session["last_name"] = lastname,
                request.session["password"] = password,
                request.session["email"] = email,
                request.session["username"] = username
                request.session["phone_number"] = phone
                request.session["verificationCode"] = generatedVerificationCode
                request.session.set_expiry(600)
                return render(request,"accountVerification.html",{"email":email})
        else:
            return render(request,'signup.html')

    def signupFinishByVerifyCode(request):
        if request.user.is_authenticated:
            return redirect("home")
        if request.method == "POST":
            userEmail = request.session.get("email")
            userInputCode = request.POST.get("userInputCode")
            if request.session.get("verificationCode") is None:
                messages.warning(request,"Your Verification Code is expired! Try to Resend again")
                return redirect("signupFinishByVerifyCode")
            generatedVerificationCode = request.session["verificationCode"]
            if int(userInputCode) == int(generatedVerificationCode):
                Ufirst_name = request.session.get("first_name")[0]
                Ulast_name = request.session.get("last_name")[0]
                Upassword = request.session.get("password")[0]
                Uemail = request.session.get("email")[0]
                Uusername = request.session.get("username")
                Uphone_number = request.session.get("phone_number")
                data = [Ufirst_name,Ulast_name,Upassword,Uusername,Uemail,Uphone_number]
                for metadata in data:
                    if metadata is None:
                        return redirect('signupGetData')
                user = CUser.objects.create_user(
                    first_name = Ufirst_name,
                    last_name = Ulast_name,
                    password = Upassword,
                    email = Uemail,
                    username = Uusername,
                    phone_number = Uphone_number,
                    pwd = Upassword,
                )
                user.save()
                user = authenticate(request,username=Uusername,password=Upassword)
                if user is not None:
                    auth_login(request,user)
                    return redirect("home")
                else:
                    return redirect('signin')
            else:
                messages.warning(request,"Invalid Code!")
                return redirect("signupFinishByVerifyCode")
        else:
            userEmail = request.session.get("email")
            return render(request,"accountVerification.html",{"email":userEmail})

    def resendCode(request):
        if request.user.is_authenticated:
            return redirect("home")
        if request.session.get("email") is None:
            return redirect("signupGetData")
        else:
            userEmail = request.session.get("email")[0]
            generatedVerificationCode = sendVerificationCode(userEmail=userEmail)
            request.session["verificationCode"] = generatedVerificationCode
            request.session.set_expiry(600)
            return render(request,"accountVerification.html",{"email":userEmail})

def signout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('home')
    else:
        return redirect("home")

def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        try:
            obj = CUser.objects.get(email=username)
        except Exception as e:
            try:
                obj = CUser.objects.get(phone_number=username)
            except Exception as e:
                messages.error(request, "Invalid Username or Password ")
                return redirect('signin')
        user = authenticate(request,username=obj.username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password ")
            return redirect("signin")
    return render(request,'signin.html')

@login_required(login_url="/accounts/signin")
def orders(request):
    return render(request,'orders.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def subscribeAndSave(request):
    return render(request,'subscribeAndSave.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def editProfile(request):
    return render(request,'editProfile.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def manageAddresses(request):
    return render(request,'manageAddresses.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def purchaseSettings(request):
    return render(request,'purchaseSettings.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def deleteMyAccount(request):
    return render(request,'deleteMyAccount.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def emailAlertPreferences(request):
    return render(request,'emailAlertPreferences.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def contactUs(request):
    return render(request,'contactUs.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def feedback(request):
    return render(request,'feedback.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def privacyNotice(request):
    return render(request,'privacyNotice.html',context={"productCategories":getProductCategories()})

@login_required(login_url="/accounts/signin")
def account(request):
    return render(request,"account.html",context={"productCategories":getProductCategories()})
