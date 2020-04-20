from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from test_app.serializers import AdSerializer, AdCategorySerializer, AddressSerializer, AddressProofSerializer, AtRiskCategorySerializer, AtRisksFavouriteSerializer, CategorySerializer, CredentialSerializer, CredentialProofSerializer, HealthLogSerializer, HealthLogNoteSerializer, HelperCategorySerializer, HelpersFavouriteSerializer, ImageSerializer, LogNoteSerializer, NoteSerializer, NoteTypeSerializer, PaymentSerializer, PaymentProofSerializer, PdfSerializer, PdfTypeSerializer, RequestSerializer, RequestCategorySerializer, ReviewSerializer, SocialMediaSerializer, SubCategorySerializer, UserLogSerializer, UserNoteSerializer, MyUserSerializer, MyUserViewsetSerializer, CustomTokenSerializer
from test_app.models import Ad, AdCategory, Address, AddressProof, AtRiskCategory, AtRisksFavourite, Category, Credential, CredentialProof, HealthLog, HealthLogNote, HelperCategory, HelpersFavourite, Image, LogNote, Note, NoteType, Payment, PaymentProof, Pdf, PdfType, Request, RequestCategory, Review, SocialMedia, SubCategory, UserLog, UserNote, MyUser
from rest_framework import parsers, renderers, status
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMultiAlternatives


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

'''
FROM USER APP
'''

class MyUserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

class MyUserCreateViewSet(ViewSet):
    """ 
    Creates the user. 
    """
    def list(self, request):
        queryset = MyUser.objects.order_by('pk')
        serializer = MyUserViewsetSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MyUserViewsetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = MyUser.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MyUserViewsetSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            return Response(status=404)
        serializer = MyUserViewsetSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


""" 
JWT Auth. 
"""
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

""" 
Reset password. 
"""

class CustomPasswordResetView:
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
        """
          Handles password reset tokens
          When a token is created, an e-mail needs to be sent to the user
        """
        # send an e-mail to the user
        context = {
            'current_user': reset_password_token.user,
            'username': reset_password_token.user.username,
            'email': reset_password_token.user.email,
            'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
        }

        # render email text
        email_html_message = render_to_string('email/user_reset_password.html', context)
        email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

        msg = EmailMultiAlternatives(
            # title:
            "Password Reset for {title}".format(title="Some website title"),
            # message:
            email_plaintext_message,
            # from:
            "test@test.com",
            # to:
            [reset_password_token.user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()


class CustomPasswordTokenVerificationView(APIView):
    """
      An Api View which provides a method to verifiy that a given pw-reset token is valid before actually confirming the
      reset.
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']

        # get token validation time
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # find token
        reset_password_token = ResetPasswordToken.objects.filter(key=token).first()

        if reset_password_token is None:
            return Response({'status': 'invalid'}, status=status.HTTP_404_NOT_FOUND)

        # check expiry date
        expiry_date = reset_password_token.created_at + timedelta(hours=password_reset_token_validation_time)

        if timezone.now() > expiry_date:
            # delete expired token
            reset_password_token.delete()
            return Response({'status': 'expired'}, status=status.HTTP_404_NOT_FOUND)

        # check if user has password to change
        if not reset_password_token.user.has_usable_password():
            return Response({'status': 'irrelevant'})

        return Response({'status': 'OK'})