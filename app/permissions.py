# --*-- coding:utf-8 --*--

from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):

        if request.method == 'POST':
            return True
        elif request.method == 'GET':
            return True

        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)