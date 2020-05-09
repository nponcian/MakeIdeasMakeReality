from rest_framework import permissions

class DefaultServicePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        allowedMethodsForServices = ["GET", "POST"]
        return request.method in allowedMethodsForServices

    def has_object_permission(self, request, view, obj):
        return False
