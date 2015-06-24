from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trabalhoCosme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'estacionamentoCosme.views.index'),
   	url(r'^admin/', include(admin.site.urls)),
    #visualizar
	    url(r'^cliente/$', 'estacionamentoCosme.views.cliente', name="cliente"),
	    url(r'^vaga/$', 'estacionamentoCosme.views.vaga', name="vaga"),
	    url(r'^carro/$', 'estacionamentoCosme.views.carro', name="carro"),
	    url(r'^alugar/', 'estacionamentoCosme.views.alugar', name="alugar"),
    # cadastra
        url(r'^models/Cliente/$', 'estacionamentoCosme.views.cadastraCliente', name='cadastra_Cliente'),
        url(r'^models/Carro/$', 'estacionamentoCosme.views.cadastraCarro', name='cadastra_Carro'),
        url(r'^models/Vaga/$', 'estacionamentoCosme.views.cadastraVaga', name='cadastra_Vaga'),
        url(r'^models/Alugar/$', 'estacionamentoCosme.views.cadastraAlugar', name='cadastra_Alugar'),
    # Edita
        url(r'^cliente/editar/(.*)/$', 'estacionamentoCosme.views.EditaCliente',name='edita_cliente'),
        url(r'^carro/editar/(.*)/$', 'estacionamentoCosme.views.EditaCarro',name='edita_carro'),
        url(r'^vaga/editar/(.*)/$', 'estacionamentoCosme.views.EditaVaga',name='edita_vaga'),
        url(r'^alugar/editar/(.*)/$', 'estacionamentoCosme.views.EditaAlugar',name='edita_Alugar'),
    )

