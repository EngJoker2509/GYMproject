from django.db import models
from datetime import datetime, timedelta
import bcrypt
import re


class usersManger(models.Manager):
    def basic_validtor(self, post_data):
        errors = {}
        if len(post_data['clubname']) < 3:
            errors["clubname"] = "Name should be at least 3 characters"
        # Note Here , make it less than 8 just for testing .
        if len(post_data['registration']) < 8:
            errors["registration"] = "Registraion Number must be 8 numbers"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_pw']:
            errors["confirm_pw"] = "Password doesn't match"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(post_data['emailaddress']):
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
    regNum = models.CharField(max_length=45, null=False)
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

    def add_participants(postData, id):
        participantName = postData['participantName']
        sex = postData['sex']
        age = postData['age']
        email = postData['email']
        legalNumber = postData['legalNumber']
        phoneNumber = postData['phoneNumber']
        midicalHistory = postData['medicalHistory']

        obj_id = gymUsers.objects.get(id=id)
        newparticipant = participants.objects.create(participantName=participantName, sex=sex, age=age, email=email,
        legalNumber=legalNumber, phoneNumber=phoneNumber, midicalHistory=midicalHistory, gymUser=obj_id)
        par_obj_id = newparticipant.id
        print(par_obj_id)
        gym_obj_id = obj_id.id
        print(gym_obj_id)
        amount = postData['amount']
        now = datetime.now()
        today = now.date()
        _to = today+timedelta(days=30)
        Subscription.add_subscription(amount, gym_obj_id, par_obj_id, _to)

    def allParticipants(gymId):
        return participants.objects.filter(gymUser=gymId).order_by('-id')


class Subscription(models.Model):
    gymUser = models.ForeignKey(
        gymUsers, related_name='gymUser_sub_id', on_delete=models.CASCADE)
    participantUser = models.ForeignKey(
        participants, related_name='participantUser_id', on_delete=models.CASCADE)
    amount = models.IntegerField()
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateTimeField(null=True)
    active = models.IntegerField(default=0, null=False)

    def add_subscription(amount, gym_obj_id, par_obj_id, _to):
        gym = gymUsers.objects.get(id=gym_obj_id)
        participant = participants.objects.get(id=par_obj_id)
        amount = amount
        Subscription.objects.create(
            gymUser=gym, participantUser=participant, amount=amount, to_date=_to)

    def update_active(today,id):
        if(Subscription.objects.exclude(to_date__gte=today).filter(gymUser=id).exists()):
            _non_active = Subscription.objects.exclude(to_date__gte=today).filter(gymUser=id)
            for non_active in _non_active:
                non_active.active = 1 
                non_active.save()
        
        return 

class Employee(models.Model):
    name = models.CharField(max_length=45)
    employment_id = models.CharField(max_length=45)
    title = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=10, null=True)
    gym = models.ForeignKey(
        gymUsers, related_name="employees", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_employee(postData, gym_id):
        name = postData['employeename']
        employment_id = postData['idnumber']
        title = postData['title']
        phonenumber = postData['phonenumber']
        gym = gymUsers.objects.get(id=gym_id)
        new_employee = Employee.objects.create(name=name, employment_id=employment_id, title=title,
        phonenumber=phonenumber, gym=gym)

        return new_employee
    
    def delete_employee(id):
        employee=Employee.objects.get(id=id)
        employee.delete()


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
