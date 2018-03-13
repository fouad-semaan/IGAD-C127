#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from django.http import Http404
from django.views.generic import DetailView, ListView

from geonode.base.models import HierarchicalKeyword

class HierarchicalKeywordMetaView(DetailView):
    model = HierarchicalKeyword
    template_name = 'igad/hierarchical_keyword_meta.html'

    def get_object(self):
        obj = super(HierarchicalKeywordMetaView, self).get_object()
        if not obj.meta:
            raise Http404("Object not found")
        return obj

    def get_context_data(self, *args, **kwargs):
        ctx = super(HierarchicalKeywordMetaView, self).get_context_data(*args, **kwargs)
        ctx['all_hkeywords'] = HierarchicalKeyword.objects\
                                                  .filter(meta__isnull=False,
                                                          depth=1)
        ctx['hkeywords_meta_children'] = self.get_hkeywords_meta_children()
        ctx['test'] = [{'name':1}]
        return ctx

    def get_hkeywords_meta_children(self):
        obj = self.get_object()
        children = obj.get_children()
        _children_meta = [child.meta for child in children]
        children_meta = sorted(_children_meta, key=lambda k: k.order)
        return children_meta


class HierarchicalKeywordMetaList(ListView):
    model = HierarchicalKeyword
    template_name = 'igad/hierarchical_keyword_list.html'
    ordering = ['order']
    
    queryset = HierarchicalKeyword.objects.filter(meta__isnull=False,
                                                  depth=1).order_by('order')


hkeyword_view = HierarchicalKeywordMetaView.as_view()
hkeyword_index = HierarchicalKeywordMetaList.as_view()
