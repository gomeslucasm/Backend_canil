from rest_framework.permissions import BasePermission

class IsVeterinary(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_veterinary

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_staff

class IsVolunteerUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_volunteer

class IsUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.user.is_authenticated:
            if user.is_volunteer:
                permission = True
            elif user.is_veterinary:
                permission = True
            elif user.is_volunteer:
                permission = True
            else:
                permission = False
            return user.is_authenticated and permission
        else:
            return False