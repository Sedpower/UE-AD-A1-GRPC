from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
import grpc
import showtime_pb2
import showtime_pb2_grpc

app = Flask(__name__)

PORT = 3003
HOST = '0.0.0.0'

with open('{}/data/bookings.json'.format("."), "r") as jsf:
   bookings = json.load(jsf)["bookings"]


@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Booking service!</h1>"


# récupérer le JSON booking
@app.route("/bookings", methods=['GET'])
def get_json():
   return make_response(jsonify(bookings), 200)


# recupérer le bookings d'un user JSON
@app.route("/bookings/<userid>", methods=['GET'])
def get_booking_for_user(userid):
   for book in bookings:
      if str(userid) == str(book["userid"]):
         res = make_response(jsonify(book), 200)
         return res
   return make_response(jsonify({"error": "bad input parameter"}), 400)


# ajouter un film au bookings d'un user via userid
@app.route("/bookings/<userid>", methods=['POST'])
def add_booking_byuser(userid):
   req = request.get_json()

   # appelle api showtime pour savoir si le film est présent à la date donnée

   with grpc.insecure_channel('localhost:3002') as channel:

      stub = showtime_pb2_grpc.ShowtimeStub(channel)

      date = showtime_pb2.Date(date=str(req["date"]))
      res_movies = stub.GetScheduleByDate(date)
      trouve =  False
      for moviesId in res_movies.movies:
         if str(req["movies"]) == str(moviesId):
            trouve = True

   channel.close()

   if not trouve:
      return make_response(jsonify({"error": "movie non dispo"}), 400)

   for booking in bookings:
      if str(userid) == str(booking["userid"]):
         for dates in booking["dates"]:
            if str(dates["date"]) == str(req["date"]):
               for movie in dates["movies"]:
                  if str(movie) == str(req["movies"]):
                     return make_response(jsonify({"error": "an existing item already exists"}), 409)
               dates["movies"].append(req["movies"][0])
               res = make_response(jsonify(booking), 200)
               return res
         booking["dates"].append(req)
         res = make_response(jsonify(booking), 200)
         return res

   return make_response(jsonify({"error": "bad input parameter"}), 400)


if __name__ == "__main__":
   print("Server running in port %s" % (PORT))
   app.run(host=HOST, port=PORT)