from invoke import task

@task
def start(ctx):
    ctx.run("python3 services/budget_service.py")
