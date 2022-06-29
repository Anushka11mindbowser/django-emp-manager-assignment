from rest_framework import permissions
class Manager(permissions.BasePermission):
    edit_methods=("POST", "GET", "PUT", "DELETE")
    def has_permission(self, request, view):
        if request.user.role == "manager":
            return True