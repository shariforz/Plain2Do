from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, Q
import math
from api.currency import USD, EUR, TRY


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class PermitDocCategory(models.Model):
    """DocumentCategory"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        # verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Citizenship(models.Model):
    """Citizenship"""

    name = models.CharField(max_length=100)

    class Meta:
        # verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    """DocumentType"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Gen_DT_DocumentType(models.Model):
    """Gen_DT_DocumentType"""

    DocumentTypeEN = models.CharField(max_length=200)
    DocumentTypeRU = models.CharField(max_length=200)
    DocumentTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["DocumentTypeEN"]

    def __str__(self):
        return self.DocumentTypeEN


class Gen_DT_Country(models.Model):
    """Gen_DT_Country"""

    CountryCode = models.CharField(max_length=50, unique=True)
    CountryEN = models.CharField(max_length=100, blank=True)
    CountryRU = models.CharField(max_length=100, blank=True)
    CountryTR = models.CharField(max_length=100, blank=True)
    AlphaCode2 = models.CharField(max_length=10, verbose_name="AlphaCode(2)", blank=True)
    AlphaCode3 = models.CharField(max_length=10, verbose_name="AlphaCode(3)", blank=True)
    CountriesForRF = models.BooleanField(default=False, blank=True)
    LocalEEC = models.BooleanField(default=False, verbose_name="Local/ EEC", blank=True)
    RvpVnj = models.BooleanField(default=False, verbose_name="RVP/ VNJ", blank=True)
    Visa = models.BooleanField(default=False, blank=True)
    VKS = models.BooleanField(default=False, blank=True)
    Patent = models.BooleanField(default=False, blank=True)

    class Meta:
        # verbose_name =CountryEN "Наименование"
        ordering = ["CountryEN"]

    def __str__(self):
        return self.CountryEN


class Gen_DT_Discipline(models.Model):
    """Gen_DT_Discipline"""

    DisciplineEN = models.CharField(max_length=200)
    DisciplineRU = models.CharField(max_length=200)
    DisciplineTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["DisciplineEN"]

    def __str__(self):
        return self.DisciplineEN


class Gen_DT_EmpLevel(models.Model):
    """Gen_DT_EmpLevel"""

    EmpLevelEN = models.CharField(max_length=200)
    EmpLevelRU = models.CharField(max_length=200)
    EmpLevelTR = models.CharField(max_length=200)
    OfficeEmp = models.BooleanField(default=False, blank=True)
    ProjectEmp = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ["EmpLevelEN"]

    def __str__(self):
        return self.EmpLevelEN


class Gen_DT_EmpClass(models.Model):
    """Gen_DT_EmpClass"""

    EmpClassEN = models.CharField(max_length=200)
    EmpClassRU = models.CharField(max_length=200)
    EmpClassTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpClassEN"]

    def __str__(self):
        return self.EmpClassEN


class Gen_DT_JobTitle(models.Model):
    """Gen_DT_JobTitle"""

    JobTitleEN = models.CharField(max_length=200)
    JobTitleRU = models.CharField(max_length=200)
    JobTitleTR = models.CharField(max_length=200)

    EmpLevel = models.ForeignKey(
        Gen_DT_EmpLevel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Level"
    )

    EmpClass = models.ForeignKey(
        Gen_DT_EmpClass, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Class"
    )

    class Meta:
        ordering = ["JobTitleEN"]

    def __str__(self):
        return self.JobTitleEN


class Gen_DT_Currency(models.Model):
    """Gen_DT_Currency"""

    CurrencyNumber = models.IntegerField(unique=True)
    CurrencyID_1C = models.CharField(max_length=100, blank=True)
    CurrencyCode = models.CharField(max_length=100, blank=True)
    CountryAlphaCode2 = models.CharField(max_length=10, blank=True, verbose_name="AlphaCode(2)")
    CountryAlphaCode3 = models.CharField(max_length=10, blank=True, verbose_name="AlphaCode(3)")
    CurrencyEN = models.CharField(max_length=200, blank=True)
    CurrencyRU = models.CharField(max_length=200, blank=True)
    CurrencyTR = models.CharField(max_length=200, blank=True)
    ActiveCurr = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ["CurrencyNumber"]

    def __str__(self):
        return self.CurrencyNumber


