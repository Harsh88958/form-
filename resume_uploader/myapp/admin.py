from django.contrib import admin

from .models import Resume


# class ResumeAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "mobile",
#         "current_location",
#         "email",
#         "gender",
#         "highest_qualification",
#         "experience",
#         "currnet_ctc",
#         "expected_ctc",
#         "working_status",
#         "notice_period",
#         "company_name",
#         "checkbox_values",
#         "key_skill",
#         "follow_status",
#         "selection_status",
#         "date",
#         "my_file",
#     )
#     list_filter = (
#         "working_status",
#         "follow_status",
#         "selection_status",
#     )
#     search_fields = ("name", "email", "mobile", "company_name")
#     ordering = ("-date",)


admin.site.register(Resume)
