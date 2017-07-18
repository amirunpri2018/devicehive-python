from tests.types import string


def test_send(test):

    def handle_connect(handler):
        device_id = test.generate_id('send-command')
        command_name = test.generate_id('send-command')
        device = handler.api.put_device(device_id)
        command = device.send_command(command_name)
        assert command.device_id() == device_id
        assert isinstance(command.id(), int)
        assert isinstance(command.user_id(), int)
        assert command.command() == command_name
        assert not command.parameters()
        assert not command.lifetime()
        assert isinstance(command.timestamp(), string)
        assert not command.status
        assert not command.result
        command_name = test.generate_id('send-command')
        parameters = 'parameters'
        lifetime = 10
        status = 'status'
        result = {'key': 'value'}
        command = device.send_command(command_name, parameters=parameters,
                                      lifetime=lifetime, status=status,
                                      result=result)
        assert command.device_id() == device_id
        assert isinstance(command.id(), int)
        assert isinstance(command.user_id(), int)
        assert command.command() == command_name
        assert command.parameters() == parameters
        assert command.lifetime() == lifetime
        assert isinstance(command.timestamp(), string)
        assert command.status == status
        assert command.result == result
        device.remove()

    test.run(handle_connect)
