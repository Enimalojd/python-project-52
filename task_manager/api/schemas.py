from typing import Any, Generic, TypeVar
from ninja import Schema
from pydantic import Field


TData = TypeVar("TData")


class PingResponseSchema(Schema):
    result: bool


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
