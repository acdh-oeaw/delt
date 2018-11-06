from django.conf import settings


def access_for_shib_and_loggedin(self):
    try:
        shib = self.request.META['HTTP_EPPN']
    except KeyError:
        shib = '(null)'
    if shib != '(null)' or self.request.user.is_authenticated:
        return True
    else:
        return False
