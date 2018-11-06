from django.conf import settings


def installed_apps(request):
    return {'APPS': settings.INSTALLED_APPS}


def is_dev_version(request):
    try:
        return {'DEV_VERSION': settings.DEV_VERSION}
    except AttributeError:
        return {}


def get_db_name(request):
    try:
        db_name = settings.DATABASES['default']['NAME']
        return {'DB_NAME': db_name}
    except Exception as e:
        return {}


def check_shb(request):
    try:
        shib = request.META['HTTP_EPPN']
    except KeyError:
        shib = '(null)'
    if shib != '(null)':
        return {'SHIB': shib}
    else:
        return {'SHIB': ''}
