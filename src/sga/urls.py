'''
@organization: Solvo
@license: GNU General Public License v3.0
@date: Created on 13 sept. 2018
@author: Guillermo Castro Sánchez
@email: guillermoestebancs@gmail.com
'''

# Import functions of another modules
from sga.views import index_sga, label_creator, label_information,label_template
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from ajax_select import urls as ajax_select_urls
from . import views


# SGA
app_name = 'sga'

# Views "The Hard Way"
urlpatterns = [
    # sga/index_sga/
    url(r'index_sga', index_sga, name='index_sga'),
    # sga/label_creator/
    url(r'label_creator', label_creator, name='label_creator'),
    # Django Ajax Selects
    url(r'^ajax_select/', include(ajax_select_urls)),
    # sga/auto_complete_sustance/
    url(r'^search_autocomplete_sustance/', views.search_autocomplete_sustance, name='search_autocomplete_sustance'),
    # sga/label_information/
    url(r'label_information', label_information, name='label_information'),
    # sga/label_template/
    url(r'label_template', label_template, name='label_template'),
]
