from django.db import models
from datetime import datetime
import bcrypt
import re


class usersManger(models.Manager):
    def basic_validtor(self, post_data):
        errors = {}
        if len(post_data['clubname']) < 3:
            errors["clubname"] = "Name should be at least 3 characters"
        if len(post_data['registration']) < 8: #Note Here , make it less than 8 just for testing .
            errors["registration"] = "Registraion Number must be 8 numbers"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_pw']:
            errors["confirm_pw"] = "Password doesn't match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['emailaddress']):    # test whether a field matches the pattern            
            errors['emailaddress'] = "Invalid email address!"
        if gymUsers.objects.filter(email=post_data['emailaddress']).exists():
            errors["emailaddress"] = "Email address is already registered!"
        if gymUsers.objects.filter(regNum=post_data['registration']).exists():
            errors["registration"] = "Registration number already exists!"
        return errors

    def basic_informatiom_validator(self, postData):
        error = {}
        if len(postData['firstName']) < 1:
            error['firstName'] = "First Name should be at least 1 character"
        if len(postData['lastName']) < 1:
            error['lastName'] = "Last Name should be at least 1 character"
        if len(postData['birthDate']) < 1:
            error['birthDate'] = "Invalid Birth Date"
        if (len(postData['phone']) == 0) or (len(postData['phone']) != 10):
            error['phone'] = "Invalid Phone Number"
        return error


class gymUsers(models.Model):
    name = models.CharField(max_length=45, null=False)
    address = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=25, null=False)
    phone = models.IntegerField()
    regNum = models.CharField(max_length=45,null=False)
    amount = models.IntegerField()
    password = models.CharField(max_length=45, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = usersManger()

class participants(models.Model):
    participantName = models.CharField(max_length=45, null=True)
    sex = models.CharField(max_length=10, null=False)
    age = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=45, null=False)
    legalNumber = models.IntegerField(null=False)
    phoneNumber = models.IntegerField(null=True)
    midicalHistory = models.TextField(max_length=255, null=True)
    gymUser = models.ForeignKey(
        gymUsers, related_name='gymUser_par_id', on_delete=models.CASCADE)

    def add_participants(request,id):
        participantName=request.POST['participantName']
        sex=request.POST['sex']
        age=request.POST['age']
        email=request.POST['email']
        legalNumber=request.POST['legalNumber']
        phoneNumber=request.POST['phoneNumber']
        midicalHistory=request.POST['midicalHistory']
        obj_id=gymUsers.objects.get(id=id)
        participants.objects.create(participantName=participantName,sex=sex,age=age,email=email,legalNumber=legalNumber,phoneNumber=phoneNumber,midicalHistory=midicalHistory,gym_user=obj_id)


class Subscription(models.Model):
    gymUser = models.ForeignKey(gymUsers, related_name='gymUser_sub_id', on_delete=models.CASCADE)
    participantUser = models.ForeignKey(participants, related_name='participantUser_id', on_delete=models.CASCADE)
    amount = models.IntegerField()
    _from = models.DateField(auto_now_add=True)
    _to = models.DateTimeField(auto_now=True)
    active = models.IntegerField(default=0, null=False)

    def add_subscription(request):
        pass

class Employee(models.Model):
    name = models.CharField(max_length=45)
    employment_id = models.CharField(max_length=45)
    title=models.CharField(max_length=255)
    gym=models.ForeignKey(gymUsers,related_name="employees",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_employee(request):
        pass

def Register(request):
    name = request.POST['clubname']
    address = request.POST['city']
    email = request.POST['emailaddress']
    phone = request.POST['phonenumber']
    regNum = request.POST['registration']
    amount = request.POST['amount']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if (request.POST['confirm_pw'] == password):
        return gymUsers.objects.create(name=name, address=address, email=email, phone=phone, regNum=regNum, amount=amount, password=pw_hash)


def Login(request):
    _gymUsers = gymUsers.objects.filter(email=request.POST['email'])
    if _gymUsers:
        loged_user = _gymUsers[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            request.session['userid'] = loged_user.id
            request.session['username'] = loged_user.name
            return True
        else:
            request.session['LoginAuth'] = "Username or password does not exist"
            return False
    else:
        request.session['LoginAuth'] = "Username or password does not exist"
        return False
