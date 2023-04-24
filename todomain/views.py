from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo, Tag
from .serializers import TodoSerializer, TodoSerializerPost, TagSerializer
# Create your views here.


class TodoViewSet(ModelViewSet):
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields=['priority', 'due_date', 'tag']
    search_fields=['title', 'description']
    ordering_fields = ['due_date', 'priority']
    permission_classes = [IsAuthenticated]
    queryset=Todo.objects.prefetch_related('tag').all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return TodoSerializer
        return TodoSerializerPost
    
    
        

    def get_serializer_context(self):
        return {'user_id':self.request.user}
    
    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff == True:
            query = self.queryset
            
        else:
            query = self.queryset.filter(user=self.request.user.id)
        serializer = TodoSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TagApiView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

@api_view(["GET", "POST"])
def TagView(request):
    if request.method == 'GET':
        allTags = Tag.objects.all()
        serializer = TagSerializer(allTags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
