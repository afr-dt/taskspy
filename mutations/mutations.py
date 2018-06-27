import graphene
from config import db_session
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError
from sqlalchemy import update

from objtypes.types import(Task, TaskModel)


class TaskInput(graphene.InputObjectType):
    """Task Mutation"""
    task_id = graphene.Int(required=False)
    title = graphene.String(required=False)
    description = graphene.String(required=False)
    timer = graphene.Int(required=False)
    status = graphene.Boolean(required=False)
    created = graphene.String(required=False)
    updated = graphene.String(required=False)


class CreateTask(graphene.Mutation):
    """Create Task"""
    class Arguments:
        task_data = TaskInput(required=True)
    task = graphene.Field(lambda: Task)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, task_data=None):
        try:
            task = TaskModel(**task_data)
            db_session.add(task)
            db_session.commit()
            return CreateTask(task=task, status=True)
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error inserting Task... {}".format(err))


class EditTask(graphene.Mutation):
    class Arguments:
        task_data = TaskInput()
    task = graphene.Field(lambda: Task)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, task_data=None):
        try:
            query = Task.get_query(info)
            task = TaskModel(task_id=task_data.task_id)
            query.filter(TaskModel.task_id == task.task_id).update(task_data)
            db_session.commit()
            return EditTask(task=task, status=True)
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error edit Task... {}".format(err))
