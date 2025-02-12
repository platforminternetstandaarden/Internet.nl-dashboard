# SPDX-License-Identifier: Apache-2.0
import json
import logging

from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from dashboard.internet_nl_dashboard.models import Account, DashboardUser

log = logging.getLogger(__package__)
LOGIN_URL = "/account/login/"

"""
Todo: csrf via API calls...
    https://docs.djangoproject.com/en/dev/ref/csrf/#csrf-ajax
    Is handled and validated via middleware, so we don't need to concern ourselves with it here.
"""


def logout_view(request) -> HttpResponse:
    logout(request)
    return redirect("/")


def get_account(request) -> Account:
    # todo: what about the exceptions that happen when there is no account? Currently exceptions, it should not happen.
    # log.debug(request)
    # log.debug(request.user)
    return DashboardUser.objects.all().filter(user=request.user).get().account


def get_dashboarduser(request) -> DashboardUser:
    # todo: what about the exceptions that happen when there is no account? Currently exceptions, it should not happen.
    return DashboardUser.objects.all().filter(user=request.user).get()


def empty_response() -> JsonResponse:
    return JsonResponse({})


def error_response(message: str) -> JsonResponse:
    return JsonResponse({"status": "error", "message": message})


def get_json_body(request):

    try:
        user_input = json.loads(request.body)
    except json.JSONDecodeError:
        user_input = {}

    return user_input
