from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import PropertyForm
from .models import Property
from .serializers import PropertiesListSerializer

@api_view(['GET'])
@authentication_classes([])  # Aquí puedes agregar autenticación si es necesario
@permission_classes([])  # Aquí puedes agregar permisos si es necesario
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)

    return JsonResponse({
        'data': serializer.data
    })

@api_view(['POST', 'FILES'])
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)

    if form.is_valid():
        property = form.save(commit=False)
        property.landlord = request.user
        property.save()

        return JsonResponse({'succes': True})
    else:
        print('error', form.erros, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)