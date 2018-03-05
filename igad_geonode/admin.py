#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from django.contrib import admin

from igad_geonode.models import HierarchicalKeywordMeta, MenuLink


@admin.register(HierarchicalKeywordMeta)
class HierarchicalKeywordMetaAdmin(admin.ModelAdmin):
    list_display = ('title', 'hkeyword', 'icon', 'url',)
    #fields = ('hkeyword', 'hkeyword__name', 'title', 'icon', 'description', 'url',)
    #raw_id_fields = ('hkeyword',)


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('menu', 'url', 'title',)