class Gen_DT_CBR_Rates(models.Model):
    """Gen_DT_CBR_Rates"""

    DateCBR = models.DateField()
    RateUSD = models.CharField(max_length=200)
    RateEUR = models.CharField(max_length=200)

    class Meta:
        ordering = ["RateEUR"]

    def __str__(self):
        return self.RateEUR


class Gen_DT_CounterParty(models.Model):
    """Gen_DT_CounterParty"""

    CounterPartyID_1C = models.CharField(max_length=100, blank=True)
    CounterPartyEN = models.CharField(max_length=200)
    CounterPartyRU = models.CharField(max_length=200)
    CounterPartyTR = models.CharField(max_length=200)
    CounterPartyINN = models.CharField(max_length=200)
    CounterPartyKPP = models.CharField(max_length=200, blank=True)
    Client = models.BooleanField(default=False, blank=True)
    ClientGroup = models.CharField(max_length=100, blank=True)
    Supplier = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ["CounterPartyEN"]

    def __str__(self):
        return self.CounterPartyEN


class Gen_DT_SubjectOfRF(models.Model):
    """Gen_DT_SubjectOfRF"""

    SubjectOfRF_EN = models.CharField(max_length=200)
    SubjectOfRF_RU = models.CharField(max_length=200)
    SubjectOfRF_TR = models.CharField(max_length=200)
    SubjRF_Abbreviation = models.CharField(max_length=200, blank=True)
    FederalDistrictEN = models.CharField(max_length=200, blank=True)
    FederalDistrictRU = models.CharField(max_length=200, blank=True)
    FederalDistrictTR = models.CharField(max_length=200, blank=True)
    OKATO_CODE = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["SubjectOfRF_EN"]

    def __str__(self):
        return self.SubjectOfRF_EN


class Gen_DT_Project(models.Model):
    """Gen_DT_Project"""

    ProjectID_1C = models.CharField(max_length=100, blank=True)
    ProjectCode = models.CharField(max_length=200, blank=True)
    ProjectNameEN = models.CharField(max_length=200)
    ProjectNameRU = models.CharField(max_length=200)
    ProjectNameTR = models.CharField(max_length=200)

    SubjectofRF = models.ForeignKey(
        Gen_DT_SubjectOfRF, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Subject of RF"
    )

    AddressEN = models.CharField(max_length=200, blank=True)
    AddressRU = models.CharField(max_length=200, blank=True)
    AddressTR = models.CharField(max_length=200, blank=True)
    StartDate = models.DateField(blank=True)
    EndDate = models.DateField(blank=True)

    class Meta:
        ordering = ["ProjectNameEN"]

    def __str__(self):
        return self.ProjectNameEN


class Gen_DT_CounterPartyType(models.Model):
    """Gen_DT_CounterPartyType"""

    CounterPartyTypeEN = models.CharField(max_length=200)
    CounterPartyTypeRU = models.CharField(max_length=200)
    CounterPartyTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["CounterPartyTypeEN"]

    def __str__(self):
        return self.CounterPartyTypeEN


class Gen_DT_ContractType(models.Model):
    """Gen_DT_ContractType"""

    ContractTypeEN = models.CharField(max_length=200)
    ContractTypeRU = models.CharField(max_length=200)
    ContractTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["ContractTypeEN"]

    def __str__(self):
        return self.ContractTypeEN


class Gen_DT_VAT_Rate(models.Model):
    """Gen_DT_VAT_Rate"""

    VAT_Rate = models.IntegerField()

    class Meta:
        ordering = ["VAT_Rate"]

    def __str__(self):
        return self.VAT_Rate


class Gen_DT_UoM(models.Model):
    """Gen_DT_UoM"""

    UoM_Code_1C = models.CharField(max_length=20, blank=True)
    UoM_Short_EN = models.CharField(max_length=200)
    UoM_Short_RU = models.CharField(max_length=200)
    UoM_Short_TR = models.CharField(max_length=200)
    UoM_EN = models.CharField(max_length=200, blank=True)
    UoM_RU = models.CharField(max_length=200, blank=True)
    UoM_TR = models.CharField(max_length=200, blank=True)
    UoM_Active = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ["UoM_Short_EN"]

    def __str__(self):
        return self.UoM_Short_EN


