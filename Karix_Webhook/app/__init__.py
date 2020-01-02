from .manage import create_app, app_init_rebbitmq, init_task
from .create_logfile import createLogfile


__all__ = ["app", "uid_object", "run_server"]

app = create_app()

createLogfile()

app_init_rebbitmq()  # Start Rebbit Mq


@app.route('/<id>')
def uid_object(id):

    init_task(id)  # Fetch And Validation Task

    return "ok"


def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'))
