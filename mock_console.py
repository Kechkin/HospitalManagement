class MockConsole:
    data_for_storing_request_and_response = {}
    stack_calls = []

    def add_expected_request_and_response(self, request, response):
        self.data_for_storing_request_and_response[request] = response

    def add_expected_output_message(self, message):
        self.stack_calls.append(message)

    def input(self, message):
        if message not in self.data_for_storing_request_and_response:
            raise AssertionError
        return self.data_for_storing_request_and_response[message]

    def _delete_massage_from_stack(self):
        self.stack_calls.pop(0)

    def _get_massage(self):
        result = self.stack_calls[0]
        self._delete_massage_from_stack()
        return result

    def print(self, message):
        if message not in self.stack_calls or self.stack_calls[0] != message:
            self.stack_calls.clear()
            raise AssertionError
        else:
            return self._get_massage()

    def verify_all_calls_have_been_made(self):
        if self.data_for_storing_request_and_response or self.stack_calls:
            raise AssertionError
