#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django import template

from igad_geonode.models import HierarchicalKeywordMeta, MenuItem, Menu


def sidebar_menus():
    return MenuItem.get_menus(Menu.MENU_SIDEBAR)


def top_menus():
    return MenuItem.get_menus(Menu.MENU_TOP) 


def menu_roots(request):
    ctx = {}
    ctx['menu_roots'] = HierarchicalKeywordMeta.get_hkeywords_roots()
    ctx['top_menus'] = top_menus
    ctx['sidebar_menus'] = sidebar_menus
    return ctx
