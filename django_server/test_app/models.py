#   Keep # in `# managed = False` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from test_app import validators
import datetime

#USERNAME_MIN_LENGTH = 5
#USERNAME_MAX_LENGTH = 20

class MyUserManager(BaseUserManager):
    def _create_generic_user(self, email, username, password, first_name, last_name, user_type):
        if not username:
            raise ValueError("Username cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not password:
            raise ValueError("Password cannot be empty")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            user_type=user_type,
            is_staff=user_type == 0,
            is_active=False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_admin(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 0)
        
    def create_monitor(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 100)

    def create_atrisk(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 200)

    def create_helper(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 201)

class MyUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        # managed = False
        db_table = 'user_entity'

    USER_TYPE_CHOICES = (
        (0, 'admin'),
        (100, 'monitor'),
        (200, 'atRisk'),
        (201, 'helper'),
        (256, 'unspecified'),
    )
    
    user_id = models.AutoField(primary_key=True, db_column='userId')
    #username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True, validators=[validators.validate_username])
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(db_column='userPassword', max_length=256)
    first_name = models.CharField(db_column='firstName', max_length=25)
    last_name = models.CharField(db_column='lastName', max_length=25)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    last_access = models.DateField(db_column='lastAccess', default=datetime.date.today)
    creation_date = models.DateTimeField(db_column='creationDate', default=timezone.now)
    last_update = models.DateField(db_column='lastUpdate', default=datetime.date.today)
    user_type = models.IntegerField(db_column='userType', choices=USER_TYPE_CHOICES, null=True)
    is_staff = models.BooleanField(db_column='isStaff', default=False)
    is_active = models.BooleanField(default=True, db_column='activeStatus')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.email)

    def has_perm(self, perm, obj=None):
        return self.user_type == 0

    def has_module_perms(self, app_label):
        return True

class Ad(models.Model):#===============================================================> READY
    ad_id = models.CharField(db_column='adId', primary_key=True, max_length=36)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=280, blank=True, null=True)
    creation_date = models.DateField(db_column='creationDate')
    last_update = models.DateTimeField(db_column='lastUpdate')
    helper_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='helperId', limit_choices_to={'user_type': 201})

    class Meta:
       # managed = False
        db_table = 'ad'

class Category(models.Model):#===============================================================> READY
    category_id = models.CharField(db_column='categoryId', primary_key=True, max_length=36)
    title = models.CharField(max_length=30)
    category_description = models.CharField(db_column='categoryDescription', max_length=280, blank=True, null=True)

    class Meta:
       # managed = False
        db_table = 'category'

class SubCategory(models.Model):#===============================================================> READY
    subcategory_id = models.CharField(db_column='subCategoryId', primary_key=True, max_length=36)
    title = models.CharField(max_length=30)
    subcategory_description = models.CharField(db_column='subCategoryDescription', max_length=280, blank=True, null=True)
    category_id = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')

    class Meta:
      #  managed = False
        db_table = 'sub_category'

class AdCategory(models.Model):#===============================================================> READY
    ad_id = models.OneToOneField(Ad, models.DO_NOTHING, db_column='adId', primary_key=True)
    subcategory_id = models.ForeignKey(SubCategory, models.DO_NOTHING, db_column='subCategoryId')

    class Meta:
      #  managed = False
        db_table = 'ad_category'
        unique_together = (('ad_id', 'subcategory_id'),)

class AtRiskCategory(models.Model):#===============================================================> READY
    atrisk_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='atRiskId', limit_choices_to={'user_type': 200}, primary_key=True)
    subcategory_id = models.ForeignKey(SubCategory, models.DO_NOTHING, db_column='subCategoryId')


    class Meta:
     #   managed = False
        db_table = 'at_risk_category'
        unique_together = (('atrisk_id', 'subcategory_id'),)

class AtRisksFavourite(models.Model):#===============================================================> READY
    atrisk_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='atRiskId', limit_choices_to={'user_type': 200}, primary_key=True)
    helper_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='helperId', related_name='+', limit_choices_to={'user_type': 201})
    date_selected = models.DateField(db_column='dateSelected', blank=True, null=True)

    class Meta:
     #   managed = False
        db_table = 'at_risks_favourite'
        unique_together = (('atrisk_id', 'helper_id'),)

class PdfType(models.Model):#===============================================================> READY
    pdf_type_id = models.IntegerField(db_column='pdfTypeId', primary_key=True)
    pdf_type = models.CharField(db_column='pdfType', max_length=15)


    class Meta:
     #   managed = False
        db_table = 'pdf_type'

