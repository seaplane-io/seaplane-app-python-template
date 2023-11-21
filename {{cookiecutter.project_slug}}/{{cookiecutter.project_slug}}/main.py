from seaplane.apps import app, start, task

# Remember to add your SEAPLANE_API_KEY in .env file

# Uncomment the relevant application based on your Seaplane version. You can find out your Seaplane version by running seaplane --version in your CLI.

###################
## Version 0.5.x ##
###################

# @task()
# def hello_world_task(context):
#     # This goes into the seaplane log
#     print(f"got context data {context.body}")

#     context.emit(b"hello world!")


# @app()
# def hello_world_app(data):
#     return hello_world_task(data)


# start()

###################
## Version 0.4.0 ##
###################

# @task(id="hello-world-task", type="compute")
# def hello_world_task(context):
#     # This goes into the seaplane log
#     print(f"got context data {context.body}")

#     context.emit(b"hello world!")


# @app(id="hello-world-app", path="/hello")
# def hello_world_app(data):
#     return hello_world_task(data)


# start()
