from django.shortcuts import render, HttpResponse, redirect

from .form import *
from .models import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def homeview(request):
    if request.method == "POST":
        category = request.POST.get("select_category")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        current_location = request.POST.get("current_location")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        highest_qualification = request.POST.get("highest_qualification")
        experience = request.POST.get("experience")
        current_ctc = request.POST.get("currnet_ctc")
        expected_ctc = request.POST.get("expected_ctc")
        working_status = request.POST.get("working_status")
        notice_period = request.POST.get("notice_period")
        company_name = request.POST.get("company_name")
        follow_status = request.POST.get("follow_status")
        selection_status = request.POST.get("selection_status")
        date = request.POST.get("date")
        checkbox_values = request.POST.get("checkbox_values")
        key_skill = request.POST.getlist("key_skill")
        skill = request.POST.getlist("skill")
        my_file = request.FILES.get("my_file")  # Use FILES for file uploads
        remark = request.POST.get("remark")
        print(my_file, " my_file-------------")

        # Create a new Resume instance with the form data
        resume = Resume(
            select_category=category,
            name=name,
            mobile=mobile,
            current_location=current_location,
            email=email,
            gender=gender,
            highest_qualification=highest_qualification,
            experience=experience,
            currnet_ctc=current_ctc,
            expected_ctc=expected_ctc,
            working_status=working_status,
            notice_period=notice_period,
            company_name=company_name,
            follow_status=follow_status,
            selection_status=selection_status,
            date=date,
            checkbox_values=checkbox_values,
            key_skill=key_skill,
            skill=skill,
            my_file=my_file,
            remark=remark,
        )
        resume.save()
        return redirect("/")
    return render(request, "myapp/home.html")


def update_resume(request, id):
    stu_det = Resume.objects.filter(pk=id).values()
    print(stu_det)
    if request.method == "POST":
        category = request.POST.get("select_category")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        current_location = request.POST.get("current_location")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        highest_qualification = request.POST.get("highest_qualification")
        experience = request.POST.get("experience")
        current_ctc = request.POST.get("currnet_ctc")
        expected_ctc = request.POST.get("expected_ctc")
        working_status = request.POST.get("working_status")
        notice_period = request.POST.get("notice_period")
        company_name = request.POST.get("company_name")
        follow_status = request.POST.get("follow_status")
        selection_status = request.POST.get("selection_status")
        date = request.POST.get("date")
        checkbox_values = request.POST.get("checkbox_values")
        key_skill = request.POST.getlist("key_skill")
        skill = request.POST.getlist("skill")
        my_file = request.FILES.get("my_file")  # Use FILES for file uploads
        remark = request.POST.get("remark")
        print(skill, "skill-----------")

        # Create a new Resume instance with the form data
        resume = Resume(
            select_category=category,
            name=name,
            mobile=mobile,
            current_location=current_location,
            email=email,
            gender=gender,
            highest_qualification=highest_qualification,
            experience=experience,
            currnet_ctc=current_ctc,
            expected_ctc=expected_ctc,
            working_status=working_status,
            notice_period=notice_period,
            company_name=company_name,
            follow_status=follow_status,
            selection_status=selection_status,
            date=date,
            checkbox_values=checkbox_values,
            key_skill=key_skill,
            skill=skill,
            my_file=my_file,
            remark=remark,
        )
        resume.save()
        return redirect("/")

    return render(
        request,
        "myapp/update.html",
        {
            "stu_det": stu_det,
        },
    )


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, "myapp/candidate.html", {"candidate": candidate})


# class UpdateView(View):
#     template_name = "myapp/update.html"

#     def get(self, request, pk):
#         candidate = Resume.objects.get(pk=pk)
#         form = ResumeForm(instance=candidate)
#         return render(
#             request, self.template_name, {"form": form, "candidate": candidate}
#         )

#     def post(self, request, pk):
#         candidate = Resume.objects.get(pk=pk)
#         form = ResumeForm(request.POST, instance=candidate)

#         if form.is_valid():
#             form.save()
#             return redirect(
#                 "/",
#             )  # Replace 'your_redirect_url' with the actual URL to redirect to

#         return render(
#             request, self.template_name, {"form": form, "candidate": candidate}
#         )


class AllList(View):
    def get(self, request, *args, **kwargs):
        candidates = Resume.objects.all()
        return render(request, "myapp/list.html", {"candidates": candidates})


def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get("toemail")
        content = request.POST.get("content")
        print(to, content)
        send_mail(
            "Testing",
            # msg
            content,
            # from email
            settings.EMAIL_HOST_USER,
            # rec list
            [to],
        )
        return render(request, "email.html", {"title": "send an email"})
    else:
        return render(request, "email.html", {"title": "send an email"})


class SendEmail(View):
    def get(self, request, pk):
        detail = Resume.objects.get(pk=pk)
        to = detail.email
        context = {
            "detail": detail,
            "name": detail.name,
        }
        html_message = render_to_string("myapp/interview.html", context)
        plain_message = strip_tags(html_message)

        # content = "hello harsh"
        send_mail(
            "Interview scheduled",
            plain_message,
            settings.EMAIL_HOST_USER,
            [to],
            html_message=html_message,
        )
        return redirect("/")
