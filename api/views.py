from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, is_success
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class SiteConfigAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=SiteConfigSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: SiteConfigSerializer(many=True)},
        tags=['SiteConfig'],
        methods=['GET'],
        operation_id='SiteConfig_get'
    )
    def get(self, request, pk=None):
        if pk:
            instance = get_object_or_404(SiteConfig, pk=pk)
            serializer = SiteConfigSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='application/json')
        objs = SiteConfig.objects.all().order_by('id')
        serializers = SiteConfigSerializer(objs, many=True)
        return Response({"Response": serializers.data}, status=HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=SiteConfigSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: SiteConfigSerializer()},
        tags=['SiteConfig'],
        methods=['POST'],
        operation_id='SiteConfig_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = SiteConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=SiteConfigSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: SiteConfigSerializer()},
        tags=['SiteConfig'],
        methods=['PUT'],
        operation_id='SiteConfig_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SiteConfig, pk=pk)
        serializer = SiteConfigSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=SiteConfigSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: SiteConfigSerializer()},
        tags=['SiteConfig'],
        methods=['DELETE'],
        operation_id='SiteConfig_delete'
    )
    def delete(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(SiteConfig, pk=pk)
        SiteConfig.objects.get(pk=pk).delete()
        serializer = SiteConfigSerializer(instance=obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='application/json')


class PermitDocCategoryAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=PermitDocCategorySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: PermitDocCategorySerializer()},
        tags=['PermitDocCategory'],
        operation_id='PermitDocCat_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(PermitDocCategory, pk=pk)
            serializer = PermitDocCategorySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='application/json')
        objects = PermitDocCategory.objects.all().order_by('id')
        serializers = PermitDocCategorySerializer(objects, many=True)
        return Response({"Response": serializers.data}, status=HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=PermitDocCategorySerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: PermitDocCategorySerializer()},
        tags=['PermitDocCategory'],
        operation_id='PermitDocCat_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = PermitDocCategorySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=PermitDocCategorySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: PermitDocCategorySerializer()},
        tags=['PermitDocCategory'],
        operation_id='PermitDocCat_put'
    )
    def put(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(PermitDocCategory, pk=pk)
        serializer = PermitDocCategorySerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=PermitDocCategorySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: PermitDocCategorySerializer()},
        tags=['PermitDocCategory'],
        operation_id='PermitDocCat_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(PermitDocCategory, pk=pk)
        serializer = PermitDocCategorySerializer(obj)
        PermitDocCategory.objects.get(pk=pk).delete()
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class CitizenshipAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CitizenshipSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: CitizenshipSerializer()},
        tags=['Citizenship'],
        operation_id='Citizenship_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Citizenship, pk=pk)
            serializer = CitizenshipSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='application/json')
        serializer = CitizenshipSerializer(instance=Citizenship.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='application/json')

    @extend_schema(
        request=CitizenshipSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: CitizenshipSerializer()},
        tags=['Citizenship'],
        operation_id='Citizenship_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = CitizenshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=CitizenshipSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: CitizenshipSerializer()},
        tags=['Citizenship'],
        operation_id='Citizenship_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Citizenship, pk=pk)
        serializer = CitizenshipSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=CitizenshipSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: CitizenshipSerializer()},
        tags=['Citizenship'],
        operation_id='Citizenship_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Citizenship, pk=pk)
        obj.delete()
        serializer = CitizenshipSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class DocumentTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: DocumentTypeSerializer()},
        tags=['DocumentType'],
        operation_id='DocumentType_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(DocumentType, pk=pk)
            serializer = DocumentTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = DocumentTypeSerializer(DocumentType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: DocumentTypeSerializer()},
        tags=['DocumentType'],
        operation_id='DocumentType_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = DocumentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: DocumentTypeSerializer()},
        tags=['DocumentType'],
        operation_id='DocumentType_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(DocumentType, pk=pk)
        serializer = DocumentTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: DocumentTypeSerializer()},
        tags=['DocumentType'],
        operation_id='DocumentType_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(DocumentType, pk=pk)
        obj.delete()
        serializer = DocumentTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_DocumentTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DocumentTypeSerializer()},
        tags=['Gen_DT_DocumentType'],
        operation_id='Gen_DT_DocumentType_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_DocumentType, pk=pk)
            serializer = Gen_DT_DocumentTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_DocumentTypeSerializer(Gen_DT_DocumentType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_DocumentTypeSerializer()},
        tags=['Gen_DT_DocumentType'],
        operation_id='Gen_DT_DocumentType_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_DocumentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DocumentTypeSerializer()},
        tags=['Gen_DT_DocumentType'],
        operation_id='Gen_DT_DocumentType_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_DocumentType, pk=pk)
        serializer = Gen_DT_DocumentTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DocumentTypeSerializer()},
        tags=['Gen_DT_DocumentType'],
        operation_id='Gen_DT_DocumentType_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_DocumentType, pk=pk)
        obj.delete()
        serializer = Gen_DT_DocumentTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CountryAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_CountrySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CountrySerializer()},
        tags=['Gen_DT_Country'],
        operation_id='Gen_DT_Country_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Country, pk=pk)
            serializer = Gen_DT_CountrySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CountrySerializer(Gen_DT_Country.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_CountrySerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_CountrySerializer()},
        tags=['Gen_DT_Country'],
        operation_id='Gen_DT_Country_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_CountrySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CountrySerializer()},
        tags=['Gen_DT_Country'],
        operation_id='Gen_DT_Country_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Country, pk=pk)
        serializer = Gen_DT_CountrySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_CountrySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CountrySerializer()},
        tags=['Gen_DT_Country'],
        operation_id='Gen_DT_Country_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Country, pk=pk)
        obj.delete()
        serializer = Gen_DT_CountrySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_DisciplineAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_DisciplineSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DisciplineSerializer()},
        tags=['Gen_DT_Discipline'],
        operation_id='Gen_DT_Discipline_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(DocumentType, pk=pk)
            serializer = Gen_DT_DisciplineSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_DisciplineSerializer(Gen_DT_Discipline.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_DisciplineSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_DisciplineSerializer()},
        tags=['Gen_DT_Discipline'],
        operation_id='Gen_DT_Discipline_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_DisciplineSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DisciplineSerializer()},
        tags=['Gen_DT_Discipline'],
        operation_id='Gen_DT_Discipline_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Discipline, pk=pk)
        serializer = Gen_DT_DisciplineSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_DisciplineSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DisciplineSerializer()},
        tags=['Gen_DT_Discipline'],
        operation_id='Gen_DT_Discipline_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Discipline, pk=pk)
        obj.delete()
        serializer = Gen_DT_DisciplineSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpLevelAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_EmpLevelSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpLevelSerializer()},
        tags=['Gen_DT_EmpLevel'],
        operation_id='Gen_DT_EmpLevel_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpLevel, pk=pk)
            serializer = Gen_DT_EmpLevelSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpLevelSerializer(Gen_DT_EmpLevel.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_EmpLevelSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_EmpLevelSerializer()},
        tags=['Gen_DT_EmpLevel'],
        operation_id='Gen_DT_EmpLevel_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_EmpLevelSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpLevelSerializer()},
        tags=['Gen_DT_EmpLevel'],
        operation_id='Gen_DT_EmpLevel_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpLevel, pk=pk)
        serializer = Gen_DT_EmpLevelSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_EmpLevelSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpLevelSerializer()},
        tags=['Gen_DT_EmpLevel'],
        operation_id='Gen_DT_EmpLevel_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpLevel, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpLevelSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpClassAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_EmpClassSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpClassSerializer()},
        tags=['Gen_DT_EmpClass'],
        operation_id='Gen_DT_EmpClass_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpClass, pk=pk)
            serializer = Gen_DT_EmpClassSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpClassSerializer(Gen_DT_EmpClass.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_EmpClassSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_EmpClassSerializer()},
        tags=['Gen_DT_EmpClass'],
        operation_id='Gen_DT_EmpClass_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_EmpClassSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpClassSerializer()},
        tags=['Gen_DT_EmpClass'],
        operation_id='Gen_DT_EmpClass_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpClass, pk=pk)
        serializer = Gen_DT_EmpClassSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_EmpClassSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpClassSerializer()},
        tags=['Gen_DT_EmpClass'],
        operation_id='Gen_DT_EmpClass_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpClass, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpClassSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_JobTitleAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_JobTitleSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_JobTitleSerializer()},
        tags=['Gen_DT_JobTitle'],
        operation_id='Gen_DT_JobTitle_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(DocumentType, pk=pk)
            serializer = Gen_DT_JobTitleSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_JobTitleSerializer(Gen_DT_JobTitle.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_JobTitleSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_JobTitleSerializer()},
        tags=['Gen_DT_JobTitle'],
        operation_id='Gen_DT_JobTitle_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_JobTitleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_JobTitleSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_JobTitleSerializer()},
        tags=['Gen_DT_JobTitle'],
        operation_id='Gen_DT_JobTitle_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_JobTitle, pk=pk)
        serializer = Gen_DT_JobTitleSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_JobTitleSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_JobTitleSerializer()},
        tags=['Gen_DT_JobTitle'],
        operation_id='Gen_DT_JobTitle_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_JobTitle, pk=pk)
        obj.delete()
        serializer = Gen_DT_JobTitleSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CurrencyAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_CurrencySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CurrencySerializer()},
        tags=['Gen_DT_Currency'],
        operation_id='Gen_DT_Currency_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Currency, pk=pk)
            serializer = Gen_DT_CurrencySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CurrencySerializer(Gen_DT_Currency.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_CurrencySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CurrencySerializer()},
        tags=['Gen_DT_Currency'],
        operation_id='Gen_DT_Currency_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_CurrencySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CurrencySerializer()},
        tags=['Gen_DT_Currency'],
        operation_id='Gen_DT_Currency_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Currency, pk=pk)
        serializer = Gen_DT_CurrencySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_CurrencySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CurrencySerializer()},
        tags=['Gen_DT_Currency'],
        operation_id='Gen_DT_Currency_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Currency, pk=pk)
        obj.delete()
        serializer = Gen_DT_CurrencySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CBR_RatesAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_CBR_RatesSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CBR_RatesSerializer()},
        tags=['Gen_DT_CBR_Rates'],
        operation_id='Gen_DT_CBR_Rates_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_CBR_Rates, pk=pk)
            serializer = Gen_DT_CBR_RatesSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CBR_RatesSerializer(Gen_DT_CBR_Rates.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_CBR_RatesSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_CBR_RatesSerializer()},
        tags=['Gen_DT_CBR_Rates'],
        operation_id='Gen_DT_CBR_Rates_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CBR_RatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_CBR_RatesSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_CBR_RatesSerializer()},
        tags=['Gen_DT_CBR_Rates'],
        operation_id='Gen_DT_CBR_Rates_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_CBR_Rates, pk=pk)
        serializer = Gen_DT_CBR_RatesSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_CBR_RatesSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CBR_RatesSerializer()},
        tags=['Gen_DT_CBR_Rates'],
        operation_id='Gen_DT_CBR_Rates_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CBR_Rates, pk=pk)
        obj.delete()
        serializer = Gen_DT_CBR_RatesSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CounterPartyAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_CounterPartySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CounterPartySerializer()},
        tags=['Gen_DT_CounterParty'],
        operation_id='Gen_DT_CounterParty_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_CounterParty, pk=pk)
            serializer = Gen_DT_CounterPartySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CounterPartySerializer(Gen_DT_CounterParty.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_CounterPartySerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_CounterPartySerializer()},
        tags=['Gen_DT_CounterParty'],
        operation_id='Gen_DT_CounterParty_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CounterPartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_CounterPartySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CounterPartySerializer()},
        tags=['Gen_DT_CounterParty'],
        operation_id='Gen_DT_CounterParty_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_CounterParty, pk=pk)
        serializer = Gen_DT_CounterPartySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_CounterPartySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CounterPartySerializer()},
        tags=['Gen_DT_CounterParty'],
        operation_id='Gen_DT_CounterParty_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CounterParty, pk=pk)
        obj.delete()
        serializer = Gen_DT_CounterPartySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_SubjectOfRFAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_SubjectOfRFSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_SubjectOfRFSerializer()},
        tags=['Gen_DT_SubjectOfRF'],
        operation_id='Gen_DT_SubjectOfRF_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_SubjectOfRF, pk=pk)
            serializer = Gen_DT_SubjectOfRFSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_SubjectOfRFSerializer(Gen_DT_SubjectOfRF.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_SubjectOfRFSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_SubjectOfRFSerializer()},
        tags=['Gen_DT_SubjectOfRF'],
        operation_id='Gen_DT_SubjectOfRF_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_SubjectOfRFSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_SubjectOfRFSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_SubjectOfRFSerializer()},
        tags=['Gen_DT_SubjectOfRF'],
        operation_id='Gen_DT_SubjectOfRF_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_SubjectOfRF, pk=pk)
        serializer = Gen_DT_SubjectOfRFSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(
        request=Gen_DT_SubjectOfRFSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_SubjectOfRFSerializer()},
        tags=['Gen_DT_SubjectOfRF'],
        operation_id='Gen_DT_SubjectOfRF_delete'
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_SubjectOfRF, pk=pk)
        obj.delete()
        serializer = Gen_DT_SubjectOfRFSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ProjectAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=Gen_DT_ProjectSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_ProjectSerializer()},
        tags=['Gen_DT_Project'],
        operation_id='Gen_DT_Project_get'
    )
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Project, pk=pk)
            serializer = Gen_DT_ProjectSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ProjectSerializer(Gen_DT_Project.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(
        request=Gen_DT_ProjectSerializer,  # Specify the serializer for the request
        responses={HTTP_201_CREATED: Gen_DT_ProjectSerializer()},
        tags=['Gen_DT_Project'],
        operation_id='Gen_DT_Project_post'
    )
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=Gen_DT_ProjectSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_ProjectSerializer()},
        tags=['Gen_DT_Project'],
        operation_id='Gen_DT_Project_put'
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Project, pk=pk)
        serializer = Gen_DT_ProjectSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ProjectSerializer, responses={HTTP_200_OK: Gen_DT_ProjectSerializer()}, tags=['Gen_DT_Project'],
                   operation_id='Gen_DT_Project_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Project, pk=pk)
        obj.delete()
        serializer = Gen_DT_ProjectSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CounterPartyTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_CounterPartyTypeSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'],
        operation_id='Gen_DT_CounterPartyType_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
            serializer = Gen_DT_CounterPartyTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CounterPartyTypeSerializer(Gen_DT_CounterPartyType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_201_CREATED: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'],
        operation_id='Gen_DT_CounterPartyType_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CounterPartyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'],
        operation_id='Gen_DT_CounterPartyType_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
        serializer = Gen_DT_CounterPartyTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'],
        operation_id='Gen_DT_CounterPartyType_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
        obj.delete()
        serializer = Gen_DT_CounterPartyTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ContractTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'],
        operation_id='Gen_DT_ContractType_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ContractType, pk=pk)
            serializer = Gen_DT_ContractTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ContractTypeSerializer(Gen_DT_ContractType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'],
        operation_id='Gen_DT_ContractType_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ContractTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'],
        operation_id='Gen_DT_ContractType_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ContractType, pk=pk)
        serializer = Gen_DT_ContractTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'],
        operation_id='Gen_DT_ContractType_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ContractType, pk=pk)
        obj.delete()
        serializer = Gen_DT_ContractTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_VAT_RateAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'],
        operation_id='Gen_DT_VAT_Rate_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
            serializer = Gen_DT_VAT_RateSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_VAT_RateSerializer(Gen_DT_VAT_Rate.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_201_CREATED: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'],
        operation_id='Gen_DT_VAT_Rate_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_VAT_RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'],
        operation_id='Gen_DT_VAT_Rate_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
        serializer = Gen_DT_VAT_RateSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'],
        operation_id='Gen_DT_VAT_Rate_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
        obj.delete()
        serializer = Gen_DT_VAT_RateSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_UoMAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'],
        operation_id='Gen_DT_UoM_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_UoM, pk=pk)
            serializer = Gen_DT_UoMSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_UoMSerializer(Gen_DT_UoM.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_201_CREATED: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'],
        operation_id='Gen_DT_UoM_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_UoMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'],
        operation_id='Gen_DT_UoM_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_UoM, pk=pk)
        serializer = Gen_DT_UoMSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'],
        operation_id='Gen_DT_UoM_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_UoM, pk=pk)
        obj.delete()
        serializer = Gen_DT_UoMSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_BudgetDataAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'],
        operation_id='Gen_DT_BudgetData_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_BudgetData, pk=pk)
            serializer = Gen_DT_BudgetDataSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_BudgetDataSerializer(Gen_DT_BudgetData.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_201_CREATED: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'],
        operation_id='Gen_DT_BudgetData_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_BudgetDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'],
        operation_id='Gen_DT_BudgetData_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_BudgetData, pk=pk)
        serializer = Gen_DT_BudgetDataSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'],
        operation_id='Gen_DT_BudgetData_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_BudgetData, pk=pk)
        obj.delete()
        serializer = Gen_DT_BudgetDataSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_BudgetDataHistoryAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'],
        operation_id='Gen_DT_BudgetDataHistory_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
            serializer = Gen_DT_BudgetDataHistorySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_BudgetDataHistorySerializer(Gen_DT_BudgetDataHistory.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_201_CREATED: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'],
        operation_id='Gen_DT_BudgetDataHistory_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_BudgetDataHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'],
        operation_id='Gen_DT_BudgetDataHistory_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
        serializer = Gen_DT_BudgetDataHistorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'],
        operation_id='Gen_DT_BudgetDataHistory_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
        obj.delete()
        serializer = Gen_DT_BudgetDataHistorySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ExpenseFrequencyAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'],
        operation_id='Gen_DT_ExpenseFrequency_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
            serializer = Gen_DT_ExpenseFrequencySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ExpenseFrequencySerializer(Gen_DT_ExpenseFrequency.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_201_CREATED: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'],
        operation_id='Gen_DT_ExpenseFrequency_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ExpenseFrequencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'],
        operation_id='Gen_DT_ExpenseFrequency_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
        serializer = Gen_DT_ExpenseFrequencySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'],
        operation_id='Gen_DT_ExpenseFrequency_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
        obj.delete()
        serializer = Gen_DT_ExpenseFrequencySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ExpenseTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'],
        operation_id='Gen_DT_ExpenseType_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
            serializer = Gen_DT_ExpenseTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ExpenseTypeSerializer(Gen_DT_ExpenseType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'],
        operation_id='Gen_DT_ExpenseType_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ExpenseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'],
        operation_id='Gen_DT_ExpenseType_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
        serializer = Gen_DT_ExpenseTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'],
        operation_id='Gen_DT_ExpenseType_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
        obj.delete()
        serializer = Gen_DT_ExpenseTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_LegalExpencesAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'],
        operation_id='Gen_DT_LegalExpences_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
            serializer = Gen_DT_LegalExpencesSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_LegalExpencesSerializer(Gen_DT_LegalExpences.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_201_CREATED: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'],
        operation_id='Gen_DT_LegalExpences_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_LegalExpencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'],
        operation_id='Gen_DT_LegalExpences_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
        serializer = Gen_DT_LegalExpencesSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'],
        operation_id='Gen_DT_LegalExpences_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
        obj.delete()
        serializer = Gen_DT_LegalExpencesSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpLegalStatusAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'],
        operation_id='Gen_DT_EmpLegalStatus_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
            serializer = Gen_DT_EmpLegalStatusSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpLegalStatusSerializer(Gen_DT_EmpLegalStatus.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'],
        operation_id='Gen_DT_EmpLegalStatus_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpLegalStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'],
        operation_id='Gen_DT_EmpLegalStatus_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
        serializer = Gen_DT_EmpLegalStatusSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'],
        operation_id='Gen_DT_EmpLegalStatus_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpLegalStatusSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'],
        operation_id='Gen_DT_EmpTaxType_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
            serializer = Gen_DT_EmpTaxTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxTypeSerializer(Gen_DT_EmpTaxType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'],
        operation_id='Gen_DT_EmpTaxType_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'],
        operation_id='Gen_DT_EmpTaxType_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
        serializer = Gen_DT_EmpTaxTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'],
        operation_id='Gen_DT_EmpTaxType_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxPayerAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'],
        operation_id='Gen_DT_EmpTaxPayer_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
            serializer = Gen_DT_EmpTaxPayerSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxPayerSerializer(Gen_DT_EmpTaxPayer.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'],
        operation_id='Gen_DT_EmpTaxPayer_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxPayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'],
        operation_id='Gen_DT_EmpTaxPayer_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
        serializer = Gen_DT_EmpTaxPayerSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'],
        operation_id='Gen_DT_EmpTaxPayer_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxPayerSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_OurCompanyAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'],
        operation_id='Gen_DT_OurCompany_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_OurCompany, pk=pk)
            serializer = Gen_DT_OurCompanySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_OurCompanySerializer(Gen_DT_OurCompany.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'],
        operation_id='Gen_DT_OurCompany_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_OurCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'],
        operation_id='Gen_DT_OurCompany_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_OurCompany, pk=pk)
        serializer = Gen_DT_OurCompanySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'],
        operation_id='Gen_DT_OurCompany_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_OurCompany, pk=pk)
        obj.delete()
        serializer = Gen_DT_OurCompanySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ContractAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'],
        operation_id='Gen_DT_Contract_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Contract, pk=pk)
            serializer = Gen_DT_ContractSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ContractSerializer(Gen_DT_Contract.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_201_CREATED: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'],
        operation_id='Gen_DT_Contract_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'],
        operation_id='Gen_DT_Contract_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Contract, pk=pk)
        serializer = Gen_DT_ContractSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'],
        operation_id='Gen_DT_Contract_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Contract, pk=pk)
        obj.delete()
        serializer = Gen_DT_ContractSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxCalcAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'],
        operation_id='Gen_DT_EmpTaxCalc_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
            serializer = Gen_DT_EmpTaxCalcSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxCalcSerializer(Gen_DT_EmpTaxCalc.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'],
        operation_id='Gen_DT_EmpTaxCalc_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxCalcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'],
        operation_id='Gen_DT_EmpTaxCalc_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
        serializer = Gen_DT_EmpTaxCalcSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'],
        operation_id='Gen_DT_EmpTaxCalc_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxCalcSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_PaymentBDHistoryAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'],
        operation_id='Gen_DT_PaymentBDHistory_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
            serializer = Gen_DT_PaymentBDHistorySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_PaymentBDHistorySerializer(Gen_DT_PaymentBDHistory.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'],
        operation_id='Gen_DT_PaymentBDHistory_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_PaymentBDHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'],
        operation_id='Gen_DT_PaymentBDHistory_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
        serializer = Gen_DT_PaymentBDHistorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'],
        operation_id='Gen_DT_PaymentBDHistory_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
        obj.delete()
        serializer = Gen_DT_PaymentBDHistorySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ProgressDocsAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'],
        operation_id='Gen_DT_ProgressDocs_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
            serializer = Gen_DT_ProgressDocsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ProgressDocsSerializer(Gen_DT_ProgressDocs.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_201_CREATED: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'],
        operation_id='Gen_DT_ProgressDocs_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ProgressDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'],
        operation_id='Gen_DT_ProgressDocs_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
        serializer = Gen_DT_ProgressDocsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'],
        operation_id='Gen_DT_ProgressDocs_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
        obj.delete()
        serializer = Gen_DT_ProgressDocsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_PaymentsAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'],
        operation_id='Gen_DT_Payments_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Payments, pk=pk)
            serializer = Gen_DT_PaymentsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_PaymentsSerializer(Gen_DT_Payments.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_201_CREATED: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'],
        operation_id='Gen_DT_Payments_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_PaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'],
        operation_id='Gen_DT_Payments_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Payments, pk=pk)
        serializer = Gen_DT_PaymentsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'],
        operation_id='Gen_DT_Payments_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Payments, pk=pk)
        obj.delete()
        serializer = Gen_DT_PaymentsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class DocAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'],
        operation_id='Doc_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Doc, pk=pk)
            serializer = DocSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = DocSerializer(Doc.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=DocSerializer, responses={HTTP_201_CREATED: DocSerializer()}, tags=['Doc'],
        operation_id='Doc_post')
    def post(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'],
        operation_id='Doc_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Doc, pk=pk)
        serializer = DocSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'],
        operation_id='Doc_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Doc, pk=pk)
        obj.delete()
        serializer = DocSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class DocBulkUploadAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'],
        operation_id='DocBulkUpload_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(DocBulkUpload, pk=pk)
            serializer = DocBulkUploadSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = DocBulkUploadSerializer(DocBulkUpload.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'],
        operation_id='DocBulkUpload_post')
    def post(self, request, *args, **kwargs):
        serializer = DocBulkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'],
        operation_id='DocBulkUpload_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(DocBulkUpload, pk=pk)
        serializer = DocBulkUploadSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'],
        operation_id='DocBulkUpload_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(DocBulkUpload, pk=pk)
        obj.delete()
        serializer = DocBulkUploadSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class EmployeeAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'],
        operation_id='Employee_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = EmployeeSerializer(Employee.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_201_CREATED: EmployeeSerializer()}, tags=['Employee'],
        operation_id='Employee_post')
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='multipart/form-data')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'],
        operation_id='Employee_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'],
        operation_id='Employee_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Employee, pk=pk)
        obj.delete()
        serializer = EmployeeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class EmployeeBulkUploadAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'],
        operation_id='EmployeeBulkUpload_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(EmployeeBulkUpload, pk=pk)
            serializer = EmployeeBulkUploadSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = EmployeeBulkUploadSerializer(EmployeeBulkUpload.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_201_CREATED: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'],
        operation_id='EmployeeBulkUpload_post')
    def post(self, request, *args, **kwargs):
        serializer = EmployeeBulkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'],
        operation_id='EmployeeBulkUpload_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(EmployeeBulkUpload, pk=pk)
        serializer = EmployeeBulkUploadSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'],
        operation_id='EmployeeBulkUpload_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(EmployeeBulkUpload, pk=pk)
        obj.delete()
        serializer = EmployeeBulkUploadSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class Gen_DT_PatentPricesDetailsAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_PatentPricesDetailsSerializer, responses={HTTP_200_OK: Gen_DT_PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'],
        operation_id='Gen_DT_PatentPricesDetails_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_PatentPricesDetails, pk=pk)
            serializer = Gen_DT_PatentPricesDetailsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_PatentPricesDetailsSerializer(Gen_DT_PatentPricesDetails.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=Gen_DT_PatentPricesDetailsSerializer, responses={HTTP_201_CREATED: Gen_DT_PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'],
        operation_id='Gen_DT_PatentPricesDetails_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_PatentPricesDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_PatentPricesDetailsSerializer, responses={HTTP_200_OK: Gen_DT_PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'],
        operation_id='Gen_DT_PatentPricesDetails_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_PatentPricesDetails, pk=pk)
        serializer = Gen_DT_PatentPricesDetailsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_PatentPricesDetailsSerializer, responses={HTTP_200_OK: Gen_DT_PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'],
        operation_id='Gen_DT_PatentPricesDetails_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_PatentPricesDetails, pk=pk)
        obj.delete()
        serializer = Gen_DT_PatentPricesDetailsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class Gen_DT_ClientAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    @extend_schema(request=Gen_DT_ClientSerializer, responses={HTTP_200_OK: Gen_DT_ClientSerializer()}, tags=['Gen_DT_Client'],
        operation_id='Gen_DT_Client_get')
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Client, pk=pk)
            serializer = Gen_DT_ClientSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ClientSerializer(Gen_DT_Client.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=Gen_DT_ClientSerializer, responses={HTTP_201_CREATED: Gen_DT_ClientSerializer()}, tags=['Gen_DT_Client'],
        operation_id='Gen_DT_Client_post')
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ClientSerializer, responses={HTTP_200_OK: Gen_DT_ClientSerializer()}, tags=['Gen_DT_Client'],
        operation_id='Gen_DT_Client_put')
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Client, pk=pk)
        serializer = Gen_DT_ClientSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ClientSerializer, responses={HTTP_200_OK: Gen_DT_ClientSerializer()}, tags=['Gen_DT_Client'],
        operation_id='Gen_DT_Client_delete')
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Client, pk=pk)
        obj.delete()
        serializer = Gen_DT_ClientSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')