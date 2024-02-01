from django.http import HttpResponse
from django.shortcuts import render
import datetime

tools_list = {"Postman": 5, 
              "Python": 4,
              "Selenium": 5,
              "Jenkins": 4,
              "Cypress": 4,
              "Playwright": 4,
              "Azure Pipelines": 3
            }

# Create your views here.
def index(request):
    return render(request, "my_skills/index.html", {
        "tools": tools_list,
        "max_value": [1,2,3,4,5]
    })



# Create your views here.
