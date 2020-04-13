from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from test_app.serializers import AdSerializer, AdCategorySerializer, AddressSerializer, AddressProofSerializer, AtRiskSerializer, AtRiskCategorySerializer, AtRisksFavouriteSerializer, AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, CategorySerializer, CredentialSerializer, CredentialProofSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, ExecutiveTypeSerializer, ExecutiveUserSerializer, HealthLogSerializer, HealthLogNoteSerializer, HelperSerializer, HelperCategorySerializer, HelpersFavouriteSerializer, ImageSerializer, LogNoteSerializer, MonitorSerializer, NormalTypeSerializer, NormalUserSerializer, NoteSerializer, NoteTypeSerializer, PaymentSerializer, PaymentProofSerializer, PdfSerializer, PdfTypeSerializer, RequestSerializer, RequestCategorySerializer, ReviewSerializer, SocialMediaSerializer, SubCategorySerializer, UserAdminSerializer, UserEntitySerializer, UserLogSerializer, UserNoteSerializer, UserTypeSerializer
from test_app.models import Ad, AdCategory, Address, AddressProof, AtRisk, AtRiskCategory, AtRisksFavourite, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Category, Credential, CredentialProof, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, ExecutiveType, ExecutiveUser, HealthLog, HealthLogNote, Helper, HelperCategory, HelpersFavourite, Image, LogNote, Monitor, NormalType, NormalUser, Note, NoteType, Payment, PaymentProof, Pdf, PdfType, Request, RequestCategory, Review, SocialMedia, SubCategory, UserAdmin, UserEntity, UserLog, UserNote, UserType


