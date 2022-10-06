import grpc

import movie_pb2
import movie_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc


def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)


def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % movie.title)


def GetMovieByTitle(stub, title):
    movie = stub.GetMovieByTitle(title)
    print(movie)


def GetMovieByRating(stub, rating):
    movie = stub.GetMovieByRating(rating)
    print(movie)


def PostMovie(stub, movie):
    movie = stub.PostMovie(movie)
    print(movie)


def PutRateByMovieId(stub, movieRateById):
    movie = stub.PutRateByMovieId(movieRateById)
    print(movie)


def DeleteByMovieId(stub, id):
    movie = stub.DeleteByMovieId(id)
    print(movie)


def GetSchedule(stub):
    allSchedules = stub.GetSchedule(showtime_pb2.ShowtimeEmpty())
    print(allSchedules)
    '''    for schedule in allSchedules:
        print(schedule)'''


def GetScheduleByDate(stub, date):
    schedule = stub.GetScheduleByDate(date)
    print(schedule)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    """
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)


        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub)

        print("---------GetMovieByTitle-------------")
        title = movie_pb2.MovieTitle(title="The Good Dinosaur")
        GetMovieByTitle(stub, title)

        print("---------GetMovieByRating-------------")
        rating = movie_pb2.MovieRating(rating=7.4)
        GetMovieByRating(stub, rating)

        print("---------PostMovie-------------")
        movie = movie_pb2.MovieData(title="MonNouveauFilm", director="Moi Forcement", rating=10.0, id="id")
        PostMovie(stub, movie)

        print("---------PutRateByMovieId-------------")
        movie = movie_pb2.MovieIdRating(id="id", rating=0.0)
        PutRateByMovieId(stub, movie)

        print("---------DeleteByMovieId-------------")
        id = movie_pb2.MovieID(id="id")
        DeleteByMovieId(stub, id)
        """

    with grpc.insecure_channel('localhost:30O2') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("---------GetSchedule-------------")
        GetSchedule(stub)

        print("---------GetScheduleByDate-------------")
        date = showtime_pb2.Date(date="20151130")
        GetScheduleByDate(stub, date)

    channel.close()


if __name__ == '__main__':
    run()