class Pdf(models.Model):#===============================================================> READY
    pdf_id = models.CharField(db_column='pdfId', primary_key=True, max_length=36)
    upload_time = models.DateTimeField(db_column='uploadTime')
    title = models.CharField(max_length=30)
    pdf_file = models.CharField(db_column='pdfFile', max_length=256, blank=True, null=True)
    pdftype = models.ForeignKey(PdfType, models.DO_NOTHING, db_column='pdfType')

    class Meta:
     #   managed = False
        db_table = 'pdf'

class Address(models.Model):#===============================================================> READY
    address_id = models.CharField(db_column='addressId', primary_key=True, max_length=36)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.PositiveIntegerField(db_column='zipCode', blank=True, null=True)
    last_update = models.DateTimeField(db_column='lastUpdate')
    verified = models.IntegerField()
    user_id = models.ForeignKey(MyUser, models.DO_NOTHING, related_name = '+', db_column='userId')

    class Meta:
      #  managed = False
        db_table = 'address'

class AddressProof(models.Model):#===============================================================> READY
    pdf_id = models.OneToOneField(Pdf, models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)
    pdf_type = models.ForeignKey(Pdf, models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)
    address_id = models.ForeignKey(Address, models.DO_NOTHING, db_column='addressId')

    class Meta:
      #  managed = False
        db_table = 'address_proof'

class Credential(models.Model):#===============================================================> READY
    credential_id = models.CharField(db_column='credentialId', primary_key=True, max_length=36)
    title = models.CharField(max_length=30)
    date_obtained = models.DateField(db_column='dateObtained')
    expiration_date = models.DateField(db_column='expirationDate', blank=True, null=True)
    institution = models.CharField(max_length=50)
    verified = models.IntegerField()

    class Meta:
      #  managed = False
        db_table = 'credential'

class CredentialProof(models.Model):#===============================================================> READY
    pdf_id = models.OneToOneField(Pdf, models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)
    pdf_type = models.ForeignKey(Pdf, models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)
    credential_id = models.ForeignKey(Credential, models.DO_NOTHING, db_column='credentialId')

    class Meta:
      #  managed = False
        db_table = 'credential_proof'

class HealthLog(models.Model):#===============================================================> READY
    patient_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='userId', limit_choices_to={'user_type': 200, 'user_type': 201}, primary_key=True)
    monitor_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='monitorId',related_name='+', limit_choices_to={'user_type': 100})

    class Meta:
      #  managed = False
        db_table = 'health_log'

class NoteType(models.Model):#===============================================================> READY
    note_type_id = models.IntegerField(db_column='noteTypeId', primary_key=True)
    note_type = models.CharField(db_column='noteType', max_length=9)

    class Meta:
      #  managed = False
        db_table = 'note_type'

class Note(models.Model):#===============================================================> READY
    note_id = models.CharField(db_column='noteId', primary_key=True, max_length=36)
    author_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='authorId')
    creation_date = models.DateField(db_column='creationDate')
    last_update = models.DateTimeField(db_column='lastUpdate')
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=400, blank=True, null=True)
    note_type = models.ForeignKey(NoteType, models.DO_NOTHING, db_column='noteType')

    class Meta:
      #  managed = False
        db_table = 'note'

class HealthLogNote(models.Model):#===============================================================> READY
    health_log_note_id = models.OneToOneField(Note, models.DO_NOTHING, db_column='healthLogNoteId', related_name = '+', primary_key=True)
    note_type = models.ForeignKey(Note, models.DO_NOTHING, db_column='noteType', related_name = '+', blank=True, null=True)
    health_log_id = models.ForeignKey(HealthLog, models.DO_NOTHING, db_column='healthLogId')

    class Meta:
      #  managed = False
        db_table = 'health_log_note'

class HelperCategory(models.Model):#===============================================================> READY
    helper_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='helperId', limit_choices_to={'user_type': 201}, primary_key=True)
    subcategory_id = models.ForeignKey(SubCategory, models.DO_NOTHING, db_column='subCategoryId')

    class Meta:
      #  managed = False
        db_table = 'helper_category'
        unique_together = (('helper_id', 'subcategory_id'),)

class HelpersFavourite(models.Model):#===============================================================> READY
    helper_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='helperId', limit_choices_to={'user_type': 201}, primary_key=True)
    atrisk_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='atRiskId',related_name='+', limit_choices_to={'user_type': 200})
    date_selected = models.DateField(db_column='dateSelected', blank=True, null=True)

    class Meta:
      #  managed = False
        db_table = 'helpers_favourite'
        unique_together = (('helper_id', 'atrisk_id'),)

class Image(models.Model):#===============================================================> READY
    user_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='userId', primary_key=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    pic = models.TextField()

    class Meta:
      #  managed = False
        db_table = 'image'

