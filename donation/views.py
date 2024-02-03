from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from sslcommerz_lib import SSLCOMMERZ


def index(request):
    if request.method == "POST":
        config = {
            "store_id": settings.SSLCOMMERZ_STORE_ID,
            "store_pass": settings.SSLCOMMERZ_PASSWORD,
            "issandbox": settings.SSLCOMMERZ_IS_SANDBOX,
        }
        sslcommerz = SSLCOMMERZ(config)

        post_body = {}
        post_body["total_amount"] = request.POST.get('amount')
        post_body["currency"] = "BDT"
        post_body["tran_id"] = "REF123"
        post_body["success_url"] = request.build_absolute_uri(
            reverse('success_donation'))
        post_body["fail_url"] = request.build_absolute_uri(
            reverse('fail_donation'))
        post_body["cancel_url"] = request.build_absolute_uri(
            reverse('cancel_donation'))
        post_body["emi_option"] = 0
        post_body["cus_name"] = "test"
        post_body["cus_email"] = "test@test.com"
        post_body["cus_phone"] = "01700000000"
        post_body["cus_add1"] = "customer address"
        post_body["cus_city"] = "Dhaka"
        post_body["cus_country"] = "Bangladesh"
        post_body["shipping_method"] = "NO"
        post_body["multi_card_name"] = ""
        post_body["num_of_item"] = 1
        post_body["product_name"] = "Test"
        post_body["product_category"] = "Test Category"
        post_body["product_profile"] = "general"

        response = sslcommerz.createSession(post_body)  # API response

        return redirect(response["GatewayPageURL"], code=303)
    return render(request, "donation/index.html")


@csrf_exempt
def success_donation(request):
    return render(request, "donation/success.html")


@csrf_exempt
def cancel_donation(request):
    return render(request, "donation/cancel.html")


@csrf_exempt
def fail_donation(request):
    return render(request, "donation/failed.html")