class Gen_DT_BudgetData(models.Model):
    """Gen_DT_BudgetData"""
    Project = models.ForeignKey(Gen_DT_Project, on_delete=models.SET_NULL, null=True)
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    APPROVAL_STATUS = [
        ('success', 'success'),
        ('rejected', 'rejected'),
    ]
    VersionDate = models.DateField(default=timezone.now)
    BudgetVersion = models.IntegerField(default=1)
    Status = models.CharField(max_length=56, choices=APPROVAL_STATUS)

    class Meta:
        # verbose_name =CountryEN "Наименование"
        ordering = ["id"]

    def __str__(self):
        return self.Status


class Gen_DT_BudgetDetails(models.Model):
    Budget_ID = models.ForeignKey(Gen_DT_BudgetData, on_delete=models.SET_NULL, verbose_name='Budget ID', null=True)
    Discipline = models.ForeignKey(
        Gen_DT_Discipline, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Discipline")

    BudgetCode = models.CharField(max_length=100, blank=True)
    PrimaveraCode = models.CharField(max_length=100, blank=True)

    JotTitle = models.ForeignKey(
        Gen_DT_JobTitle, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Job Title")

    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")

    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")

    UoM = models.ForeignKey(
        Gen_DT_UoM, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="UoM")

    StartOfWorkDate = models.DateField(blank=True)
    EndOfWorkDate = models.DateField(blank=True)

    EmpQty = models.IntegerField(blank=True)
    EmpNetSalary = models.FloatField(blank=True)

    class Meta:
        # verbose_name =CountryEN "Наименование"
        ordering = ["BudgetCode"]
        indexes = [
            models.Index(fields=['Budget_ID']),
        ]

    def __str__(self):
        return self.BudgetCode

    def calculate_salary(self):
        tax_percent = {"VKS": 13, "Visa": 43, "Local/ EEC": 43, 'RVP/ VNJ': 43, "Patent": 43}
        month_diff = self.EndOfWorkDate.month - self.StartOfWorkDate.month
        day_diff = self.EndOfWorkDate.day - self.StartOfWorkDate.day
        day_difference = (self.EndOfWorkDate - self.StartOfWorkDate).days
        year_difference = self.EndOfWorkDate.year - self.StartOfWorkDate.year
        adjusted_month_diff = month_diff + (1 if day_diff > 0 else 0)
        salary_per_day = self.EmpNetSalary / 30
        salary = salary_per_day * day_difference * self.EmpQty
        taxes = 0
        if self.LegDocumentType.DocumentTypeEN == "Visa":
            if day_difference <= 182:
                taxes = 60 / 100 * salary
            elif day_difference > 182:
                remaining_days = day_difference - 182
                taxes = salary_per_day * 182 * 0.6 + salary_per_day * remaining_days * 0.43
        else:
            taxes = (tax_percent[self.LegDocumentType.DocumentTypeEN]) / 100 * salary
        expense_frequency = ["First Month", "Every Month", "Monthly", "Yearly", "Every 3 Year"]
        legal_expenses = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN).values('ExpensePrice',
                                                                                        'ExpenseFrequency__ExpenseFrequencyEN')
        FIRST_MONTH_TOTAL_RUB = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN,
            ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0], Currency__CurrencyCode="RUB").values(
            'ExpensePrice', 'Currency__CurrencyCode').aggregate(total=Sum('ExpensePrice'))
        FIRST_MONTH_TOTAL_TRY = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN,
            ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0], Currency__CurrencyCode="TRY").values(
            'ExpensePrice', 'Currency__CurrencyCode').aggregate(total=Sum('ExpensePrice'))
        FIRST_MONTH_TOTAL_EUR = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN,
            ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0], Currency__CurrencyCode="EUR").values(
            'ExpensePrice', 'Currency__CurrencyCode').aggregate(total=Sum('ExpensePrice'))
        FIRST_MONTH_TOTAL = FIRST_MONTH_TOTAL_RUB['total'] + (
            1 if FIRST_MONTH_TOTAL_EUR['total'] is None else FIRST_MONTH_TOTAL_EUR['total']) * round(EUR, 2) + (
                                1 if FIRST_MONTH_TOTAL_TRY['total'] is None else FIRST_MONTH_TOTAL_TRY[
                                    'total']) * round(TRY, 2)

        EVERY_MONTHS_TOTAL = Gen_DT_LegalExpences.objects.filter(
            Q(LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN) & (
                        Q(ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[1]) | Q(
                    ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[2]))).values('ExpensePrice').aggregate(
            total=Sum('ExpensePrice'))
        YEARLY_TOTAL = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN,
            ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[3]).values('ExpensePrice').aggregate(
            total=Sum('ExpensePrice'))
        EVERY_3_YEAR_TOTAL = Gen_DT_LegalExpences.objects.filter(
            LegDocumentType__DocumentTypeEN=self.LegDocumentType.DocumentTypeEN,
            ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[4]).values('ExpensePrice').aggregate(
            total=Sum('ExpensePrice'))
        month_cost = yearly_cost = every_3_year_cost = 0
        for i in legal_expenses:
            if i['ExpenseFrequency__ExpenseFrequencyEN'] in [expense_frequency[1], expense_frequency[2]]:
                month_cost = EVERY_MONTHS_TOTAL['total'] * adjusted_month_diff
            elif i['ExpenseFrequency__ExpenseFrequencyEN'] == expense_frequency[3]:
                yearly = year_difference + (1 if month_diff > 0 else 0)
                yearly_cost = yearly * YEARLY_TOTAL['total']
            elif i['ExpenseFrequency__ExpenseFrequencyEN'] == expense_frequency[4]:
                every_3_year = 1 if day_difference > 0 and year_difference <= 3 else math.ceil(year_difference / 3)
                every_3_year_cost = every_3_year * EVERY_3_YEAR_TOTAL['total']
        TOTAL_LEGAL_EXPENSES = (month_cost + yearly_cost + every_3_year_cost + FIRST_MONTH_TOTAL) * self.EmpQty
        return {"days_diff": day_difference, "month_diff": adjusted_month_diff, 'year_diff': year_difference,
                "salary": round(salary, 1), "taxes": round(taxes, 1), 'LegalExpenses': round(TOTAL_LEGAL_EXPENSES, 2)}


