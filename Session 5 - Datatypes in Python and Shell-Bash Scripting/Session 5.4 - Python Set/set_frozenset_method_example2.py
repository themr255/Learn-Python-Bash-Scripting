"""
Method - frozenset()

Description: Immutable version of a Python set object. While elements of a set can be modified at any time,
            elements of the frozen set remain the same after creation.
            Once you create a frozenset, you cannot modify it by adding or removing elements.
"""

# Define user roles and their permissions using frozensets
admin_permissions = frozenset(["create", "read", "update", "delete"])
editor_permissions = frozenset(["read", "update"])
viewer_permissions = frozenset(["read"])

# Store user roles and their permissions
user_roles = {
    "admin": admin_permissions,
    "editor": editor_permissions,
    "viewer": viewer_permissions,
}

for user in user_roles:
    print("User Type: {}".format(user))
    print("User has permission to create: {}".format(user_roles[user]))

# Attempt to add a new destination to the frozenset (this will raise an error)
try:
    viewer_permissions.add("create")
except AttributeError:
    print("\nCannot add 'create' permission to a viewer_permissions frozenset.")

"""
                        Output - 
---------------------------------------------------------------
User Type: admin
User has permission to create: frozenset({'delete', 'read', 'create', 'update'})
User Type: editor
User has permission to create: frozenset({'read', 'update'})
User Type: viewer
User has permission to create: frozenset({'read'})

Cannot add 'create' permission to a viewer_permissions frozenset.

"""