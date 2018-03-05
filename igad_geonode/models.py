#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from django.utils.translation import ugettext_lazy as _
from django.db import models

from geonode.base.models import HierarchicalKeyword
# Create your models here.


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


class MenuLink(models.Model):
    MENU_EXT_LINK = 'external_link'

    MENUS = ((MENU_EXT_LINK, _("External Links"),),
             )
    menu = models.CharField(max_length=32,
                            choices=MENUS,
                            null=False,
                            default=MENU_EXT_LINK,
                            db_index=True)
    title = models.CharField(max_length=255, null=False, unique=True)
    url = models.URLField(null=False, unique=True)

    @classmethod
    def get_for_menu(cls, menu):
        return cls.objects.filter(menu=menu)
