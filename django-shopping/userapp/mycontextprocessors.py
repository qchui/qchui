
def getUserInfo(request):
    return {'userSession':request.session.get('user','')}
