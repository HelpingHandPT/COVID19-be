from note.viewsets import NotesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NotesViewSet)
#router.register('monitors', MonitorsViewSet)