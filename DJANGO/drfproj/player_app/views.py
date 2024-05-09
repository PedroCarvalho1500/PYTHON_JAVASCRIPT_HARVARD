from .models import Player
from django.shortcuts import render, redirect
import csv
import pandas as pd


def home(request):
    with open('out.csv') as f:
        f_csv = csv.reader(f) 
        headers = next(f_csv) 
        for row in f_csv:
            print(row)
            player = Player.objects.create(name=row[1], team=row[2],total_goals=row[3], total_assists=row[4],market_value=row[5])
            player.save()

    return (request,'<h1> CREATE PLAYERS </h1>')