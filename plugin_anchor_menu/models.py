import logging

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from plugin_anchor_menu import app_settings

log = logging.getLogger(__name__)


class AnchorPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=254)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255)

    def validate_field_unique_on_page(self, error_dict, field_name):
        assert hasattr(self, field_name)
        unique_checks = [
            (AnchorPluginModel, ("placeholder", "language", field_name)),
        ]
        errors = self._perform_unique_checks(unique_checks)
        if errors:
            value = getattr(self, field_name)
            error_dict[field_name] = _(
                "{field_name} '%s' already exists on current page" % value
            ).format(
                field_name=field_name
            )

    def validate_unique_on_page(self):
        error_dict = {}
        self.validate_field_unique_on_page(error_dict, field_name="title")
        self.validate_field_unique_on_page(error_dict, field_name="slug")
        if error_dict:
            raise ValidationError(error_dict)

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)
        self.validate_unique_on_page()

    def save(self, **kwargs):
        self.validate_unique_on_page()
        super().save(**kwargs)

    def __str__(self):
        return self.title


class AnchorMenuPluginModel(CMSPlugin):
    menu_id = models.SlugField(_("The internal menu ID"), default=app_settings.ANCHOR_MENU_DEFAULT_ID, max_length=254)
    top_offset_minus = models.IntegerField(verbose_name='Поправка на высоту меню', default='80')

    TYPE_HREF = "h"
    TYPE_SCROLL = "s"
    TYPE_CHOICES = (
        (TYPE_HREF, _("Add '#anchor' to browser addess.")),
        (TYPE_SCROLL, _("Don't add '#anchor' to browser addess.")),
    )

    link_type = models.CharField(_("Link type"),
                                 max_length=1,
                                 choices=TYPE_CHOICES,
                                 default=app_settings.ANCHOR_MENU_DEFAULT_TYPE,
                                 )

    @property
    def scroll_mode(self):
        return self.link_type == self.TYPE_SCROLL
