from apps.corecode.models import Gen_DT_BudgetDetails
from django.db.models import F, ExpressionWrapper, DurationField, Sum, fields
from django.db.models.functions import ExtractMonth
from django.db.models.functions import Cast, ExtractDay, TruncDate
from django.db.models import Case, When, IntegerField


class Calculation:
    def __init__(self, BudgetDetails_ID):
        self.id = BudgetDetails_ID
        self.data = self.salary()
        self.index = 0

    def salary(self):
        total_sum = Gen_DT_BudgetDetails.objects.filter(Budget_ID=self.id).annotate(
            month_diff=ExtractMonth('EndOfWorkDate') - ExtractMonth('StartOfWorkDate'),
            day_diff=ExtractDay('EndOfWorkDate') - ExtractDay('StartOfWorkDate')
        ).annotate(
            adjusted_month_diff=ExpressionWrapper(
                F('month_diff') + Case(
                    When(day_diff__gt=0, then=1),
                    default=0,
                    output_field=IntegerField(),
                ),
                output_field=IntegerField()
            )
        ).annotate(
            product=F('adjusted_month_diff') * F('EmpQty') * F('EmpNetSalary')
        )
        # .aggregate(
        #     total=Sum('product')
        # )['total']
        # for i in total_sum:
        #     print(i.product)
        return total_sum

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
