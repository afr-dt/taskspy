import graphene
from sqlalchemy import update
from graphene import relay, Connection
from graphene.relay import Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert

from mutations.mutations import (CreateTask, CreateUser)

from objtypes.types import(User, UserModel, Task, TaskModel)


class Query(graphene.ObjectType):

    tasks = SQLAlchemyConnectionField(Task)
    task = graphene.Field(lambda: Task, task_id=graphene.Int())

    def resolve_task(self, info, task_id):
        query = Task.get_query(info)
        return query.filter(TaskModel.task_id == task_id).first()


class TasksMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_task = CreateTask.Field()


schema = graphene.Schema(query=Query, mutation=TasksMutations, types=[
                         User, Task], auto_camelcase=False)
