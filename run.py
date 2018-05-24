from app import create_app


if __name__ == '__main__':

    flask_app = create_app('dev')

    flask_app.run()

    with flask_app.app_context():
        db.create_all()
    flask.app.run()