class AdViewSet(ViewSet):

    def list(self, request):
        queryset = Ad.objects.order_by('pk')
        serializer = AdSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Ad.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AdSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            return Response(status=404)
        serializer = AdSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AdCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = AdCategory.objects.order_by('pk')
        serializer = AdCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AdCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AdCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AdCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AdCategory.objects.get(pk=pk)
        except AdCategory.DoesNotExist:
            return Response(status=404)
        serializer = AdCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AdCategory.objects.get(pk=pk)
        except AdCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AddressViewSet(ViewSet):

    def list(self, request):
        queryset = Address.objects.order_by('pk')
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response(status=404)
        serializer = AddressSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AddressProofViewSet(ViewSet):

    def list(self, request):
        queryset = AddressProof.objects.order_by('pk')
        serializer = AddressProofSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AddressProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AddressProof.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AddressProofSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AddressProof.objects.get(pk=pk)
        except AddressProof.DoesNotExist:
            return Response(status=404)
        serializer = AddressProofSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AddressProof.objects.get(pk=pk)
        except AddressProof.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AtRiskViewSet(ViewSet):

    def list(self, request):
        queryset = AtRisk.objects.order_by('pk')
        serializer = AtRiskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AtRiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AtRisk.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AtRiskSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AtRisk.objects.get(pk=pk)
        except AtRisk.DoesNotExist:
            return Response(status=404)
        serializer = AtRiskSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AtRisk.objects.get(pk=pk)
        except AtRisk.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AtRiskCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = AtRiskCategory.objects.order_by('pk')
        serializer = AtRiskCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AtRiskCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AtRiskCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AtRiskCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AtRiskCategory.objects.get(pk=pk)
        except AtRiskCategory.DoesNotExist:
            return Response(status=404)
        serializer = AtRiskCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AtRiskCategory.objects.get(pk=pk)
        except AtRiskCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AtRisksFavouriteViewSet(ViewSet):

    def list(self, request):
        queryset = AtRisksFavourite.objects.order_by('pk')
        serializer = AtRisksFavouriteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AtRisksFavouriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AtRisksFavourite.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AtRisksFavouriteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AtRisksFavourite.objects.get(pk=pk)
        except AtRisksFavourite.DoesNotExist:
            return Response(status=404)
        serializer = AtRisksFavouriteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AtRisksFavourite.objects.get(pk=pk)
        except AtRisksFavourite.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupViewSet(ViewSet):

    def list(self, request):
        queryset = AuthGroup.objects.order_by('pk')
        serializer = AuthGroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthGroup.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthGroupSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthGroup.objects.get(pk=pk)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthGroup.objects.get(pk=pk)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupPermissionsViewSet(ViewSet):

    def list(self, request):
        queryset = AuthGroupPermissions.objects.order_by('pk')
        serializer = AuthGroupPermissionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthGroupPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthGroupPermissions.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthGroupPermissionsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=pk)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=pk)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthPermissionViewSet(ViewSet):

    def list(self, request):
        queryset = AuthPermission.objects.order_by('pk')
        serializer = AuthPermissionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthPermission.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthPermissionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthPermission.objects.get(pk=pk)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        serializer = AuthPermissionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthPermission.objects.get(pk=pk)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserViewSet(ViewSet):

    def list(self, request):
        queryset = AuthUser.objects.order_by('pk')
        serializer = AuthUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthUser.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthUserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthUser.objects.get(pk=pk)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserGroupsViewSet(ViewSet):

    def list(self, request):
        queryset = AuthUserGroups.objects.order_by('pk')
        serializer = AuthUserGroupsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthUserGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthUserGroups.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthUserGroupsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthUserGroups.objects.get(pk=pk)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserGroupsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthUserGroups.objects.get(pk=pk)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserUserPermissionsViewSet(ViewSet):

    def list(self, request):
        queryset = AuthUserUserPermissions.objects.order_by('pk')
        serializer = AuthUserUserPermissionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthUserUserPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AuthUserUserPermissions.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthUserUserPermissionsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=pk)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserUserPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=pk)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CredentialViewSet(ViewSet):

    def list(self, request):
        queryset = Credential.objects.order_by('pk')
        serializer = CredentialSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CredentialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Credential.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CredentialSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Credential.objects.get(pk=pk)
        except Credential.DoesNotExist:
            return Response(status=404)
        serializer = CredentialSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Credential.objects.get(pk=pk)
        except Credential.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CredentialProofViewSet(ViewSet):

    def list(self, request):
        queryset = CredentialProof.objects.order_by('pk')
        serializer = CredentialProofSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CredentialProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = CredentialProof.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CredentialProofSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = CredentialProof.objects.get(pk=pk)
        except CredentialProof.DoesNotExist:
            return Response(status=404)
        serializer = CredentialProofSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = CredentialProof.objects.get(pk=pk)
        except CredentialProof.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoAdminLogViewSet(ViewSet):

    def list(self, request):
        queryset = DjangoAdminLog.objects.order_by('pk')
        serializer = DjangoAdminLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DjangoAdminLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DjangoAdminLog.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DjangoAdminLogSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = DjangoAdminLog.objects.get(pk=pk)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        serializer = DjangoAdminLogSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = DjangoAdminLog.objects.get(pk=pk)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoContentTypeViewSet(ViewSet):

    def list(self, request):
        queryset = DjangoContentType.objects.order_by('pk')
        serializer = DjangoContentTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DjangoContentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DjangoContentType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DjangoContentTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = DjangoContentType.objects.get(pk=pk)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        serializer = DjangoContentTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = DjangoContentType.objects.get(pk=pk)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoMigrationsViewSet(ViewSet):

    def list(self, request):
        queryset = DjangoMigrations.objects.order_by('pk')
        serializer = DjangoMigrationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DjangoMigrationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DjangoMigrations.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DjangoMigrationsSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = DjangoMigrations.objects.get(pk=pk)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        serializer = DjangoMigrationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = DjangoMigrations.objects.get(pk=pk)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoSessionViewSet(ViewSet):

    def list(self, request):
        queryset = DjangoSession.objects.order_by('pk')
        serializer = DjangoSessionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DjangoSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = DjangoSession.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DjangoSessionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = DjangoSession.objects.get(pk=pk)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        serializer = DjangoSessionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = DjangoSession.objects.get(pk=pk)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ExecutiveTypeViewSet(ViewSet):

    def list(self, request):
        queryset = ExecutiveType.objects.order_by('pk')
        serializer = ExecutiveTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExecutiveTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ExecutiveType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ExecutiveTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ExecutiveType.objects.get(pk=pk)
        except ExecutiveType.DoesNotExist:
            return Response(status=404)
        serializer = ExecutiveTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ExecutiveType.objects.get(pk=pk)
        except ExecutiveType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ExecutiveUserViewSet(ViewSet):

    def list(self, request):
        queryset = ExecutiveUser.objects.order_by('pk')
        serializer = ExecutiveUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExecutiveUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ExecutiveUser.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ExecutiveUserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = ExecutiveUser.objects.get(pk=pk)
        except ExecutiveUser.DoesNotExist:
            return Response(status=404)
        serializer = ExecutiveUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = ExecutiveUser.objects.get(pk=pk)
        except ExecutiveUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HealthLogViewSet(ViewSet):

    def list(self, request):
        queryset = HealthLog.objects.order_by('pk')
        serializer = HealthLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HealthLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = HealthLog.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HealthLogSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = HealthLog.objects.get(pk=pk)
        except HealthLog.DoesNotExist:
            return Response(status=404)
        serializer = HealthLogSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = HealthLog.objects.get(pk=pk)
        except HealthLog.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HealthLogNoteViewSet(ViewSet):

    def list(self, request):
        queryset = HealthLogNote.objects.order_by('pk')
        serializer = HealthLogNoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HealthLogNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = HealthLogNote.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HealthLogNoteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = HealthLogNote.objects.get(pk=pk)
        except HealthLogNote.DoesNotExist:
            return Response(status=404)
        serializer = HealthLogNoteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = HealthLogNote.objects.get(pk=pk)
        except HealthLogNote.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HelperViewSet(ViewSet):

    def list(self, request):
        queryset = Helper.objects.order_by('pk')
        serializer = HelperSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HelperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Helper.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HelperSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Helper.objects.get(pk=pk)
        except Helper.DoesNotExist:
            return Response(status=404)
        serializer = HelperSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Helper.objects.get(pk=pk)
        except Helper.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HelperCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = HelperCategory.objects.order_by('pk')
        serializer = HelperCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HelperCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = HelperCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HelperCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = HelperCategory.objects.get(pk=pk)
        except HelperCategory.DoesNotExist:
            return Response(status=404)
        serializer = HelperCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = HelperCategory.objects.get(pk=pk)
        except HelperCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HelpersFavouriteViewSet(ViewSet):

    def list(self, request):
        queryset = HelpersFavourite.objects.order_by('pk')
        serializer = HelpersFavouriteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HelpersFavouriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = HelpersFavourite.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HelpersFavouriteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = HelpersFavourite.objects.get(pk=pk)
        except HelpersFavourite.DoesNotExist:
            return Response(status=404)
        serializer = HelpersFavouriteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = HelpersFavourite.objects.get(pk=pk)
        except HelpersFavourite.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ImageViewSet(ViewSet):

    def list(self, request):
        queryset = Image.objects.order_by('pk')
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Image.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ImageSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=404)
        serializer = ImageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LogNoteViewSet(ViewSet):

    def list(self, request):
        queryset = LogNote.objects.order_by('pk')
        serializer = LogNoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LogNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = LogNote.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = LogNoteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = LogNote.objects.get(pk=pk)
        except LogNote.DoesNotExist:
            return Response(status=404)
        serializer = LogNoteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = LogNote.objects.get(pk=pk)
        except LogNote.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MonitorViewSet(ViewSet):

    def list(self, request):
        queryset = Monitor.objects.order_by('pk')
        serializer = MonitorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MonitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Monitor.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MonitorSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Monitor.objects.get(pk=pk)
        except Monitor.DoesNotExist:
            return Response(status=404)
        serializer = MonitorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Monitor.objects.get(pk=pk)
        except Monitor.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NormalTypeViewSet(ViewSet):

    def list(self, request):
        queryset = NormalType.objects.order_by('pk')
        serializer = NormalTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NormalTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = NormalType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NormalTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = NormalType.objects.get(pk=pk)
        except NormalType.DoesNotExist:
            return Response(status=404)
        serializer = NormalTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = NormalType.objects.get(pk=pk)
        except NormalType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NormalUserViewSet(ViewSet):

    def list(self, request):
        queryset = NormalUser.objects.order_by('pk')
        serializer = NormalUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NormalUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = NormalUser.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NormalUserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = NormalUser.objects.get(pk=pk)
        except NormalUser.DoesNotExist:
            return Response(status=404)
        serializer = NormalUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = NormalUser.objects.get(pk=pk)
        except NormalUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NoteViewSet(ViewSet):

    def list(self, request):
        queryset = Note.objects.order_by('pk')
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Note.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NoteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response(status=404)
        serializer = NoteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class NoteTypeViewSet(ViewSet):

    def list(self, request):
        queryset = NoteType.objects.order_by('pk')
        serializer = NoteTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NoteTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = NoteType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NoteTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = NoteType.objects.get(pk=pk)
        except NoteType.DoesNotExist:
            return Response(status=404)
        serializer = NoteTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = NoteType.objects.get(pk=pk)
        except NoteType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PaymentViewSet(ViewSet):

    def list(self, request):
        queryset = Payment.objects.order_by('pk')
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Payment.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(status=404)
        serializer = PaymentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PaymentProofViewSet(ViewSet):

    def list(self, request):
        queryset = PaymentProof.objects.order_by('pk')
        serializer = PaymentProofSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = PaymentProof.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PaymentProofSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = PaymentProof.objects.get(pk=pk)
        except PaymentProof.DoesNotExist:
            return Response(status=404)
        serializer = PaymentProofSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = PaymentProof.objects.get(pk=pk)
        except PaymentProof.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PdfViewSet(ViewSet):

    def list(self, request):
        queryset = Pdf.objects.order_by('pk')
        serializer = PdfSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Pdf.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PdfSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Pdf.objects.get(pk=pk)
        except Pdf.DoesNotExist:
            return Response(status=404)
        serializer = PdfSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Pdf.objects.get(pk=pk)
        except Pdf.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PdfTypeViewSet(ViewSet):

    def list(self, request):
        queryset = PdfType.objects.order_by('pk')
        serializer = PdfTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PdfTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = PdfType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PdfTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = PdfType.objects.get(pk=pk)
        except PdfType.DoesNotExist:
            return Response(status=404)
        serializer = PdfTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = PdfType.objects.get(pk=pk)
        except PdfType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RequestViewSet(ViewSet):

    def list(self, request):
        queryset = Request.objects.order_by('pk')
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Request.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RequestSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            return Response(status=404)
        serializer = RequestSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RequestCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = RequestCategory.objects.order_by('pk')
        serializer = RequestCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RequestCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = RequestCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = RequestCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = RequestCategory.objects.get(pk=pk)
        except RequestCategory.DoesNotExist:
            return Response(status=404)
        serializer = RequestCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = RequestCategory.objects.get(pk=pk)
        except RequestCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ReviewViewSet(ViewSet):

    def list(self, request):
        queryset = Review.objects.order_by('pk')
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Review.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ReviewSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=404)
        serializer = ReviewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SocialMediaViewSet(ViewSet):

    def list(self, request):
        queryset = SocialMedia.objects.order_by('pk')
        serializer = SocialMediaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SocialMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SocialMedia.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SocialMediaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SocialMedia.objects.get(pk=pk)
        except SocialMedia.DoesNotExist:
            return Response(status=404)
        serializer = SocialMediaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SocialMedia.objects.get(pk=pk)
        except SocialMedia.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SubCategoryViewSet(ViewSet):

    def list(self, request):
        queryset = SubCategory.objects.order_by('pk')
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SubCategory.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SubCategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response(status=404)
        serializer = SubCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserAdminViewSet(ViewSet):

    def list(self, request):
        queryset = UserAdmin.objects.order_by('pk')
        serializer = UserAdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserAdmin.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserAdminSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserAdmin.objects.get(pk=pk)
        except UserAdmin.DoesNotExist:
            return Response(status=404)
        serializer = UserAdminSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserAdmin.objects.get(pk=pk)
        except UserAdmin.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserEntityViewSet(ViewSet):

    def list(self, request):
        queryset = UserEntity.objects.order_by('pk')
        serializer = UserEntitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserEntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserEntity.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserEntitySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserEntity.objects.get(pk=pk)
        except UserEntity.DoesNotExist:
            return Response(status=404)
        serializer = UserEntitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserEntity.objects.get(pk=pk)
        except UserEntity.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserLogViewSet(ViewSet):

    def list(self, request):
        queryset = UserLog.objects.order_by('pk')
        serializer = UserLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserLog.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserLogSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserLog.objects.get(pk=pk)
        except UserLog.DoesNotExist:
            return Response(status=404)
        serializer = UserLogSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserLog.objects.get(pk=pk)
        except UserLog.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserNoteViewSet(ViewSet):

    def list(self, request):
        queryset = UserNote.objects.order_by('pk')
        serializer = UserNoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserNote.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserNoteSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserNote.objects.get(pk=pk)
        except UserNote.DoesNotExist:
            return Response(status=404)
        serializer = UserNoteSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserNote.objects.get(pk=pk)
        except UserNote.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserTypeViewSet(ViewSet):

    def list(self, request):
        queryset = UserType.objects.order_by('pk')
        serializer = UserTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = UserType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserTypeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = UserType.objects.get(pk=pk)
        except UserType.DoesNotExist:
            return Response(status=404)
        serializer = UserTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = UserType.objects.get(pk=pk)
        except UserType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
