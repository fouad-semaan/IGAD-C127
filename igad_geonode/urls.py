# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
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

from django.conf.urls import url, include
from django.views.generic import TemplateView

from geonode.urls import urlpatterns
from igad_geonode import views

hkeywords_patterns = [
                #url(r'^$', views.hkeyword_index, name='hkeyword_index'),
                url(r'^area/(?P<slug>[a-zA-Z0-9_.-]+)/',
                    views.hkeyword_view,
                    name='hkeyword_view'),
                url(r'^list/(?P<slug>[a-zA-Z0-9_.-]+)/',
                    views.hkeyword_contents_view,
                    name='hkeyword_contents_view'),
                url(r'^group/(?P<pk>[0-9]+)/',
                    views.groupcontents_view,
                    name='groupcontents_view'),
                ]

urlpatterns = [
    url(r'contents/', include(hkeywords_patterns)),
    url(r'^/?$',
        TemplateView.as_view(template_name='site_index.html'),
        name='home'),
] + urlpatterns
