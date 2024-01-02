from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from app1.models import SaleEnquiry


def home(request):
    return render(request, "app1/home.html")


def create_data(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        guardian_type = request.POST.get("guardian_type")
        guardian_name = request.POST.get("guardian_name", "")
        dob = request.POST.get("dob")
        mobile_no = request.POST.get("mobile_no")
        additional_mobile_no = request.POST.get("additional_mobile_no", "")
        address = request.POST.get("address")
        state = request.POST.get("state")
        district = request.POST.get("district")
        city = request.POST.get("city")
        next_follow_up_date = request.POST.get("next_follow_up_date")
        notes = request.POST.get("notes")

        # if SaleEnquiry.objects.filter(mobile_no=mobile_no).exists() or SaleEnquiry.objects.filter(additional_mobile_no=additional_mobile_no).exists():
        #     return JsonResponse({'status': 'error', 'message': 'Duplication error'})

        sale_enquiry = SaleEnquiry(
            client_name=client_name,
            guardian_type=guardian_type,
            guardian_name=guardian_name,
            dob=dob,
            mobile_no=mobile_no,
            additional_mobile_no=additional_mobile_no,
            address=address,
            state=state,
            district=district,
            city=city,
            next_follow_up_date=next_follow_up_date,
            notes=notes,
        )
        if sale_enquiry.isExists():
            return JsonResponse(
                {"status": "error", "message": "Mobile Number  Already Registered "}
            )
        else:
            sale_enquiry.register()

        return redirect("read")

    return render(request, "app1/create.html")


# Create your views here.
def read(request):
    pi = SaleEnquiry.objects.all()
    return render(request, "app1/read.html", {"pi": pi})
