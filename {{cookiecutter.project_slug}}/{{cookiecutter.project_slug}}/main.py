from seaplane.apps import app, start, task

#Remember to add your SEAPLANE_API_KEY in .env file

@task(type="compute", id="{{cookiecutter.project_slug}}-task")
def hello_world_task(context):
    # This goes into the seaplane log
    print(f"got context data {context.body}")

    context.emit(b"hello world!")

@app(id="{{cookiecutter.project_slug}}-app")
def hello_world_app(data):
    return hello_world_task(data)


start()
