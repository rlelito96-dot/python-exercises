
#imports

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

#create your database

engine = create_engine("sqlite:///pierwszy.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#define models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan"  )

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

Base.metadata.create_all(engine)

#Utility functions

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt:str) -> bool:
    return input(f"{prompt} yes/no: ").strip().lower() == "yes"

#CRUD Ops

def add_user():
    name, email = input(f"Enter user name: "), input(f"Enter the email: ")
    if get_user_by_email(email):
        print(f"User already exists: {email}")
        return

    try:
        session.add(User(name=name, email=email))
        session.commit()
        print(f"User {name} has been added!")
    except IntegrityError:
        session.rollback()
        print(f"ERROR")

def add_task():
    email = input(f"Enter the email of the user to add tasks: ")
    user = get_user_by_email(email)

    if not user:
        print(f"No user found with that email.Try again.")
        return

    title, description = input(f"Enter the title: "), input(f"Enter the description: ")
    session.add(Task(title=title, description=description, user=user))
    session.commit()
    print(f"Added to the database: {title}:{description}")


#Query

def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id} Name: {user.name} Email: {user.email}")

def query_tasks():
    email = input(f"Enter the email of the user for tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f"There was no user with that email.")
        return

    if not user.tasks:
        print(f"User {email} has no tasks yet.")
        return

    for task in user.tasks:
        print(f"Task ID: {task.id} Title: {task.title}")

def update_user():
    email = input(f"Enter the email of user for update: ")
    user = get_user_by_email(email)
    if not user:
        print(f"User does not exist!")
        return

    user.name = input(f"Enter a new name for the user(leave blank to stay the same): ") or user.name
    user.email = input(f"Enter a new email for the user(leave blank to stay the same): ") or user.email
    session.commit()
    print(f"User has been updated!!")

#Deleting

def delete_user():
    email = input(f"Enter the email of user for delete: ")
    user = get_user_by_email(email)

    if not user:
        print(f"User {email} does not exist!")
        return

    if confirm_action(f"Are u sure u want to delete a user: {user.name}"):
        session.delete(user)
        session.commit()
        print(f"User {user.name} has been deleted!")

def delete_task():
    email = input(f"Enter the email linked to the tasks: ")
    user = get_user_by_email(email)

    if not user:
        print(f"User {email} does not exist!")
        return

    for task in user.tasks:
        print(f"Task ID: {task.id} Title: {task.title}")

    task_id = input(f"Enter ID of task to delete: ")

    task = next((t for t in user.tasks if str(t.id) == task_id), None)

    if confirm_action(f"Are you sure you want to delete this task: {task.id} "):
        session.delete(task)
        session.commit()
        print(f"Task has been deleted!")

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

        choice = input(f"Enter an option: ")

        if choice == "8":
            print(f"Adios!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print(f"That is not an option!")

if __name__ == "__main__":
    main()
