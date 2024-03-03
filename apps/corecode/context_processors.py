from django.db.models import F

from .models import SiteConfig
from apps.employees.models import Employee


def site_defaults(request):
    # current_session = AcademicSession.objects.get(current=True)
    # current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    active_employee_count = Employee.objects.filter(current_status='active').count() # Get all employees with status 'active'
    contexts = {
        "active_employee_count": active_employee_count,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts