from seaplane import app, start, task

#Remember to add your SEAPLANE_API_KEY in .env file

@task(type="compute", id="hello-world-task")
def hello_world_task(data):
    return "hello world"


@app(id="hello-world-app", path="/hello")
def hello_world_app(data):
    return hello_world_task(data)


start()
