from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from.permissions import IsRecruiterOrReadOnly
from django.shortcuts import get_object_or_404

class Joblistcreate(APIView):
    permission_classes=[TokenAuthentication]
    permission_classes=[IsRecruiterOrReadOnly]
    def get(self,request):
        e=Job.objects.all()
        serializer_instance=JobSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer_instance = JobSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(posted_by=request.user)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class JobRetrieveUpdateDelete(APIView):

    permission_classes=[TokenAuthentication]
    permission_classes=[IsRecruiterOrReadOnly]

    def get(self, request, i):
        e = get_object_or_404(Job, id=i)
        serializer_instance = JobSerializer(e) 
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def put(self, request, i):
        e = get_object_or_404(Job, id=i)
        serializer_instance = JobSerializer(e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, i):
        e = Job.objects.get(id=i)
        serializer_instance = JobSerializer(e, request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, i):
        e = get_object_or_404(Job, id=i)
        e.delete()
        return Response({"Message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)




