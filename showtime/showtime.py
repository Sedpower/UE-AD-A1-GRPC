import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc
import json


class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    def GetSchedule(self, request, context):
        for schedule in self.db:
            yield showtime_pb2.Schedule(date=schedule['date'], movies=schedule['movies'])

    def GetScheduleByDate(self, request, context):
        for schedule in self.db:
            if schedule['date'] == request.date:
                return showtime_pb2.Schedule(date=schedule['date'], movies=schedule['movies'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    print("started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
