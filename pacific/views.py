from pyramid.view import view_config


@view_config(route_name='home', renderer='/index.plim')
def home(request):
    return {'project': 'Pacific'}
