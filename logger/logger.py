import datetime
from flask_socketio import emit


class Logger:
    def __init__(self, socketio):
        self.socketio = socketio
        self._setup_events(socketio)

    def send_message(self, message):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        self.socketio.emit('message', {'message': time + ' ' + message}, namespace='/', broadcast=True)
        self.socketio.sleep(0)

    def _setup_events(self, socketio):
        @socketio.on('my event', namespace='/')
        def test_message(message):
            emit('my response', {'data': message['data']})
            self.socketio.emit('message', {'check logger': 'logger is connected'})

        # @socketio.on('connect', namespace='/')
        # def test_connect():
        #     emit('my response', {'data': 'Connected'})
        #
        # @socketio.on('disconnect', namespace='/')
        # def test_disconnect():
        #     print('Client disconnected')
