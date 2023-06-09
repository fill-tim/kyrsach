from django.urls import path

from .views import home, info, add_file, guide, create_file, data_output, convert_pdf

urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info'),
    path('add_file/', add_file, name='form_add_file'),
    path('output/', data_output, name='data_output'),
    path('guide_page/', guide, name='guide_page'),
    path('docx/', create_file, name='docx'),
    # path('pdf/', convert_pdf, name='pdf'),
]
