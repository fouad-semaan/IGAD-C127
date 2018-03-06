#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from django.contrib import admin

from igad_geonode.models import HierarchicalKeywordMeta, Menu, MenuItem


@admin.register(HierarchicalKeywordMeta)
class HierarchicalKeywordMetaAdmin(admin.ModelAdmin):
    list_display = ('title', 'hkeyword', 'icon', 'url',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'order',)


@admin.register(MenuItem)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'url',)
