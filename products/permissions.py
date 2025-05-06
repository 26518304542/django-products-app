from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Admin kullanıcı her şeyi yapabilir.
    Diğer kullanıcılar sadece GET (read) yapabilir.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsStaffOrReadOnly(BasePermission):
    """
    Custom permission to only allow staff members to edit products.
    """
    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Allow write access only to staff members
        return request.user and request.user.is_staff