# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-02-14 22:11'

import xadmin
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from xadmin.layout import Fieldset,Main,Side,Row
from django.utils.translation import ugettext as _

from .models import *


# xadmin全局配置
class BaseSetting(object):
    enable_themes=True;
    use_bootswatch=True;


class GlobalSettings(object):
    site_title="IMOOC后台管理";
    site_footer="IMOOC"
    menu_style='accordion'


class SuperUserAdmin(UserAdmin):
    """
    配置自定义超级用户
    """
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class AccountAdmin(object):
    pass


xadmin.site.register(Account,AccountAdmin);
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)