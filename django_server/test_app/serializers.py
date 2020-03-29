from rest_framework.serializers import ModelSerializer
from test_app.models import Ad, AdCategory, Address, AddressProof, AtRisk, AtRiskCategory, AtRisksFavourite, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Category, Credential, CredentialProof, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, ExecutiveType, ExecutiveUser, HealthLog, HealthLogNote, Helper, HelperCategory, HelpersFavourite, Image, LogNote, Monitor, NormalType, NormalUser, Note, NoteType, Payment, PaymentProof, Pdf, PdfType, Request, RequestCategory, Review, SocialMedia, SubCategory, UserAdmin, UserEntity, UserLog, UserNote, UserType


class AdSerializer(ModelSerializer):

    class Meta:
        model = Ad
        fields = '__all__'


class AdCategorySerializer(ModelSerializer):

    class Meta:
        model = AdCategory
        fields = '__all__'


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class AddressProofSerializer(ModelSerializer):

    class Meta:
        model = AddressProof
        fields = '__all__'


class AtRiskSerializer(ModelSerializer):

    class Meta:
        model = AtRisk
        fields = '__all__'


class AtRiskCategorySerializer(ModelSerializer):

    class Meta:
        model = AtRiskCategory
        fields = '__all__'


class AtRisksFavouriteSerializer(ModelSerializer):

    class Meta:
        model = AtRisksFavourite
        fields = '__all__'


class AuthGroupSerializer(ModelSerializer):

    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(ModelSerializer):

    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(ModelSerializer):

    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CredentialSerializer(ModelSerializer):

    class Meta:
        model = Credential
        fields = '__all__'


class CredentialProofSerializer(ModelSerializer):

    class Meta:
        model = CredentialProof
        fields = '__all__'


class DjangoAdminLogSerializer(ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(ModelSerializer):

    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(ModelSerializer):

    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(ModelSerializer):

    class Meta:
        model = DjangoSession
        fields = '__all__'


class ExecutiveTypeSerializer(ModelSerializer):

    class Meta:
        model = ExecutiveType
        fields = '__all__'


class ExecutiveUserSerializer(ModelSerializer):

    class Meta:
        model = ExecutiveUser
        fields = '__all__'


class HealthLogSerializer(ModelSerializer):

    class Meta:
        model = HealthLog
        fields = '__all__'


class HealthLogNoteSerializer(ModelSerializer):

    class Meta:
        model = HealthLogNote
        fields = '__all__'


class HelperSerializer(ModelSerializer):

    class Meta:
        model = Helper
        fields = '__all__'


class HelperCategorySerializer(ModelSerializer):

    class Meta:
        model = HelperCategory
        fields = '__all__'


class HelpersFavouriteSerializer(ModelSerializer):

    class Meta:
        model = HelpersFavourite
        fields = '__all__'


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class LogNoteSerializer(ModelSerializer):

    class Meta:
        model = LogNote
        fields = '__all__'


class MonitorSerializer(ModelSerializer):

    class Meta:
        model = Monitor
        fields = '__all__'


class NormalTypeSerializer(ModelSerializer):

    class Meta:
        model = NormalType
        fields = '__all__'


class NormalUserSerializer(ModelSerializer):

    class Meta:
        model = NormalUser
        fields = '__all__'


class NoteSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class NoteTypeSerializer(ModelSerializer):

    class Meta:
        model = NoteType
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentProofSerializer(ModelSerializer):

    class Meta:
        model = PaymentProof
        fields = '__all__'


class PdfSerializer(ModelSerializer):

    class Meta:
        model = Pdf
        fields = '__all__'


class PdfTypeSerializer(ModelSerializer):

    class Meta:
        model = PdfType
        fields = '__all__'


class RequestSerializer(ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'


class RequestCategorySerializer(ModelSerializer):

    class Meta:
        model = RequestCategory
        fields = '__all__'


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class SocialMediaSerializer(ModelSerializer):

    class Meta:
        model = SocialMedia
        fields = '__all__'


class SubCategorySerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class UserAdminSerializer(ModelSerializer):

    class Meta:
        model = UserAdmin
        fields = '__all__'


class UserEntitySerializer(ModelSerializer):

    class Meta:
        model = UserEntity
        fields = '__all__'


class UserLogSerializer(ModelSerializer):

    class Meta:
        model = UserLog
        fields = '__all__'


class UserNoteSerializer(ModelSerializer):

    class Meta:
        model = UserNote
        fields = '__all__'


class UserTypeSerializer(ModelSerializer):

    class Meta:
        model = UserType
        fields = '__all__'
