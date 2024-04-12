from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, is_success
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from drf_spectacular.utils import extend_schema


class SiteConfigAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=SiteConfigSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: SiteConfigSerializer(many=True)},
        tags=['SiteConfig'],
        methods=['GET']
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
        methods=['POST']
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
        methods = ['PUT']
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
        methods=['DELETE']
    )
    def delete(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(SiteConfig, pk=pk)
        SiteConfig.objects.get(pk=pk).delete()
        serializer = SiteConfigSerializer(instance=obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='application/json')


class PermitDocCategoryAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=PermitDocCategorySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: PermitDocCategorySerializer()},
        tags=['PermitDocCategory']
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
        tags=['PermitDocCategory']
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
        tags=['PermitDocCategory']
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
        tags=['PermitDocCategory']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(PermitDocCategory, pk=pk)
        serializer = PermitDocCategorySerializer(obj)
        PermitDocCategory.objects.get(pk=pk).delete()
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class CitizenshipAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=CitizenshipSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: CitizenshipSerializer()},
        tags=['Citizenship']
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
        tags=['Citizenship']
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
        tags=['Citizenship']
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
        tags=['Citizenship']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Citizenship, pk=pk)
        obj.delete()
        serializer = CitizenshipSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class DocumentTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: DocumentTypeSerializer()},
        tags=['DocumentType']
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
        tags=['DocumentType']
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
        tags=['DocumentType']
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
        tags=['DocumentType']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(DocumentType, pk=pk)
        obj.delete()
        serializer = DocumentTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_DocumentTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_DocumentTypeSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DocumentTypeSerializer()},
        tags=['Gen_DT_DocumentType']
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
        tags=['Gen_DT_DocumentType']
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
        tags=['Gen_DT_DocumentType']
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
        tags=['Gen_DT_DocumentType']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_DocumentType, pk=pk)
        obj.delete()
        serializer = Gen_DT_DocumentTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CountryAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_CountrySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CountrySerializer()},
        tags=['Gen_DT_Country']
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
        tags=['Gen_DT_Country']
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
        tags=['Gen_DT_Country']
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
        tags=['Gen_DT_Country']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Country, pk=pk)
        obj.delete()
        serializer = Gen_DT_CountrySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_DisciplineAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_DisciplineSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_DisciplineSerializer()},
        tags=['Gen_DT_Discipline']
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
        tags=['Gen_DT_Discipline']
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
        tags=['Gen_DT_Discipline']
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
        tags=['Gen_DT_Discipline']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Discipline, pk=pk)
        obj.delete()
        serializer = Gen_DT_DisciplineSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpLevelAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_EmpLevelSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpLevelSerializer()},
        tags=['Gen_DT_EmpLevel']
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
        tags=['Gen_DT_EmpLevel']
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
        tags=['Gen_DT_EmpLevel']
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
        tags=['Gen_DT_EmpLevel']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpLevel, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpLevelSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpClassAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_EmpClassSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_EmpClassSerializer()},
        tags=['Gen_DT_EmpClass']
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
        tags=['Gen_DT_EmpClass']
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
        tags=['Gen_DT_EmpClass']
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
        tags=['Gen_DT_EmpClass']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpClass, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpClassSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_JobTitleAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_JobTitleSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_JobTitleSerializer()},
        tags=['Gen_DT_JobTitle']
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
        tags=['Gen_DT_JobTitle']
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
        tags=['Gen_DT_JobTitle']
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
        tags=['Gen_DT_JobTitle']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_JobTitle, pk=pk)
        obj.delete()
        serializer = Gen_DT_JobTitleSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CurrencyAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_CurrencySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CurrencySerializer()},
        tags=['Gen_DT_Currency']
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
        tags=['Gen_DT_Currency']
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
        tags=['Gen_DT_Currency']
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
        tags=['Gen_DT_Currency']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Currency, pk=pk)
        obj.delete()
        serializer = Gen_DT_CurrencySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CBR_RatesAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_CBR_RatesSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CBR_RatesSerializer()},
        tags=['Gen_DT_CBR_Rates']
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
        tags=['Gen_DT_CBR_Rates']
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
        tags=['Gen_DT_CBR_Rates']
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
        tags=['Gen_DT_CBR_Rates']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CBR_Rates, pk=pk)
        obj.delete()
        serializer = Gen_DT_CBR_RatesSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CounterPartyAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_CounterPartySerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_CounterPartySerializer()},
        tags=['Gen_DT_CounterParty']
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
        tags=['Gen_DT_CounterParty']
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
        tags=['Gen_DT_CounterParty']
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
        tags=['Gen_DT_CounterParty']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CounterParty, pk=pk)
        obj.delete()
        serializer = Gen_DT_CounterPartySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_SubjectOfRFAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_SubjectOfRFSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_SubjectOfRFSerializer()},
        tags=['Gen_DT_SubjectOfRF']
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
        tags=['Gen_DT_SubjectOfRF']
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
        tags=['Gen_DT_SubjectOfRF']
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
        tags=['Gen_DT_SubjectOfRF']
    )
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_SubjectOfRF, pk=pk)
        obj.delete()
        serializer = Gen_DT_SubjectOfRFSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ProjectAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(
        request=Gen_DT_ProjectSerializer,  # Specify the serializer for the request
        responses={HTTP_200_OK: Gen_DT_ProjectSerializer()},
        tags=['Gen_DT_Project']
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
        tags=['Gen_DT_Project']
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
        tags=['Gen_DT_Project']
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Project, pk=pk)
        serializer = Gen_DT_ProjectSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ProjectSerializer, responses={HTTP_200_OK: Gen_DT_ProjectSerializer()}, tags=['Gen_DT_Project'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Project, pk=pk)
        obj.delete()
        serializer = Gen_DT_ProjectSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_CounterPartyTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
            serializer = Gen_DT_CounterPartyTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_CounterPartyTypeSerializer(Gen_DT_CounterPartyType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_201_CREATED: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_CounterPartyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
        serializer = Gen_DT_CounterPartyTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=SiteConfigSerializer, responses={HTTP_200_OK: Gen_DT_CounterPartyTypeSerializer()}, tags=['Gen_DT_CounterPartyType'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_CounterPartyType, pk=pk)
        obj.delete()
        serializer = Gen_DT_CounterPartyTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ContractTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ContractType, pk=pk)
            serializer = Gen_DT_ContractTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ContractTypeSerializer(Gen_DT_ContractType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ContractTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ContractType, pk=pk)
        serializer = Gen_DT_ContractTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ContractTypeSerializer, responses={HTTP_200_OK: Gen_DT_ContractTypeSerializer()}, tags=['Gen_DT_ContractType'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ContractType, pk=pk)
        obj.delete()
        serializer = Gen_DT_ContractTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_VAT_RateAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
            serializer = Gen_DT_VAT_RateSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_VAT_RateSerializer(Gen_DT_VAT_Rate.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_201_CREATED: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_VAT_RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
        serializer = Gen_DT_VAT_RateSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_VAT_RateSerializer, responses={HTTP_200_OK: Gen_DT_VAT_RateSerializer()}, tags=['Gen_DT_VAT_Rate'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_VAT_Rate, pk=pk)
        obj.delete()
        serializer = Gen_DT_VAT_RateSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_UoMAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_UoM, pk=pk)
            serializer = Gen_DT_UoMSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_UoMSerializer(Gen_DT_UoM.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_201_CREATED: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_UoMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_UoM, pk=pk)
        serializer = Gen_DT_UoMSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_UoMSerializer, responses={HTTP_200_OK: Gen_DT_UoMSerializer()}, tags=['Gen_DT_UoM'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_UoM, pk=pk)
        obj.delete()
        serializer = Gen_DT_UoMSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_BudgetDataAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_BudgetData, pk=pk)
            serializer = Gen_DT_BudgetDataSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_BudgetDataSerializer(Gen_DT_BudgetData.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_201_CREATED: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_BudgetDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_BudgetData, pk=pk)
        serializer = Gen_DT_BudgetDataSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_BudgetDataSerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataSerializer()}, tags=['Gen_DT_BudgetData'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_BudgetData, pk=pk)
        obj.delete()
        serializer = Gen_DT_BudgetDataSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_BudgetDataHistoryAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
            serializer = Gen_DT_BudgetDataHistorySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_BudgetDataHistorySerializer(Gen_DT_BudgetDataHistory.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_201_CREATED: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_BudgetDataHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
        serializer = Gen_DT_BudgetDataHistorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_BudgetDataHistorySerializer, responses={HTTP_200_OK: Gen_DT_BudgetDataHistorySerializer()}, tags=['Gen_DT_BudgetDataHistory'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_BudgetDataHistory, pk=pk)
        obj.delete()
        serializer = Gen_DT_BudgetDataHistorySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ExpenseFrequencyAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
            serializer = Gen_DT_ExpenseFrequencySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ExpenseFrequencySerializer(Gen_DT_ExpenseFrequency.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_201_CREATED: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ExpenseFrequencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
        serializer = Gen_DT_ExpenseFrequencySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ExpenseFrequencySerializer, responses={HTTP_200_OK: Gen_DT_ExpenseFrequencySerializer()}, tags=['Gen_DT_ExpenseFrequency'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ExpenseFrequency, pk=pk)
        obj.delete()
        serializer = Gen_DT_ExpenseFrequencySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ExpenseTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
            serializer = Gen_DT_ExpenseTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ExpenseTypeSerializer(Gen_DT_ExpenseType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ExpenseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
        serializer = Gen_DT_ExpenseTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ExpenseTypeSerializer, responses={HTTP_200_OK: Gen_DT_ExpenseTypeSerializer()}, tags=['Gen_DT_ExpenseType'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ExpenseType, pk=pk)
        obj.delete()
        serializer = Gen_DT_ExpenseTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_LegalExpencesAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
            serializer = Gen_DT_LegalExpencesSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_LegalExpencesSerializer(Gen_DT_LegalExpences.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_201_CREATED: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_LegalExpencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
        serializer = Gen_DT_LegalExpencesSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_LegalExpencesSerializer, responses={HTTP_200_OK: Gen_DT_LegalExpencesSerializer()}, tags=['Gen_DT_LegalExpences'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_LegalExpences, pk=pk)
        obj.delete()
        serializer = Gen_DT_LegalExpencesSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpLegalStatusAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
            serializer = Gen_DT_EmpLegalStatusSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpLegalStatusSerializer(Gen_DT_EmpLegalStatus.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpLegalStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
        serializer = Gen_DT_EmpLegalStatusSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpLegalStatusSerializer, responses={HTTP_200_OK: Gen_DT_EmpLegalStatusSerializer()}, tags=['Gen_DT_EmpLegalStatus'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpLegalStatus, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpLegalStatusSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxTypeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
            serializer = Gen_DT_EmpTaxTypeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxTypeSerializer(Gen_DT_EmpTaxType.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
        serializer = Gen_DT_EmpTaxTypeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxTypeSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxTypeSerializer()}, tags=['Gen_DT_EmpTaxType'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxType, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxTypeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxPayerAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
            serializer = Gen_DT_EmpTaxPayerSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxPayerSerializer(Gen_DT_EmpTaxPayer.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxPayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
        serializer = Gen_DT_EmpTaxPayerSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxPayerSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxPayerSerializer()}, tags=['Gen_DT_EmpTaxPayer'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxPayer, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxPayerSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_OurCompanyAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_OurCompany, pk=pk)
            serializer = Gen_DT_OurCompanySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_OurCompanySerializer(Gen_DT_OurCompany.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_OurCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_OurCompany, pk=pk)
        serializer = Gen_DT_OurCompanySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_OurCompanySerializer, responses={HTTP_200_OK: Gen_DT_OurCompanySerializer()}, tags=['Gen_DT_OurCompany'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_OurCompany, pk=pk)
        obj.delete()
        serializer = Gen_DT_OurCompanySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ContractAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Contract, pk=pk)
            serializer = Gen_DT_ContractSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ContractSerializer(Gen_DT_Contract.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_201_CREATED: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Contract, pk=pk)
        serializer = Gen_DT_ContractSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ContractSerializer, responses={HTTP_200_OK: Gen_DT_ContractSerializer()}, tags=['Gen_DT_Contract'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Contract, pk=pk)
        obj.delete()
        serializer = Gen_DT_ContractSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_EmpTaxCalcAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
            serializer = Gen_DT_EmpTaxCalcSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_EmpTaxCalcSerializer(Gen_DT_EmpTaxCalc.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_201_CREATED: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_EmpTaxCalcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
        serializer = Gen_DT_EmpTaxCalcSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_EmpTaxCalcSerializer, responses={HTTP_200_OK: Gen_DT_EmpTaxCalcSerializer()}, tags=['Gen_DT_EmpTaxCalc'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_EmpTaxCalc, pk=pk)
        obj.delete()
        serializer = Gen_DT_EmpTaxCalcSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_PaymentBDHistoryAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
            serializer = Gen_DT_PaymentBDHistorySerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_PaymentBDHistorySerializer(Gen_DT_PaymentBDHistory.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_PaymentBDHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
        serializer = Gen_DT_PaymentBDHistorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_PaymentBDHistorySerializer, responses={HTTP_200_OK: Gen_DT_PaymentBDHistorySerializer()}, tags=['Gen_DT_PaymentBDHistory'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_PaymentBDHistory, pk=pk)
        obj.delete()
        serializer = Gen_DT_PaymentBDHistorySerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_ProgressDocsAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
            serializer = Gen_DT_ProgressDocsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_ProgressDocsSerializer(Gen_DT_ProgressDocs.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_201_CREATED: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_ProgressDocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
        serializer = Gen_DT_ProgressDocsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_ProgressDocsSerializer, responses={HTTP_200_OK: Gen_DT_ProgressDocsSerializer()}, tags=['Gen_DT_ProgressDocs'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_ProgressDocs, pk=pk)
        obj.delete()
        serializer = Gen_DT_ProgressDocsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class Gen_DT_PaymentsAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Gen_DT_Payments, pk=pk)
            serializer = Gen_DT_PaymentsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = Gen_DT_PaymentsSerializer(Gen_DT_Payments.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK)

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_201_CREATED: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'])
    def post(self, request, *args, **kwargs):
        serializer = Gen_DT_PaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Gen_DT_Payments, pk=pk)
        serializer = Gen_DT_PaymentsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=Gen_DT_PaymentsSerializer, responses={HTTP_200_OK: Gen_DT_PaymentsSerializer()}, tags=['Gen_DT_Payments'])
    def delete(self, request, pk):
        obj = get_object_or_404(Gen_DT_Payments, pk=pk)
        obj.delete()
        serializer = Gen_DT_PaymentsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK)


class DocAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Doc, pk=pk)
            serializer = DocSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = DocSerializer(Doc.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=DocSerializer, responses={HTTP_201_CREATED: DocSerializer()}, tags=['Doc'])
    def post(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Doc, pk=pk)
        serializer = DocSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=DocSerializer, responses={HTTP_200_OK: DocSerializer()}, tags=['Doc'])
    def delete(self, request, pk):
        obj = get_object_or_404(Doc, pk=pk)
        obj.delete()
        serializer = DocSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class DocBulkUploadAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(DocBulkUpload, pk=pk)
            serializer = DocBulkUploadSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = DocBulkUploadSerializer(DocBulkUpload.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'])
    def post(self, request, *args, **kwargs):
        serializer = DocBulkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(DocBulkUpload, pk=pk)
        serializer = DocBulkUploadSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=DocBulkUploadSerializer, responses={HTTP_200_OK: DocBulkUploadSerializer()}, tags=['DocBulkUpload'])
    def delete(self, request, pk):
        obj = get_object_or_404(DocBulkUpload, pk=pk)
        obj.delete()
        serializer = DocBulkUploadSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class EmployeeAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = EmployeeSerializer(Employee.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_201_CREATED: EmployeeSerializer()}, tags=['Employee'])
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='application/json')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='multipart/form-data')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=EmployeeSerializer, responses={HTTP_200_OK: EmployeeSerializer()}, tags=['Employee'])
    def delete(self, request, pk):
        obj = get_object_or_404(Employee, pk=pk)
        obj.delete()
        serializer = EmployeeSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class EmployeeBulkUploadAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(EmployeeBulkUpload, pk=pk)
            serializer = EmployeeBulkUploadSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = EmployeeBulkUploadSerializer(EmployeeBulkUpload.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_201_CREATED: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'])
    def post(self, request, *args, **kwargs):
        serializer = EmployeeBulkUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(EmployeeBulkUpload, pk=pk)
        serializer = EmployeeBulkUploadSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=EmployeeBulkUploadSerializer, responses={HTTP_200_OK: EmployeeBulkUploadSerializer()}, tags=['EmployeeBulkUpload'])
    def delete(self, request, pk):
        obj = get_object_or_404(EmployeeBulkUpload, pk=pk)
        obj.delete()
        serializer = EmployeeBulkUploadSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class PatentPricesDetailsAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=PatentPricesDetailsSerializer, responses={HTTP_200_OK: PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(PatentPricesDetails, pk=pk)
            serializer = PatentPricesDetailsSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = PatentPricesDetailsSerializer(PatentPricesDetails.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=PatentPricesDetailsSerializer, responses={HTTP_201_CREATED: PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'])
    def post(self, request, *args, **kwargs):
        serializer = PatentPricesDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=PatentPricesDetailsSerializer, responses={HTTP_200_OK: PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(PatentPricesDetails, pk=pk)
        serializer = PatentPricesDetailsSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=PatentPricesDetailsSerializer, responses={HTTP_200_OK: PatentPricesDetailsSerializer()}, tags=['Gen_DT_PatentPricesDetails'])
    def delete(self, request, pk):
        obj = get_object_or_404(PatentPricesDetails, pk=pk)
        obj.delete()
        serializer = PatentPricesDetailsSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

#
# class UnitOfMeasureAPIView(APIView):
#     renderer_classes = [JSONRenderer]
#
#     @extend_schema(request=UnitOfMeasureSerializer, responses={HTTP_200_OK: UnitOfMeasureSerializer()}, tags=['UnitOfMeasure'])
#     def get(self, request, pk=None, *args, **kwargs):
#         if pk:
#             instance = get_object_or_404(UnitOfMeasure, pk=pk)
#             serializer = UnitOfMeasureSerializer(instance=instance)
#             return Response({"Response": serializer.data}, status=HTTP_200_OK)
#         serializer = UnitOfMeasureSerializer(UnitOfMeasure.objects.all().order_by('id'), many=True)
#         return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')
#
#     @extend_schema(request=UnitOfMeasureSerializer, responses={HTTP_201_CREATED: UnitOfMeasureSerializer()}, tags=['UnitOfMeasure'])
#     def post(self, request, *args, **kwargs):
#         serializer = UnitOfMeasureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
#                             content_type='multipart/form-data')
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#
#     @extend_schema(request=UnitOfMeasureSerializer, responses={HTTP_200_OK: UnitOfMeasureSerializer()}, tags=['UnitOfMeasure'])
#     def put(self, request, pk, *args, **kwargs):
#         instance = get_object_or_404(UnitOfMeasure, pk=pk)
#         serializer = UnitOfMeasureSerializer(instance=instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
#                             content_type='multipart/form-data')
#
#     @extend_schema(request=UnitOfMeasureSerializer, responses={HTTP_200_OK: UnitOfMeasureSerializer()}, tags=['UnitOfMeasure'])
#     def delete(self, request, pk):
#         obj = get_object_or_404(UnitOfMeasure, pk=pk)
#         obj.delete()
#         serializer = UnitOfMeasureSerializer(obj)
#         return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')


class ClientAPIView(APIView):
    renderer_classes = [JSONRenderer]

    @extend_schema(request=ClientSerializer, responses={HTTP_200_OK: ClientSerializer()}, tags=['Gen_DT_Client'])
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            instance = get_object_or_404(Client, pk=pk)
            serializer = ClientSerializer(instance=instance)
            return Response({"Response": serializer.data}, status=HTTP_200_OK)
        serializer = ClientSerializer(Client.objects.all().order_by('id'), many=True)
        return Response({"Response": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')

    @extend_schema(request=ClientSerializer, responses={HTTP_201_CREATED: ClientSerializer()}, tags=['Gen_DT_Client'])
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully saved": serializer.data}, status=HTTP_201_CREATED,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(request=ClientSerializer, responses={HTTP_200_OK: ClientSerializer()}, tags=['Gen_DT_Client'])
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Data is successfully edited": serializer.data}, status=HTTP_200_OK,
                            content_type='multipart/form-data')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST, content_type='application/json')

    @extend_schema(request=ClientSerializer, responses={HTTP_200_OK: ClientSerializer()}, tags=['Gen_DT_Client'])
    def delete(self, request, pk):
        obj = get_object_or_404(Client, pk=pk)
        obj.delete()
        serializer = ClientSerializer(obj)
        return Response({"Data is deleted": serializer.data}, status=HTTP_200_OK, content_type='multipart/form-data')