class Gen_DT_BudgetDataHistory(models.Model):
    """Gen_DT_BudgetDataHistory"""

    BudgetDate = models.DateField()

    BudgetID = models.ForeignKey(
        Gen_DT_BudgetData, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Budget ID")

    ProjectID = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project ID")
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Author", null=True)

    # user

    class Meta:
        ordering = ["BudgetDate"]

    def __str__(self):
        return self.BudgetDate


class Gen_DT_ExpenseFrequency(models.Model):
    """Gen_DT_ExpenseFrequency"""

    ExpenseFrequencyEN = models.CharField(max_length=200)
    ExpenseFrequencyRU = models.CharField(max_length=200)
    ExpenseFrequencyTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["ExpenseFrequencyEN"]

    def __str__(self):
        return self.ExpenseFrequencyEN


class Gen_DT_ExpenseType(models.Model):
    """Gen_DT_ExpenseType"""

    ExpenseTypeEN = models.CharField(max_length=200)
    ExpenseTypeRU = models.CharField(max_length=200)
    ExpenseTypeTR = models.CharField(max_length=200)

    # ExpenseFrequency = models.ForeignKey(
    #     Gen_DT_ExpenseFrequency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expense Frequency")

    class Meta:
        ordering = ["ExpenseTypeEN"]

    def __str__(self):
        return self.ExpenseTypeEN


class Gen_DT_LegalExpences(models.Model):
    """Gen_DT_LegalExpences"""

    ProjectID = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project ID")

    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")

    ExpeneseCountry = models.ForeignKey(
        Gen_DT_Country, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expenese Country")

    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")

    ExpenseType = models.ForeignKey(
        Gen_DT_ExpenseType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expense Type")

    ExpensePrice = models.FloatField(blank=True)

    LegalExpenseActive = models.BooleanField(default=True, blank=True)

    EffectiveDate = models.DateField(blank=True)

    ExpenseFrequency = models.ForeignKey(
        Gen_DT_ExpenseFrequency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Expense Frequency'
    )

    class Meta:
        ordering = ["ProjectID"]

    def __str__(self):
        return str(self.ProjectID)


class Gen_DT_EmpLegalStatus(models.Model):
    """Gen_DT_EmpLegalStatus"""

    EmpLegalStatusEN = models.CharField(max_length=200)
    EmpLegalStatusRU = models.CharField(max_length=200)
    EmpLegalStatusTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpLegalStatusEN"]

    def __str__(self):
        return self.EmpLegalStatusEN


class Gen_DT_EmpTaxType(models.Model):
    """Gen_DT_EmpTaxType"""

    EmpTaxTypeEN = models.CharField(max_length=200)
    EmpTaxTypeRU = models.CharField(max_length=200)
    EmpTaxTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpTaxTypeEN"]

    def __str__(self):
        return self.EmpTaxTypeEN


class Gen_DT_EmpTaxPayer(models.Model):
    """Gen_DT_EmpTaxPayer"""

    EmpTaxCategoryCode = models.CharField(max_length=200, blank=True)

    EmpTaxCategoryEN = models.CharField(max_length=200)
    EmpTaxCategoryRU = models.CharField(max_length=200)
    EmpTaxCategoryTR = models.CharField(max_length=200)

    EmpTaxType = models.ForeignKey(
        Gen_DT_EmpTaxType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Tax Type")

    UniformBaseValueLimitUCVB = models.FloatField(verbose_name="UniformBaseValueLimit(UCVB)")
    WithinLimit = models.FloatField(blank=True)
    AboveLimit = models.FloatField(blank=True)

    class Meta:
        ordering = ["EmpTaxCategoryEN"]

    def __str__(self):
        return self.EmpTaxCategoryEN


class Gen_DT_OurCompany(models.Model):
    """Gen_DT_OurCompany"""

    OurCompanyID_1C = models.CharField(max_length=100, blank=True)
    OurCompanyEN = models.CharField(max_length=200)
    OurCompanyRU = models.CharField(max_length=200)
    OurCompanyTR = models.CharField(max_length=200)
    OurCompanyINN = models.CharField(max_length=200, blank=True)
    OurCompanyKPP = models.CharField(max_length=200, blank=True)
    ShortCode = models.CharField(max_length=100, blank=True)

    TaxPayer = models.ForeignKey(
        Gen_DT_EmpTaxPayer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tax Payer")

    class Meta:
        ordering = ["OurCompanyEN"]

    def __str__(self):
        return self.OurCompanyEN


class Gen_DT_Contract(models.Model):
    """Gen_DT_Contract"""

    ContractID_1C = models.CharField(max_length=100, blank=True)
    ContractsNo = models.CharField(max_length=200)
    ContractDate = models.DateField(blank=True)
    ContractsSubject = models.CharField(max_length=200, blank=True)

    OurCompany = models.ForeignKey(
        Gen_DT_OurCompany, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Our Company")

    ContractType = models.ForeignKey(
        Gen_DT_ContractType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Contract Type")

    CounterParty = models.ForeignKey(
        Gen_DT_CounterParty, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Counter Party")

    CounterPartyType = models.ForeignKey(
        Gen_DT_CounterPartyType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Counter Party Type")

    Project = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project")

    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")

    ContractAmountVatWo = models.FloatField(blank=True)

    VAT_Rate = models.ForeignKey(
        Gen_DT_VAT_Rate, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="VAT Rate")

    ContractStartDate = models.DateField(blank=True)
    ContractEndDate = models.DateField(blank=True)

    class Meta:
        ordering = ["ContractsSubject"]

    def __str__(self):
        return self.ContractsSubject


class Gen_DT_EmpTaxCalc(models.Model):
    """Gen_DT_EmpTaxCalc"""

    EmpTaxRateEN = models.CharField(max_length=200)
    EmpTaxRateRU = models.CharField(max_length=200)
    EmpTaxRateTR = models.CharField(max_length=200)

    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")

    TaxCodeSSF = models.IntegerField(blank=True)
    TaxCodePIT_Until182day = models.IntegerField(blank=True)
    TaxCodePIT_After182day = models.IntegerField(blank=True)

    class Meta:
        ordering = ["EmpTaxRateEN"]

    def __str__(self):
        return self.EmpTaxRateEN


class Gen_DT_PaymentBDHistory(models.Model):
    """Gen_DT_PaymentBDHistory"""

    FloatingRate = models.IntegerField(blank=True)
    FixedRate = models.IntegerField(blank=True)
    FixedRateCurrency = models.FloatField(blank=True)
    PaymentBreakdownDate = models.DateField(blank=True)

    @property
    def FloatingRatePerc(self):
        return f"{self.FloatingRate} %"

    @property
    def FixedRatePerc(self):
        return f"{self.FixedRate} %"

    ContractID = models.ForeignKey(
        Gen_DT_Contract, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Contract")

    class Meta:
        ordering = ["PaymentBreakdownDate"]

    def __str__(self):
        return self.PaymentBreakdownDate


class Gen_DT_ProgressDocs(models.Model):
    """Gen_DT_ProgressDocs"""

    PaymentID_1C = models.CharField(max_length=200, blank=True)

    PBHistoryID = models.ForeignKey(
        Gen_DT_PaymentBDHistory, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Payment BreakDown History")

    ProgressPeriodStart = models.DateField(blank=True)
    ProgressPeriodEnd = models.DateField(blank=True)
    ProgressDate = models.DateField(blank=True)
    ProgressAmountVatWo = models.IntegerField(blank=True)
    AdvanceDeduction = models.IntegerField(blank=True)
    OtherDeductions = models.IntegerField(blank=True)

    CURRENT_STATUS_CHOICES = [("signed", "Подписано"), ("approved", "Одобрено")]

    current_status = models.CharField(
        max_length=15, choices=CURRENT_STATUS_CHOICES, default="signed", verbose_name="Статус")

    class Meta:
        ordering = ["PaymentID_1C"]

    def __str__(self):
        return self.PaymentID_1C


class Gen_DT_Payments(models.Model):
    """Gen_DT_Payments"""

    PaymentID_1C = models.CharField(max_length=200, blank=True)

    ContractID = models.ForeignKey(
        Gen_DT_Contract, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Contract")

    ProgressID = models.ForeignKey(
        Gen_DT_ProgressDocs, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Progress Docs")

    PaymentDate = models.DateField(blank=True)

    PAYMENT_TYPE_CHOICES = [("Advance", "Аванс"), ("Progress", "Прогресс"), ("3rd Party", "3ая сторона")]

    PaymentType = models.CharField(
        max_length=10, choices=PAYMENT_TYPE_CHOICES, default="Advance", verbose_name="Тип оплаты")

    PaymentBreakdown = models.FloatField(blank=True)
    PaymentAmountFloating = models.FloatField(blank=True)

    PaymentCurrencyFloating = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Progress Docs")

    PaymentAmountFixed = models.FloatField(blank=True)
    PaymentCurrencyFixed = models.FloatField(blank=True)
    Comment = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["PaymentID_1C"]

    def __str__(self):
        return self.PaymentID_1C


class Gen_DT_PatentPricesDetails(models.Model):
    """PatentPricesDetail"""
    SubjectofRF_ID = models.ForeignKey(Gen_DT_SubjectOfRF, on_delete=models.SET_NULL, blank=True, null=True,
                                       verbose_name="Gen_DT_SubjectOfRF")
    RegionalCoefficient_Base = models.CharField(max_length=256)
    Amount = models.FloatField(blank=True)
    MonthlyPatentPayment = models.FloatField(null=True)
    Active = models.BooleanField()
    Effective_Date = models.DateField(blank=True)

    class Meta:
        ordering = ['SubjectofRF_ID']

    def __str__(self):
        return self.RegionalCoefficient_Base


class Gen_DT_Client(models.Model):
    """Client"""
    ClientID = models.IntegerField()
    ClientShortNameRU = models.CharField(max_length=56)
    ClientShortNameEN = models.CharField(max_length=56)
    ClientINN = models.BigIntegerField()
    ClientKPP = models.IntegerField()

    class Meta:
        ordering = ['ClientID']

    def __str__(self):
        return self.ClientShortNameRU
