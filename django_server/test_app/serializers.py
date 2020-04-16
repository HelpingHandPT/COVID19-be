from rest_framework.serializers import ModelSerializer
from test_app.models import Ad, AdCategory, Address, AddressProof, AtRiskCategory, AtRisksFavourite, Category, Credential, CredentialProof, HealthLog, HealthLogNote, HelperCategory, HelpersFavourite, Image, LogNote, Note, NoteType, Payment, PaymentProof, Pdf, PdfType, Request, RequestCategory, Review, SocialMedia, SubCategory, UserLog, UserNote, MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


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


class AtRiskCategorySerializer(ModelSerializer):

    class Meta:
        model = AtRiskCategory
        fields = '__all__'


class AtRisksFavouriteSerializer(ModelSerializer):

    class Meta:
        model = AtRisksFavourite
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

class HealthLogSerializer(ModelSerializer):

    class Meta:
        model = HealthLog
        fields = '__all__'


class HealthLogNoteSerializer(ModelSerializer):

    class Meta:
        model = HealthLogNote
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


class UserLogSerializer(ModelSerializer):

    class Meta:
        model = UserLog
        fields = '__all__'


class UserNoteSerializer(ModelSerializer):

    class Meta:
        model = UserNote
        fields = '__all__'


'''
FROM: USER APP
'''
class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True, # make sure email is provided
            validators=[UniqueValidator(queryset=MyUser.objects.all())] # make sure email is unique
            )
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())],
            min_length=5,
            max_length=20
            )
    password = serializers.CharField(
            write_only=True,
            required=True,
            max_length=256
            )
    first_name = serializers.CharField(
            required=True,
            max_length=25
            )
    last_name = serializers.CharField(
            required=True,
            max_length=25
            )

    def create_atrisk(self, validated_data):
        user = MyUser.objects.create_atrisk(validated_data['email'], validated_data['username'], validated_data['password'],
        validated_data['first_name'], validated_data['last_name'])
        return user


    class Meta:
        model = MyUser
        fields = ('user_id', 'email', 'username', 'password', 'first_name', 'last_name')