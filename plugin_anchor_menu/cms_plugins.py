import logging

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

# Django CMS Tools
from plugin_anchor_menu import constants as plugin_anchor_menu_constants
from plugin_anchor_menu import app_settings
from plugin_anchor_menu.models import AnchorPluginModel, AnchorMenuPluginModel

log = logging.getLogger(__name__)


@plugin_pool.register_plugin
class AnchorPlugin(CMSPluginBase):
    """
    One anchor in a CMS page
    """
    name = _("Ссылка для меню")
    model = AnchorPluginModel
    render_template = app_settings.ANCHOR_MENU_TEMPLATE_ANCHOR
    prepopulated_fields = {"slug": ("title",)}


assert AnchorPlugin.__name__ == plugin_anchor_menu_constants.ANCHOR_PLUGIN_NAME


@plugin_pool.register_plugin
class AnchorMenuPlugin(CMSPluginBase):
    """
    Render a anchor menu
    """
    name = _("Меню из ссылок")
    model = AnchorMenuPluginModel
    render_template = app_settings.ANCHOR_MENU_TEMPLATE_MENU

    def render(self, context, instance, placeholder):
        anchors = AnchorPluginModel.objects.all().filter(
            placeholder__page=instance.page,
            # language=instance.language,
        )
        context.update({
            "menu_id": instance.menu_id,
            "scroll_mode": instance.scroll_mode,
            "anchors": anchors,
            "ANCHOR_MENU_JQUERY_URL": app_settings.ANCHOR_MENU_JQUERY_URL,
            "DEBUG": settings.DEBUG,
        })
        return super().render(context, instance, placeholder)


assert AnchorMenuPlugin.__name__ == plugin_anchor_menu_constants.DROP_DOWN_ANCHOR_MENU_PLUGIN_NAME
