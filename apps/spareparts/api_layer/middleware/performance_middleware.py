from starlette.middleware.base import BaseHTTPMiddleware
import time

class PerformanceMiddleware(BaseHTTPMiddleware):

    def dispatch(self, request, call_next):
        start_time = time.perf_counter()
        response = call_next(request)
        process_time  = time.perf_counter() - start_time
        print(f'process time: {process_time}')
        return response


