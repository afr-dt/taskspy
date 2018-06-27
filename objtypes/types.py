import graphene
from graphene import relay
from graphene.relay import Connection, ConnectionField
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import(Task as TaskModel)


class Task(SQLAlchemyObjectType):
    """Task Object"""
    class Meta:
        model = TaskModel
        interfaces = (relay.Node, )
