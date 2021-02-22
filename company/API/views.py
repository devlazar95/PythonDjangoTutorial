from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from company.API.models import Employee, Project, Sector
from company.API.serializers import UserSerializer, GroupSerializer, EmployeeSerializer, ProjectSerializer, \
    SectorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeList(APIView):
    """
    List all employees
    """

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetails(APIView):
    """Retrieve an employee instance"""

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class SectorList(APIView):
    """
    List all employees
    """

    def get(self, request, format=None):
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)


class SectorDetails(APIView):
    """Retrieve an employee instance"""

    def get_object(self, pk):
        try:
            return Sector.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        sector = self.get_object(pk)
        serializer = SectorSerializer(sector)
        return Response(serializer.data)


class ProjectList(APIView):
    """
    List all employees
    """

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetails(APIView):
    """Retrieve an employee instance"""

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)