#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.exceptions import ValidationError

from geonode.base.models import HierarchicalKeyword, Region
from geonode.groups.models import GroupProfile

from igad_geonode.utils import searchurl


class HierarchicalKeywordMeta(models.Model):
    hkeyword = models.ForeignKey(HierarchicalKeyword, related_name='meta')
    icon = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=128, null=True)
    description = models.TextField(null=True)
    url = models.URLField(null=True)

    @classmethod
    def get_keywords(cls):
        return HierarchicalKeyword.objects.filter(meta__isnull=False)

    @staticmethod
    def get_hkeywords_roots():
        return HierarchicalKeyword.objects\
                                  .filter(meta__isnull=False,
                                          depth=1)

    def update(self, **attrs):
        for attr, val in attrs.items():
            setattr(self, attr, val)


def get_menu_order():
    return Menu.objects.all().count() + 1

def get_menu_item_order():
    return MenuItem.objects.all().count() + 1

class Menu(models.Model):

    class Meta:
        ordering = ['order']

    name = models.CharField(max_length=255, null=False, unique=False)
    order = models.IntegerField(null=False, default=get_menu_order,
                                help_text=_("Position of menu, ascending"))

    def __str__(self):
        return 'Menu: {}'.format(self.name)

    def get_items(self):
        return MenuItem.get_for_menu(self)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=255, null=False, unique=False)
    url = models.URLField(null=True, blank=True)
    order = models.IntegerField(null=False, default=get_menu_item_order,
                                help_text=_("Position of menu item, ascending"))

    group = models.ForeignKey(GroupProfile, null=True, blank=True)
    region = models.ForeignKey(Region, null=True, blank=True)

    class Meta:
        ordering = ['order']

    def clean(self):
        if not (self.url or self.group or self.region):
            msg = _("There should be one of: url, group or region, got none")
            raise ValidationError({'url': msg, 'group': msg, 'region': msg})
        if self.url and self.group:
            msg = _("There should be one of: url or group, got both")
            raise ValidationError({'url': msg, 'group': msg})

    @classmethod
    def get_for_menu(cls, menu):
        if isinstance(menu, (str, unicode,)):
            return cls.objects.filter(menu__name=menu)
        elif isinstance(menu, Menu):
            return cls.objects.filter(menu=menu)
        else:
            return cls.objects.filter(menu__id=menu)

    def get_url(self):
        # this may be extended in future, so url can be generated
        # dynamically, or for related object
        if self.group:
            return searchurl(group=self.group.group.id)
        elif self.region:
            return searchurl(regions__name__in=self.region.name)
        return self.url

    @classmethod
    def get_menus(cls):
        out = []
        for m in Menu.objects.all():
            out.append((m, cls.get_for_menu(m),))
        return out
