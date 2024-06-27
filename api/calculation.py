from django.db.models import F, ExpressionWrapper, DurationField, Value, Case, When, FloatField, IntegerField, Sum, Q
from django.db.models.functions import Round, Coalesce, ExtractDay, ExtractMonth, ExtractYear
from datetime import timedelta
from apps.corecode.models import Gen_DT_BudgetDetails, Gen_DT_LegalExpences
from .currency import EUR, TRY, USD


def salary_calculation(Budget_ID):
    # total_sum = Gen_DT_BudgetDetails.objects.filter(Budget_ID=Budget_ID).annotate(
    #     month_diff=ExtractMonth('EndOfWorkDate') - ExtractMonth('StartOfWorkDate'),
    #     day_diff=ExtractDay('EndOfWorkDate') - ExtractDay('StartOfWorkDate'),
    # ).annotate(
    #     adjusted_month_diff=ExpressionWrapper(
    #         F('month_diff') + Case(
    #             When(day_diff__gt=1, then=1),
    #             default=0,
    #             output_field=IntegerField(),
    #         ),
    #         output_field=IntegerField()
    #     )
    # ).annotate(
    #     product=F('adjusted_month_diff') * F('EmpQty') * F('EmpNetSalary')
    # )
    # print(total_sum.aggregate(
    #     total=Sum('product')
    # )['total'])
    # for i in total_sum:
    #     print(i.product)
    expense_frequency = ["First Month", "Every Month", "Monthly", "Yearly", "Every 3 Year"]
    tax_percent = {"VKS": 13, "Visa": 43, "Local/ EEC": 43, 'RVP/ VNJ': 43, "Patent": 43}

    legal_expenses = Gen_DT_LegalExpences.objects.filter(LegDocumentType__DocumentTypeEN="VKS").annotate(
        first_month=Case(
            When(
                Q(Currency__CurrencyEN='RUB') & Q(ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0]),
                then=Sum('ExpensePrice')
            ),
            When(
                Q(Currency__CurrencyEN='EUR') & Q(ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0]),
                then=EUR * Sum('ExpensePrice')
            ),
            When(
                Q(Currency__CurrencyEN='TRY') & Q(ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0]),
                then=TRY * Sum('ExpensePrice')
            ),
            default=Value(0),
            output_field=FloatField()
        ),
    )
    total_cost = Gen_DT_LegalExpences.objects.filter(
        LegDocumentType__DocumentTypeEN='VKS',
        ExpenseFrequency__ExpenseFrequencyEN=expense_frequency[0]
    ).aggregate(
        total_cost=Sum('ExpensePrice')
    )
    print(total_cost['total_cost'])
    # print(">>>>>>", legal_expenses.values('first_month'))

    total_sum = Gen_DT_BudgetDetails.objects.filter(Budget_ID=Budget_ID).annotate(
        day_diff=ExtractDay('EndOfWorkDate') - ExtractDay('StartOfWorkDate'),
        day_difference=ExpressionWrapper(
            (F('EndOfWorkDate') - F('StartOfWorkDate')) / timedelta(days=1),
            output_field=IntegerField()
        ),
        month_diff=ExtractMonth('EndOfWorkDate') - ExtractMonth('StartOfWorkDate'),
        month_difference=ExpressionWrapper(
            F('month_diff') + Case(
                When(day_diff__gt=1, then=1),
                default=0,
                output_field=IntegerField(),
            ),
            output_field=IntegerField()
        ),
        year_difference=ExtractYear('EndOfWorkDate') - ExtractYear('StartOfWorkDate'),
        total_cost=Round(ExpressionWrapper(
            F('EmpNetSalary') / 30.0 * F('day_difference') * Coalesce(F('EmpQty'), 1),
            output_field=FloatField()
        ), 2),
        salary_per_day=ExpressionWrapper(
            F('EmpNetSalary') / 30.0,
            output_field=FloatField()
        ),
        salary=Round(F('salary_per_day') * F('EmpQty') * F("day_difference"), 1),
        taxes=Round(ExpressionWrapper(
            Case(
                When(
                    LegDocumentType__DocumentTypeEN='Visa',
                    then=Case(
                        When(
                            day_difference__lte=182,
                            then=F('salary_per_day') * F('day_difference') * 0.6
                        ),
                        When(
                            day_difference__gt=182,
                            then=F('salary_per_day') * 182 * 0.6 + F('salary_per_day') * (
                                    F('day_difference') - 182) * 0.43
                        ),
                        default=Value(0),
                        output_field=FloatField()
                    )
                ),
                default=F('total_cost') * Case(
                    When(LegDocumentType__DocumentTypeEN='VKS', then=Value(tax_percent['VKS'])),
                    When(LegDocumentType__DocumentTypeEN='Local/ EEC', then=Value(tax_percent['Local/ EEC'])),
                    When(LegDocumentType__DocumentTypeEN='RVP/ VNJ', then=Value(tax_percent['RVP/ VNJ'])),
                    When(LegDocumentType__DocumentTypeEN='Patent', then=Value(tax_percent['Patent'])),
                    default=Value(0),
                    output_field=FloatField()
                ) / 100
            ),
            output_field=FloatField()
        ), 1)

    )
    return total_sum
