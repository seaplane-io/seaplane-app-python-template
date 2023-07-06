from seaplane import app, task, config, start

config.set_api_key("sp-your_api_key")

@task(type="compute", id='hello-world-task')
def hello_world_task(data):
	return "hello world"

@app(id='hello-world-app', path='/hello')
def hello_world_app(data):
	return hello_world_task(data)


start()