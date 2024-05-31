from api.calculation import Calculation
from apps.corecode.models import *
from apps.employees.models import *
from apps.docs.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class SiteConfigSerializer(ModelSerializer):
    class Meta:
        model = SiteConfig
        fields = "__all__"


class PermitDocCategorySerializer(ModelSerializer):
    class Meta:
        model = PermitDocCategory
        fields = "__all__"


class CitizenshipSerializer(ModelSerializer):
    class Meta:
        model = Citizenship
        fields = '__all__'


class DocumentTypeSerializer(ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class Gen_DT_DocumentTypeSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_DocumentType
        fields = '__all__'


class Gen_DT_CountrySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Country
        fields = '__all__'


class Gen_DT_DisciplineSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Discipline
        fields = '__all__'


class Gen_DT_EmpLevelSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpLevel
        fields = '__all__'


class Gen_DT_EmpClassSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpClass
        fields = '__all__'


class Gen_DT_JobTitleSerializer(ModelSerializer):
    EmpLevel = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_EmpLevel.objects.all(), write_only=True)
    EmpClass = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_EmpClass.objects.all(), write_only=True)
    EmpLevel_data = Gen_DT_EmpLevelSerializer(read_only=True, source='EmpLevel')
    EmpClass_data = Gen_DT_EmpClassSerializer(read_only=True, source='EmpClass')

    class Meta:
        model = Gen_DT_JobTitle
        fields = '__all__'
        # depth = 1


class Gen_DT_CurrencySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Currency
        fields = "__all__"


class Gen_DT_CBR_RatesSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_CBR_Rates
        fields = '__all__'


class Gen_DT_CounterPartySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_CounterParty
        fields = '__all__'


class Gen_DT_SubjectOfRFSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_SubjectOfRF
        fields = '__all__'


class Gen_DT_ProjectSerializer(ModelSerializer):
    # SubjectofRF = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_SubjectOfRF.objects.all(), write_only=True)
    # SubjectofRF_data = Gen_DT_SubjectOfRFSerializer(source='SubjectofRF', read_only=True)

    class Meta:
        model = Gen_DT_Project
        fields = '__all__'
        # depth = 1


class Gen_DT_CounterPartyTypeSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_CounterPartyType
        fields = '__all__'


class Gen_DT_ContractTypeSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_ContractType
        fields = '__all__'


class Gen_DT_VAT_RateSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_VAT_Rate
        fields = '__all__'


class Gen_DT_UoMSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_UoM
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class Gen_DT_BudgetDataSerializer(ModelSerializer):
    Project = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Project.objects.all(), write_only=True)
    Project_data = Gen_DT_ProjectSerializer(source='Project', read_only=True)
    Author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    Author_data = UserSerializer(source='Author', read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Gen_DT_BudgetData
        fields = '__all__'

    def get_total_cost(self, obj):
        return 123


class BudgetDetailsSerializer(ModelSerializer):
    Discipline = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Discipline.objects.all(), write_only=True)
    Currency = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Currency.objects.all(), write_only=True)
    UoM = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_UoM.objects.all(), write_only=True)
    LegDocumentType = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_DocumentType.objects.all(), write_only=True)
    JotTitle = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_JobTitle.objects.all(), write_only=True)

    Discipline_data = Gen_DT_DisciplineSerializer(read_only=True, source='Discipline')
    Currency_data = Gen_DT_CurrencySerializer(read_only=True, source='Currency')
    UoM_data = Gen_DT_UoMSerializer(read_only=True, source='UoM')
    LegDocumentType_data = Gen_DT_DocumentTypeSerializer(read_only=True, source='LegDocumentType')
    JotTitle_data = Gen_DT_JobTitleSerializer(read_only=True, source='JotTitle')
    salary = serializers.SerializerMethodField()
    day_difference = serializers.SerializerMethodField()
    month_difference = serializers.SerializerMethodField()
    year_difference = serializers.SerializerMethodField()
    taxes = serializers.SerializerMethodField()
    legal_expenses = serializers.SerializerMethodField()

    class Meta:
        model = Gen_DT_BudgetDetails
        fields = '__all__'

    def get_salary(self, obj):
        return obj.calculate_salary()['salary']

    def get_day_difference(self, obj):
        return obj.calculate_salary()['days_diff']

    def get_month_difference(self, obj):
        return obj.calculate_salary()['month_diff']

    def get_taxes(self, obj):
        return obj.calculate_salary()['taxes']

    def get_year_difference(self, obj):
        return obj.calculate_salary()['year_diff']

    def get_legal_expenses(self, obj):
        return obj.calculate_salary()['LegalExpenses']


class Gen_DT_BudgetDataHistorySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_BudgetDataHistory
        fields = '__all__'


class Gen_DT_ExpenseFrequencySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_ExpenseFrequency
        fields = '__all__'


class Gen_DT_ExpenseTypeSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_ExpenseType
        fields = '__all__'


class Gen_DT_LegalExpencesSerializer(ModelSerializer):
    ProjectID = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Project.objects.all(), write_only=True)
    LegDocumentType = serializers.PrimaryKeyRelatedField(queryset=DocumentType.objects.all(), write_only=True)
    ExpeneseCountry = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Country.objects.all(), write_only=True)
    Currency = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_Currency.objects.all(), write_only=True)
    ExpenseType = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_ExpenseType.objects.all(), write_only=True)
    ExpenseFrequency = serializers.PrimaryKeyRelatedField(queryset=Gen_DT_ExpenseFrequency.objects.all(), write_only=True)

    ProjectID_data = Gen_DT_ProjectSerializer(read_only=True, source='ProjectID')
    LegDocumentType_data = Gen_DT_DocumentTypeSerializer(read_only=True, source='LegDocumentType')
    ExpeneseCountry_data = Gen_DT_CountrySerializer(read_only=True, source='ExpeneseCountry')
    Currency_data = Gen_DT_CurrencySerializer(read_only=True, source='Currency')
    ExpenseType_data = Gen_DT_ExpenseTypeSerializer(read_only=True, source='ExpenseType')
    ExpenseFrequency_data = Gen_DT_ExpenseFrequencySerializer(read_only=True, source='ExpenseFrequency')

    class Meta:
        model = Gen_DT_LegalExpences
        fields = '__all__'


class Gen_DT_EmpLegalStatusSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpLegalStatus
        fields = '__all__'


class Gen_DT_EmpTaxTypeSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpTaxType
        fields = '__all__'


class Gen_DT_EmpTaxPayerSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpTaxPayer
        fields = '__all__'


class Gen_DT_OurCompanySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_OurCompany
        fields = '__all__'


class Gen_DT_ContractSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Contract
        fields = '__all__'


class Gen_DT_EmpTaxCalcSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_EmpTaxCalc
        fields = '__all__'


class Gen_DT_PaymentBDHistorySerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_PaymentBDHistory
        fields = '__all__'


class Gen_DT_ProgressDocsSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_ProgressDocs
        fields = '__all__'


class Gen_DT_PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Payments
        fields = '__all__'


class Gen_DT_PatentPricesDetailsSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_PatentPricesDetails
        fields = '__all__'


class Gen_DT_ClientSerializer(ModelSerializer):
    class Meta:
        model = Gen_DT_Client
        fields = '__all__'


# serializers for docs models starts from here
class DocSerializer(ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'


class DocBulkUploadSerializer(ModelSerializer):
    class Meta:
        model = DocBulkUpload
        fields = '__all__'


# serializers for employees models starts from here
class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeBulkUploadSerializer(ModelSerializer):
    class Meta:
        model = EmployeeBulkUpload
        fields = '__all__'
