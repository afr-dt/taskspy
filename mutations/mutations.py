import graphene
from config import db_session
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError
from sqlalchemy import update

from objtypes.types import(Task, TaskModel, User, UserModel)


class UserInput(graphene.InputObjectType):
    """User Mutation"""
    user_id = graphene.Int(required=True)
    username = graphene.String(required=True)
    surname = graphene.String(required=False)


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)
    user = graphene.Field(lambda: User)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, user_data=None):
        try:
            user = UserModel(**user_data)
            db_session.add(user)
            db_session.commit()
            return CreateUser(user=user, status=True)
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error inserting data {}".format(err))


class TaskInput(graphene.InputObjectType):
    """Task Mutation"""
    task_id = graphene.Int(required=False)
    title = graphene.String(required=True)
    description = graphene.String(required=True)
    timer = graphene.Int(required=True)
    status = graphene.Boolean(required=False)
    created = graphene.String(required=False)
    updated = graphene.String(required=False)


class CreateTask(graphene.Mutation):
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
