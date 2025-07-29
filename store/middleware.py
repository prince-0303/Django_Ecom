import time

class TimeTaken:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        started = time.time()
        ended = time.time()
        time_taken = ended-started
        print(f'Time taken to execute is : {time_taken:.6f}s')

        response = self.get_response(request)
        return response