class UserLog(models.Model):#===============================================================> READY
    log_id = models.CharField(db_column='logId', primary_key=True, max_length=36)
    ip = models.CharField(max_length=15, blank=True, null=True)
    host_name = models.CharField(db_column='hostName', max_length=20, blank=True, null=True)
    isp = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.PositiveIntegerField(db_column='zipCode', blank=True, null=True)
    lat = models.DecimalField(max_digits=7, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    log_date = models.DateTimeField(db_column='logDate', blank=True, null=True)
    user_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='userId')

    class Meta:
      #  managed = False
        db_table = 'user_log'

class UserNote(models.Model):#===============================================================> READY
    user_note_id = models.OneToOneField(Note, models.DO_NOTHING, db_column='userNoteId', related_name = '+', primary_key=True)
    note_type = models.ForeignKey(Note, models.DO_NOTHING, db_column='noteType', blank=True, null=True)
    user_id = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='userId')

    class Meta:
     #   managed = False
        db_table = 'user_note'

class LogNote(models.Model):#===============================================================> READY
    log_note_id = models.OneToOneField(Note, models.DO_NOTHING, db_column='logNoteId', related_name = '+', primary_key=True)
    note_type = models.ForeignKey(Note, models.DO_NOTHING, db_column='noteType', related_name = '+', blank=True, null=True)
    log_id = models.ForeignKey(UserLog, models.DO_NOTHING, db_column='logId')

    class Meta:
     #   managed = False
        db_table = 'log_note'

class Request(models.Model):#===============================================================> READY
    request_id = models.CharField(db_column='requestId', primary_key=True, max_length=36)
    date_created = models.DateField(db_column='dateCreated')
    periodicity = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    request_description = models.CharField(db_column='requestDescription', max_length=280, blank=True, null=True)
    expiration_date = models.DateField(db_column='expirationDate', blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)
    atrisk = models.ForeignKey(MyUser, models.DO_NOTHING, limit_choices_to={'user_type': 200})
    helper = models.ForeignKey(MyUser, models.DO_NOTHING,related_name='+', limit_choices_to={'user_type': 201})

    class Meta:
      #  managed = False
        db_table = 'request'

class Payment(models.Model):#===============================================================> READY
    payment_id = models.CharField(db_column='paymentId', primary_key=True, max_length=36)
    payment_value = models.DecimalField(db_column='paymentValue', max_digits=6, decimal_places=2)
    payment_date_time = models.DateTimeField(db_column='paymentDateTime')
    method = models.CharField(max_length=6)
    origin_iban = models.CharField(db_column='originIBAN', max_length=25)
    destination_iban = models.CharField(db_column='destinationIBAN', max_length=25)
    approved = models.IntegerField()
    subsidised = models.IntegerField()
    request_id = models.ForeignKey(Request, models.DO_NOTHING, db_column='requestId')

    class Meta:
      #  managed = False
        db_table = 'payment'


class PaymentProof(models.Model):#===============================================================> READY
    pdf_id = models.OneToOneField(Pdf, models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)
    pdf_type = models.ForeignKey(Pdf, models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)
    payment_id = models.ForeignKey(Payment, models.DO_NOTHING, db_column='paymentId')

    class Meta:
      #  managed = False
        db_table = 'payment_proof'

class RequestCategory(models.Model):#===============================================================> READY
    request_id = models.OneToOneField(Request, models.DO_NOTHING, db_column='requestId', primary_key=True)
    subcategory_id = models.ForeignKey(SubCategory, models.DO_NOTHING, db_column='subCategoryId')

    class Meta:
      #  managed = False
        db_table = 'request_category'
        unique_together = (('request_id', 'subcategory_id'),)


class Review(models.Model):#===============================================================> READY
    review_id = models.CharField(db_column='reviewId', primary_key=True, max_length=36)
    reviewing_id = models.CharField(db_column='reviewingId', max_length=36)
    reviewed_id = models.CharField(db_column='reviewedId', max_length=36)
    review_description = models.CharField(db_column='reviewDescription', max_length=280, blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    last_update = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)
    request_id = models.ForeignKey(Request, models.DO_NOTHING, db_column='requestId')

    class Meta:
      #  managed = False
        db_table = 'review'

class SocialMedia(models.Model):#===============================================================> READY
    user_id = models.OneToOneField(MyUser, models.DO_NOTHING, db_column='userId', related_name = '+', primary_key=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(db_column='linkedIn', max_length=61, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    reddit = models.CharField(max_length=20, blank=True, null=True)
    skype = models.CharField(max_length=32, blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)
    last_update = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)

    class Meta:
      #  managed = False
        db_table = 'social_media'
