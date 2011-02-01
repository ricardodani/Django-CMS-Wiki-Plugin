# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.db import models
#import gettext
from cms.models import CMSPlugin


class WikiPostPlugin(CMSPlugin):

    body = models.TextField(verbose_name=_("Corpo"))

    def __unicode__(self):
        #return self.title
        return u"#%d - %s"  % (self.id, self.body[:100] + "...")

    class Meta:
        verbose_name = _("Postagem Wiki")
        verbose_name_plural = _("Postagens Wiki")
