from django.shortcuts import render,redirect


def auth_middleware(get_request):

    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if not request.session.get("customer"):
            return redirect(f'login.html?return_url={returnUrl}')

        response = get_request(request)
        return response
    return middleware