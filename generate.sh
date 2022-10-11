#!/bin/bash

python -m grpc_tools.protoc -I=./movie/protos --python_out=./movie --grpc_python_out=./movie movie.proto
python -m grpc_tools.protoc -I=./showtime/protos --python_out=./showtime --grpc_python_out=./showtime showtime.proto

cp ./movie/movie_pb2.py ./movie/movie_pb2_grpc.py ./showtime/showtime_pb2.py ./showtime/showtime_pb2_grpc.py ./client
cp ./showtime/showtime_pb2.py ./showtime/showtime_pb2_grpc.py ./booking
cp ./movie/movie_pb2.py ./movie/movie_pb2_grpc.py ./user