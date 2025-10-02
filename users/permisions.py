from rest_framework import permissions

class RolePermission(permissions.BasePermission):
    """
    Role-based access control for API ViewSets.
    """

    ROLE_PERMISSIONS = {
        # Students API
        "students": {
            "list": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "retrieve": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "create": ["ADMIN", "MANAGER", "CLERK"],
            "update": ["ADMIN", "MANAGER", "CLERK"],
            "partial_update": ["ADMIN", "MANAGER", "CLERK"],
            "destroy": ["ADMIN", "MANAGER"],
        },
        # Classes API
        "classes": {
            "list": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "retrieve": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "create": ["ADMIN", "MANAGER", "CLERK"],
            "update": ["ADMIN", "MANAGER"],
            "partial_update": ["ADMIN", "MANAGER"],
            "destroy": ["ADMIN"],
        },
        # Courses API
        "courses": {
            "list": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "retrieve": ["ADMIN", "MANAGER", "LECTURER", "CLERK"],
            "create": ["ADMIN", "MANAGER"],
            "update": ["ADMIN", "MANAGER"],
            "partial_update": ["ADMIN", "MANAGER"],
            "destroy": ["ADMIN"],
        },
        # Instructors API
        "instructors": {
            "list": ["ADMIN", "MANAGER"],
            "retrieve": ["ADMIN", "MANAGER"],
            "create": ["ADMIN"],
            "update": ["ADMIN"],
            "partial_update": ["ADMIN"],
            "destroy": ["ADMIN"],
        },
        # Results API
        "results": {
            "list": ["ADMIN", "MANAGER", "LECTURER"],
            "retrieve": ["ADMIN", "MANAGER", "LECTURER"],
            "create": ["ADMIN", "MANAGER", "CLERK"],
            "update": ["ADMIN", "MANAGER", "CLERK"],
            "partial_update": ["ADMIN", "MANAGER", "CLERK"],
            "destroy": ["ADMIN", "MANAGER"],
        },
    }

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        app_name = view.basename  # e.g., "students", "results"
        action = view.action       # e.g., "list", "create"
        user_role = getattr(request.user, "role", None)

        allowed_roles = self.ROLE_PERMISSIONS.get(app_name, {}).get(action, [])

        return user_role in allowed_roles
