import docker

client = docker.from_env()
output = client.containers.run("myfirstpythonapp:latest", auto_remove=True, stdout=True)
print(output)
