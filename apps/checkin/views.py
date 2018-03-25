from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from madras import settings
from apps.registration.models import Applicant
from .models import CheckInGroup, CheckInEvent
import qrcode
import os.path
from django.utils import timezone


static_path = "static/checkin/qr_codes/"


def get_qr_code(request):
    if request.GET:
        try:
            email = request.POST["email"]
        except KeyError:
            return error_response("Must include email.",
                                  "You must include the user's email in the request body.",
                                  400)
        try:
            applicant = Applicant.objects.get(email=email)
        except Applicant.DoesNotExist:
            return error_response("User does not exist.",
                                  "A user with that email address was not found in the database.",
                                  404)
        # TODO: check that applicant was actually admitted
        return success_data_jsonify({ "qr_image_path": "/" + return_qr(applicant.email)})
    else:
        return error_response("Invalid method.", "Please use a get request.", 405)


def get_qr_codes(request):
    # TODO: will need to be authenticated to admins
    applicants = Applicant.objects.all()
    # TODO: filter to only include admitted applicants
    files = []
    for applicant in applicants:
        files.append(return_qr(applicant.email))
    return success_data_jsonify({"qr_image_paths": files})


def return_qr(email):
    relative_path = static_path + email.replace("@", "").replace(".", "") + ".png"
    full_path = os.path.join(settings.PROJECT_ROOT, relative_path)
    if not os.path.exists(full_path):
        with open(full_path, "wb") as f:
            qrcode.make(email).save(f, format="PNG")
    return relative_path


@csrf_exempt
def check_in(request):
    if request.POST:
        try:
            email = request.POST["email"]
        except KeyError:
            return error_response("Must include email.",
                                  "You must include the user's email in the request body.",
                                  400)
        try:
            applicant = Applicant.objects.get(email=email)
        except Applicant.DoesNotExist:
            return error_response("User does not exist.",
                                  "A user with that email address was not found in the database.",
                                  404)
        group, _ = CheckInGroup.objects.get_or_create(applicant=applicant)
        if group.checked_in:
            return error_response("User already checked in.",
                                  "The user specified is already checked in.",
                                  409)
        event = CheckInEvent(check_in_group=group, check_in=True, time=timezone.now())
        group.checked_in = True
        event.save()
        group.save()
        return success_data_jsonify()
    else:
        return error_response("Invalid method.", "Please use a post request.", 405)
    # TODO: will need to be authenticated to admins


@csrf_exempt
def check_out(request):
    if request.POST:
        try:
            email = request.POST["email"]
        except KeyError:
            return error_response("Must include email.",
                                  "You must include the user's email in the request body.",
                                  400)
        try:
            applicant = Applicant.objects.get(email=email)
        except Applicant.DoesNotExist:
            return error_response("User does not exist.",
                                  "A user with that email address was not found in the database.",
                                  404)
        group, _ = CheckInGroup.objects.get_or_create(applicant=applicant)
        if not group.checked_in:
            return error_response("User not checked in.",
                                  "The user must be checked in to be checked out.",
                                  409)
        event = CheckInEvent(check_in_group=group, check_in=False, time=timezone.now())
        group.checked_in = False
        event.save()
        group.save()
        return success_data_jsonify()
    else:
        return error_response("Invalid method.", "Please use a post request.", 405)
    # TODO: will need to be authenticated to admins


# TODO: move the below functions to utils somewhere so everyone can use them
def success_data_jsonify(obj={}, code=200):
    response = JsonResponse({
        'success' : True,
        'data' : obj
    })

    response.status_code = code

    return response


def error_response(title, message, code):

    error_dictionary = {'message' : message,
                        'title' : title}

    response = JsonResponse({'success' : False,
                        'error' : error_dictionary
    })
    response.status_code = code

    return response