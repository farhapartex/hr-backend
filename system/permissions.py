def _check_has_permission(request, model, view):
    perm_str = ""
    if view.action == "list":
        perm_str = model._meta.app_label + ".view_" + model.__name__.lower()
    elif view.action == "create":
        perm_str = model._meta.app_label + ".add_" + model.__name__.lower()
    elif view.action == "update":
        perm_str = model._meta.app_label + ".change_" + model.__name__.lower()
    elif view.action == "retrieve":
        perm_str = model._meta.app_label + ".view_" + model.__name__.lower()
    elif view.action == "destroy":
        perm_str = model._meta.app_label + ".delete_" + model.__name__.lower()
        
    return request.user.has_perm(perm_str)