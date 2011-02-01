# -*- encoding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import WikiPostPlugin
from django.utils.translation import ugettext as _

class CMSWikiPostPlugin(CMSPluginBase):
    model = WikiPostPlugin
    name = _("Wiki")
    render_template = "wiki/post.html"

    def render(self, context, instance, placeholder):
        context.update({'post':instance, 'object':instance, 'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSWikiPostPlugin)
