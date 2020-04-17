from django.urls import path, include
from test_app import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'ad', views.AdViewSet, 'Ad')
router.register(r'adcategory', views.AdCategoryViewSet, 'AdCategory')
router.register(r'address', views.AddressViewSet, 'Address')
router.register(r'addressproof', views.AddressProofViewSet, 'AddressProof')
router.register(r'atriskcategory', views.AtRiskCategoryViewSet, 'AtRiskCategory')
router.register(r'atrisksfavourite', views.AtRisksFavouriteViewSet, 'AtRisksFavourite')
router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'credential', views.CredentialViewSet, 'Credential')
router.register(r'credentialproof', views.CredentialProofViewSet, 'CredentialProof')
router.register(r'healthlog', views.HealthLogViewSet, 'HealthLog')
router.register(r'healthlognote', views.HealthLogNoteViewSet, 'HealthLogNote')
router.register(r'helpercategory', views.HelperCategoryViewSet, 'HelperCategory')
router.register(r'helpersfavourite', views.HelpersFavouriteViewSet, 'HelpersFavourite')
router.register(r'image', views.ImageViewSet, 'Image')
router.register(r'lognote', views.LogNoteViewSet, 'LogNote')
router.register(r'note', views.NoteViewSet, 'Note')
router.register(r'notetype', views.NoteTypeViewSet, 'NoteType')
router.register(r'payment', views.PaymentViewSet, 'Payment')
router.register(r'paymentproof', views.PaymentProofViewSet, 'PaymentProof')
router.register(r'pdf', views.PdfViewSet, 'Pdf')
router.register(r'pdftype', views.PdfTypeViewSet, 'PdfType')
router.register(r'request', views.RequestViewSet, 'Request')
router.register(r'requestcategory', views.RequestCategoryViewSet, 'RequestCategory')
router.register(r'review', views.ReviewViewSet, 'Review')
router.register(r'socialmedia', views.SocialMediaViewSet, 'SocialMedia')
router.register(r'subcategory', views.SubCategoryViewSet, 'SubCategory')
router.register(r'userlog', views.UserLogViewSet, 'UserLog')
router.register(r'usernote', views.UserNoteViewSet, 'UserNote')
router.register(r'user', views.MyUserCreateViewSet, 'MyUserCreate')

urlpatterns = [
    path('',include(router.urls)),
    url(r'api/users', views.MyUserCreate.as_view(), name='user-create'),
    
    #test JWT Auth
    path('hello/', views.HelloView.as_view(), name='hello'),
]