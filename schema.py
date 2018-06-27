import graphene
from sqlalchemy import update
from graphene import relay, Connection
from graphene.relay import Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import insert

from mutations.mutations import CreateTask, EditTask
from objtypes.types import(Task, TaskModel)


class Query(graphene.ObjectType):

    tasks = SQLAlchemyConnectionField(
        Task, status=graphene.Boolean(), required=False)

    # def resolve_tasks(self, info, status):
    #     query = Task.get_query(info)
    #     return query.filter(TaskModel.status == status).all()

    task = graphene.Field(lambda: Task, task_id=graphene.Int())

    def resolve_task(self, info, task_id):
        query = Task.get_query(info)
        return query.filter(TaskModel.task_id == task_id).first()


class TasksMutations(graphene.ObjectType):
    create_task = CreateTask.Field()
    edit_task = EditTask.Field()


schema = graphene.Schema(query=Query, mutation=TasksMutations, types=[
                         Task], auto_camelcase=False)
