from rest_framework import permissions
"""first defining the boundaries of the admin"""
class isAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        """Basic authorisation for authorising the users"""
        return request.user and request.user_is_authenticated

"""Defining the admin authorisations"""
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return(
            request.user and
            request.user.is_authenticated and
            request.user.is_authenticated.role=="admin"
        )

"""Role for admin or staff; for those who are working in the same org and want to view the billing and other aspects"""
class IsAdminOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return(
            request.user and
            request.user.is_authenticated and
            request.user.is_authenticated.role=="admin" or request.user.is_authenticated.role=="staff"
        )

"""Same organization for accessing the other users data like bils/invoices and etc"""
class IsSameOrganization(permissions.BasePermission):
    def has_permission(self, request, view,obj):
        return(hasattr(obj,"organization") and
               request.user.organization==obj.organization)
"""for admins and read-only for others"""
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """"read only for others like the bills and invoices and write-only for admins"""
        if(request.method in permissions.SAFE_METHODS):
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated.role=="admin"

class IsAdminOrStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #everyone can see
        if request.method in ["GET","HEAD","OPTIONS"]:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.role=="admin":
            return True
        if request.user.role=="staff" and request.method in ["POST","PUT","PATCH"]:
            return True
        return False



