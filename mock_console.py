class MockConsole:
    def __init__(self):
        self.data_for_storing_request_and_response = []
        self.message_call_queue = []

    def add_expected_request_and_response(self, request, response):
        self.data_for_storing_request_and_response.append((request, response))

    def add_expected_output_message(self, message):
        self.message_call_queue.append(message)

    def _delete_call_from_storing_request_and_response(self):
        self.data_for_storing_request_and_response.pop(0)

    def input(self, message):
        if message != self.data_for_storing_request_and_response[0][0]:
            raise AssertionError
        result = self.data_for_storing_request_and_response[0][1]
        self._delete_call_from_storing_request_and_response()
        return result

    def print(self, message):
        if message not in self.message_call_queue or self.message_call_queue[0] != message:
            raise AssertionError
        return self._get_massage_massage_from_queue()

    def _get_massage_from_queue(self):
        return self.message_call_queue[0]

    def _delete_massage_from_queue(self):
        self.message_call_queue.pop(0)

    def _get_massage_massage_from_queue(self):
        result = self._get_massage_from_queue()
        self._delete_massage_from_queue()
        return result

    def verify_all_calls_have_been_made(self):
        if self.data_for_storing_request_and_response or self.message_call_queue:
            raise AssertionError
