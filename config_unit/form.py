from django import forms
from captcha.fields import CaptchaField

from appcenter.form import *

all_tables_form = {
    "supermanager": mc_supermanager_form,
    "permkwkwissions": mc_permkwkwissions_form,
    "logs": mc_logs_form,
    "comments": mc_comments_form,
    "reckwkwordattachments": mc_reckwkwordattachments_form,
    "reckwkwords": mc_reckwkwords_form,
    "reckwkwordcategkwkwories": mc_reckwkwordcategkwkwories_form,
    "roles": mc_roles_form,
    "users": mc_users_form,
}
