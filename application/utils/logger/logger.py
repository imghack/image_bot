import datetime

TIME_FORMAT = '%H:%M:%S'


class Logger:
    def __init__(self, socketio):
        self._socketio = socketio
        self._setup_events(socketio)

    def send_message(self, message):
        time = datetime.datetime.now().strftime(TIME_FORMAT)
        self._socketio.emit('message', {'message': time + ' ' + message})

    def _setup_events(self, socketio):
        @socketio.on('connect', namespace='/')
        def connect():
            self._socketio.emit('message', {'users': 'new user is connected'})

        @socketio.on('disconnect', namespace='/')
        def disconnect():
            self._socketio.emit('message', {'users': 'user closed app'})
