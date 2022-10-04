import grpc
from concurrent import futures
import movie_pb2
import movie_pb2_grpc
import json


class MovieServicer(movie_pb2_grpc.MovieServicer):

    def __init__(self):
        with open('{}/data/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]

    def GetMovieByID(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'],
                                           id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="", id="")

    def GetListMovies(self, request, context):
        for movie in self.db:
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'],
                                      id=movie['id'])

    def GetMovieByTitle(self, request, context):
        for movie in self.db:
            if movie['title'] == request.title:
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'],
                                           id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="",
                                   id="")

    def GetMovieByRating(self, request, context):
        for movie in self.db:
            print(movie['rating'], request.rating, movie['rating'] - request.rating < 0.0)
            if movie['rating'] - request.rating < 0.0:
                print("Rating found")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'],
                                           id=movie['id'])
        return movie_pb2.MovieData(title="", rating=0.0, director="",
                                   id="")

    def PostMovie(self, request, context):
        self.db.append({"title":request.title,"rating":request.rating,"director":request.director,"id":request.id})
        return self.GetMovieByID(request,context)

    def PutRateByMovieId(self, request, context):
        for movie in self.db:
            if movie['id'] == request.id:
                movie['rating'] = request.rating + 0.01
        return self.GetMovieByID(request, context)

    def DeleteByMovieId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
