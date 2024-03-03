from .models import PermitDocCategory


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # current_permitdoccategory = PermitDocCategory.objects.get(current=True)

        # request.current_permitdoccategory = current_permitdoccategory

        response = self.get_response(request)

        return response

