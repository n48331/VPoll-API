from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VoterSerializer
from .models import Voter
# Create your views here.


class VotersListView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        voter = Voter.objects.all().order_by('sl')
        serializer = VoterSerializer(voter, many=True)
        return Response(serializer.data)


class VotersView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Voter.objects.get(pk=pk)

    def get(self, request, pk):
        voter = self.get_object(pk)
        serializer = VoterSerializer(voter)
        return Response(serializer.data)

    def patch(self, request, pk):
        Voter_object = self.get_object(pk)
        # set partial=True to update a data partially
        serializer = VoterSerializer(
            Voter_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")
