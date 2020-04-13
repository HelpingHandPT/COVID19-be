# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True ========================> done
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior ========================> done
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ad(models.Model):
    adid = models.CharField(db_column='adId', primary_key=True, max_length=36)  # Field name made lowercase.
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=280, blank=True, null=True)
    creationdate = models.DateField(db_column='creationDate')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    helperid = models.ForeignKey('Helper', on_delete=models.CASCADE, db_column='helperId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad'


class AdCategory(models.Model):
    adid = models.OneToOneField(Ad, on_delete=models.CASCADE, db_column='adId', primary_key=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='subCategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ad_category'
        unique_together = (('adid', 'subcategoryid'),)


class Address(models.Model):
    addressid = models.CharField(db_column='addressId', primary_key=True, max_length=36)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.PositiveIntegerField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    verified = models.IntegerField()
    userid = models.ForeignKey('UserEntity', on_delete=models.CASCADE, related_name = '+', db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class AddressProof(models.Model):
    pdfid = models.OneToOneField('Pdf', models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)  # Field name made lowercase.
    pdftype = models.ForeignKey('Pdf', models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='addressId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address_proof'


class AtRisk(models.Model):
    userid = models.OneToOneField('NormalUser', on_delete=models.CASCADE, db_column='userId', primary_key=True)  # Field name made lowercase.
    normaltype = models.ForeignKey('NormalType', models.DO_NOTHING, db_column='normalType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'at_risk'


class AtRiskCategory(models.Model):
    userid = models.OneToOneField(AtRisk, models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='subCategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'at_risk_category'
        unique_together = (('userid', 'subcategoryid'),)


class AtRisksFavourite(models.Model):
    atriskid = models.OneToOneField(AtRisk, on_delete=models.CASCADE, db_column='atRiskId', primary_key=True)  # Field name made lowercase.
    helperid = models.ForeignKey('Helper', on_delete=models.CASCADE, db_column='helperId')  # Field name made lowercase.
    dateselected = models.DateField(db_column='dateSelected', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'at_risks_favourite'
        unique_together = (('atriskid', 'helperid'),)


class AuthGroup(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    categoryid = models.CharField(db_column='categoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    title = models.CharField(max_length=30)
    categorydescription = models.CharField(db_column='categoryDescription', max_length=280, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Credential(models.Model):
    credentialid = models.CharField(db_column='credentialId', primary_key=True, max_length=36)  # Field name made lowercase.
    title = models.CharField(max_length=30)
    dateobtained = models.DateField(db_column='dateObtained')  # Field name made lowercase.
    expirationdate = models.DateField(db_column='expirationDate', blank=True, null=True)  # Field name made lowercase.
    institution = models.CharField(max_length=50)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credential'


class CredentialProof(models.Model):
    pdfid = models.OneToOneField('Pdf', models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)  # Field name made lowercase.
    pdftype = models.ForeignKey('Pdf', models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    credentialid = models.ForeignKey(Credential, on_delete=models.CASCADE, db_column='credentialId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'credential_proof'


class DjangoAdminLog(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.AutoField(unique=True, db_column='id', primary_key=True, max_length=11)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExecutiveType(models.Model):
    executivetypeid = models.IntegerField(db_column='executiveTypeId', primary_key=True)  # Field name made lowercase.
    executivetype = models.CharField(db_column='executiveType', max_length=7)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'executive_type'


class ExecutiveUser(models.Model):
    userid = models.OneToOneField('UserEntity', on_delete=models.CASCADE, db_column='userId', related_name = '+', primary_key=True)  # Field name made lowercase.
    usertype = models.ForeignKey('UserEntity', models.DO_NOTHING, db_column='userType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    executivetype = models.ForeignKey(ExecutiveType, models.DO_NOTHING, db_column='executiveType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'executive_user'


class HealthLog(models.Model):
    patientid = models.OneToOneField('UserEntity', on_delete=models.CASCADE, db_column='patientId', primary_key=True)  # Field name made lowercase.
    monitorid = models.ForeignKey('Monitor', models.DO_NOTHING, db_column='monitorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'health_log'


class HealthLogNote(models.Model):
    healthlognoteid = models.OneToOneField('Note', models.DO_NOTHING, db_column='healthLogNoteId', related_name = '+', primary_key=True)  # Field name made lowercase.
    notetype = models.ForeignKey('Note', models.DO_NOTHING, db_column='noteType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    healthlogid = models.ForeignKey(HealthLog, on_delete=models.CASCADE, db_column='healthLogId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'health_log_note'


class Helper(models.Model):
    userid = models.OneToOneField('NormalUser', on_delete=models.CASCADE, db_column='userId', primary_key=True)  # Field name made lowercase.
    normaltype = models.ForeignKey('NormalType', models.DO_NOTHING, db_column='normalType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'helper'


class HelperCategory(models.Model):
    userid = models.OneToOneField(Helper, models.DO_NOTHING, db_column='userId', primary_key=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='subCategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'helper_category'
        unique_together = (('userid', 'subcategoryid'),)


class HelpersFavourite(models.Model):
    helperid = models.OneToOneField(Helper, on_delete=models.CASCADE, db_column='helperId', primary_key=True)  # Field name made lowercase.
    atriskid = models.ForeignKey(AtRisk, on_delete=models.CASCADE, db_column='atRiskId')  # Field name made lowercase.
    dateselected = models.DateField(db_column='dateSelected', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'helpers_favourite'
        unique_together = (('helperid', 'atriskid'),)


class Image(models.Model):
    userid = models.OneToOneField('UserEntity', on_delete=models.CASCADE, db_column='userId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=40, blank=True, null=True)
    pic = models.TextField()

    class Meta:
        managed = False
        db_table = 'image'


class LogNote(models.Model):
    lognoteid = models.OneToOneField('Note', models.DO_NOTHING, db_column='logNoteId', related_name = '+', primary_key=True)  # Field name made lowercase.
    notetype = models.ForeignKey('Note', models.DO_NOTHING, db_column='noteType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    logid = models.ForeignKey('UserLog', on_delete=models.CASCADE, db_column='logId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_note'


class Monitor(models.Model):
    userid = models.OneToOneField(ExecutiveUser, on_delete=models.CASCADE, db_column='userId', primary_key=True)  # Field name made lowercase.
    executivetype = models.ForeignKey(ExecutiveType, models.DO_NOTHING, db_column='executiveType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monitor'


class NormalType(models.Model):
    normaltypeid = models.IntegerField(db_column='normalTypeId', primary_key=True)  # Field name made lowercase.
    normaltype = models.CharField(db_column='normalType', max_length=7)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'normal_type'


class NormalUser(models.Model):
    userid = models.OneToOneField('UserEntity', on_delete=models.CASCADE, db_column='userId', related_name = '+', primary_key=True)  # Field name made lowercase.
    usertype = models.ForeignKey('UserEntity', models.DO_NOTHING, db_column='userType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    normaltype = models.ForeignKey(NormalType, models.DO_NOTHING, db_column='normalType')  # Field name made lowercase.
    userdescription = models.CharField(db_column='userDescription', max_length=280, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'normal_user'


class Note(models.Model):
    noteid = models.CharField(db_column='noteId', primary_key=True, max_length=36)  # Field name made lowercase.
    authorid = models.ForeignKey('UserEntity', models.DO_NOTHING, db_column='authorId')  # Field name made lowercase.
    creationdate = models.DateField(db_column='creationDate')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=400, blank=True, null=True)
    notetype = models.ForeignKey('NoteType', models.DO_NOTHING, db_column='noteType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'note'


class NoteType(models.Model):
    notetypeid = models.IntegerField(db_column='noteTypeId', primary_key=True)  # Field name made lowercase.
    notetype = models.CharField(db_column='noteType', max_length=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'note_type'


class Payment(models.Model):
    paymentid = models.CharField(db_column='paymentId', primary_key=True, max_length=36)  # Field name made lowercase.
    paymentvalue = models.DecimalField(db_column='paymentValue', max_digits=6, decimal_places=2)  # Field name made lowercase.
    paymentdatetime = models.DateTimeField(db_column='paymentDateTime')  # Field name made lowercase.
    method = models.CharField(max_length=6)
    originiban = models.CharField(db_column='originIBAN', max_length=25)  # Field name made lowercase.
    destinationiban = models.CharField(db_column='destinationIBAN', max_length=25)  # Field name made lowercase.
    approved = models.IntegerField()
    subsidised = models.IntegerField()
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentProof(models.Model):
    pdfid = models.OneToOneField('Pdf', models.DO_NOTHING, db_column='pdfId', related_name = '+', primary_key=True)  # Field name made lowercase.
    pdftype = models.ForeignKey('Pdf', models.DO_NOTHING, db_column='pdfType', related_name = '+', blank=True, null=True)  # Field name made lowercase.
    paymentid = models.ForeignKey(Payment, models.DO_NOTHING, db_column='paymentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_proof'


class Pdf(models.Model):
    pdfid = models.CharField(db_column='pdfId', primary_key=True, max_length=36)  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='uploadTime')  # Field name made lowercase.
    title = models.CharField(max_length=30)
    pdffile = models.CharField(db_column='pdfFile', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pdftype = models.ForeignKey('PdfType', models.DO_NOTHING, db_column='pdfType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdf'


class PdfType(models.Model):
    pdftypeid = models.IntegerField(db_column='pdfTypeId', primary_key=True)  # Field name made lowercase.
    pdftype = models.CharField(db_column='pdfType', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdf_type'


class Request(models.Model):
    requestid = models.CharField(db_column='requestId', primary_key=True, max_length=36)  # Field name made lowercase.
    datecreated = models.DateField(db_column='dateCreated')  # Field name made lowercase.
    periodicity = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    requestdescription = models.CharField(db_column='requestDescription', max_length=280, blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateField(db_column='expirationDate', blank=True, null=True)  # Field name made lowercase.
    done = models.IntegerField(blank=True, null=True)
    atriskid = models.ForeignKey(AtRisk, models.DO_NOTHING, db_column='atRiskId')  # Field name made lowercase.
    helperid = models.ForeignKey(Helper, models.DO_NOTHING, db_column='helperId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'


class RequestCategory(models.Model):
    requestid = models.OneToOneField(Request, models.DO_NOTHING, db_column='requestId', primary_key=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='subCategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request_category'
        unique_together = (('requestid', 'subcategoryid'),)


class Review(models.Model):
    reviewid = models.CharField(db_column='reviewId', primary_key=True, max_length=36)  # Field name made lowercase.
    reviewingid = models.CharField(db_column='reviewingId', max_length=36)  # Field name made lowercase.
    reviewedid = models.CharField(db_column='reviewedId', max_length=36)  # Field name made lowercase.
    reviewdescription = models.CharField(db_column='reviewDescription', max_length=280, blank=True, null=True)  # Field name made lowercase.
    rating = models.PositiveIntegerField(blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.
    requestid = models.ForeignKey(Request, models.DO_NOTHING, db_column='requestId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class SocialMedia(models.Model):
    userid = models.OneToOneField('UserEntity', on_delete=models.CASCADE, db_column='userId', related_name = '+', primary_key=True)  # Field name made lowercase.
    facebook = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(db_column='linkedIn', max_length=61, blank=True, null=True)  # Field name made lowercase.
    instagram = models.CharField(max_length=30, blank=True, null=True)
    reddit = models.CharField(max_length=20, blank=True, null=True)
    skype = models.CharField(max_length=32, blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'social_media'


class SubCategory(models.Model):
    subcategoryid = models.CharField(db_column='subCategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    title = models.CharField(max_length=30)
    subcategorydescription = models.CharField(db_column='subCategoryDescription', max_length=280, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='categoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_category'


class UserAdmin(models.Model):
    userid = models.OneToOneField(ExecutiveUser, on_delete=models.CASCADE, db_column='userId', primary_key=True)  # Field name made lowercase.
    executivetype = models.ForeignKey(ExecutiveType, models.DO_NOTHING, db_column='executiveType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_admin'


class UserEntity(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=20)
    userpassword = models.CharField(db_column='userPassword', max_length=256)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=50)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    activestatus = models.IntegerField(db_column='activeStatus')  # Field name made lowercase.
    lastaccess = models.DateField(db_column='lastAccess')  # Field name made lowercase.
    creationdate = models.DateField(db_column='creationDate')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate')  # Field name made lowercase.
    usertype = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_entity'


class UserLog(models.Model):
    logid = models.CharField(db_column='logId', primary_key=True, max_length=36)  # Field name made lowercase.
    ip = models.CharField(max_length=15, blank=True, null=True)
    hostname = models.CharField(db_column='hostName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isp = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.PositiveIntegerField(db_column='zipCode', blank=True, null=True)  # Field name made lowercase.
    lat = models.DecimalField(max_digits=7, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    logdate = models.DateTimeField(db_column='logDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(UserEntity, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_log'


class UserNote(models.Model):
    usernoteid = models.OneToOneField(Note, models.DO_NOTHING, db_column='userNoteId', related_name = '+', primary_key=True)  # Field name made lowercase.
    notetype = models.ForeignKey(Note, models.DO_NOTHING, db_column='noteType', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(UserEntity, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_note'


class UserType(models.Model):
    usertypeid = models.IntegerField(db_column='userTypeId', primary_key=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=9)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_type'
