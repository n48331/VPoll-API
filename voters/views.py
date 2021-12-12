from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VoterSerializer
from .models import Voter
# Create your views here.


class VoterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        voter = Voter.objects.all()
        serializer = VoterSerializer(voter, many=True)
        return Response(serializer.data)
