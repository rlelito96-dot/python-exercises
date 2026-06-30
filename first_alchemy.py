
#import

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError

#create database

engine = create_engine("sqlite:///wlasny.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#define models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    tasks = relationship('Task', back_populates="user", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship('User', back_populates="tasks")

Base.metadata.create_all(engine)

#utility functions(pomocniki)

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt:str) -> bool:
    return input(f"{prompt} (yes/no): ").strip().lower() == 'yes'

#CRUD Ops

def add_user():
    name, email = input(f"Enter name of new user: "), input(f"Enter email of new user: ")
    user = get_user_by_email(email)
    if user:
        print(f"User with this email already exist!")
        return

    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print(f"User {new_user.name} has been added!")

    except IntegrityError:
        session.rollback()
        print(f"ERROR")

def add_task():
    email = input(f"Enter email of user to add tasks: ")
    user = get_user_by_email(email)

    if not user:
        print(f"User with this email does not exist!")
        return

    title = input(f"Enter the title of task to add: ")
    description = input(f"Enter the description of task to add: ")

    session.add(Task(title=title, description=description, user=user))
    session.commit()
    print(f"Added to the database: {title}: {description}")

#Query

def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id} Name: {user.name} Email: {user.email}")

def query_tasks():
    email = input(f"Enter email of user to display tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f"User does not exist!")
        return

    if not user.tasks:
        print(f"User with this email does not have any tasks yet.")
        return

    for task in user.tasks:
        print(f"ID: {task.id} Title: {task.title} Description: {task.description}")

def update_user():
    email = input(f"Enter email of user for update: ")
    user = get_user_by_email(email)
    if not user:
        print(f"User does not exist!")
        return

    user.name = input(f"Enter a new name to update(leave blank to stay the same): ") or user.name
    user.email = input(f"Enter a new email to update(leave blank to stay the same): ") or user.email

    session.commit()
    print(f"User has been updated!")

#Deleting

def delete_user():
    email = input(f"Enter email of user for delete: ")
    user = get_user_by_email(email)
    if not user:
        print(f"User does not exist!")
        return

    if confirm_action(f"Are u sure u want to delete this user: {user.name}"):
        session.delete(user)
        session.commit()

        print(f"User {user.name} has been deleted!")

def delete_task():
    email = input(f"Enter email of user: ")
    user = get_user_by_email(email)
    if not user:
        print(f"User does not exist!")
        return

    if not user.tasks:
        print(f"User with this email does not have any tasks yet.")
        return

    for task in user.tasks:
        print(f"ID: {task.id} Title: {task.title} Description: {task.description}")


    task_id = input(f"Enter ID of task to delete: ")
    task = next((x for x in user.tasks if str(x.id) == task_id), None)

    if task is None:
        print(f"Task not found!")
        return

    if confirm_action(f"Are u sure u want to delete this task: {task.title}"):
        session.delete(task)
        session.commit()

        print(f"Task {task.title} has been deleted!")

#Main Ops

def main() -> None:
    actions = {
        "1": add_user,
        "2": add_task,
        "3": query_users,
        "4": query_tasks,
        "5": update_user,
        "6": delete_user,
        "7": delete_task

    }

    while True:
        print("\nOptions:\n1. Add user\n2. Add task\n3. Query users\n4. Query task\n"
              "5. Update user\n6. Delete user\n7. Delete task\n8. Exit")

        choice = input(f"Enter an option(1-8): ")

        if choice == "8":
            print("Adios!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print(f"That is not an option! Please choose number from 1 to 8.")

if __name__ == "__main__":
    main()