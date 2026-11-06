"""Telamon: framework-agnostic admin panel for SQLAlchemy, Tortoise ORM, MongoDB and Beanie."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

from .core import (
    Action,
    AdminError,
    AdminRequest,
    AdminResponse,
    AdminSite,
    AuthProvider,
    Backend,
    FieldType,
    FilterGroup,
    ListQuery,
    ModelAdmin,
    ModelSchema,
    NotFound,
    PermissionDenied,
    Repository,
    SessionAuth,
    SimpleAuth,
    User,
    ValidationError,
    action,
    hash_password,
)

try:
    __version__ = _pkg_version("telamon")
except PackageNotFoundError:  # running from a source checkout without installation
    __version__ = "0.0.0"

__all__ = [
    "Action",
    "AdminError",
    "AdminRequest",
    "AdminResponse",
    "AdminSite",
    "AuthProvider",
    "Backend",
    "FieldType",
    "FilterGroup",
    "ListQuery",
    "ModelAdmin",
    "ModelSchema",
    "NotFound",
    "PermissionDenied",
    "Repository",
    "SessionAuth",
    "SimpleAuth",
    "User",
    "ValidationError",
    "action",
    "hash_password",
]
