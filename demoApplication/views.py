from django.http import HttpResponse
from django.shortcuts import render,redirect
import random
users = {}

quotes = {
    "category1":[
        "Quote 1",
        "Quote 2",
        "Quote 3",
        "Quote 4",
    ],
    "category2":[
        "category2 Quote 1",
        "category2 Quote 2",
        "category2 Quote 3",
        "category2 Quote 4",
    ],
    "category3":[
        "category3 Quote 1",
        "category3 Quote 2",
        "category3 Quote 3",
        "category3 Quote 4",
    ],
    "category4":[
        "category4 Quote 1",
        "category4 Quote 2",
        "category4 Quote 3",
        "category4 Quote 4",
    ]
}

def home(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")
        username = req.POST.get("username")
        users[username] = {"email":email,"password":password}
        print(users)
        # users[username] = password
        return render(req,"login.html")
    
    return render(req, "index.html")
    
def login(req):
    if req.method == "POST":
        username = req.POST.get("username")    
        password = req.POST.get("password") 
    
        if username in users and users[username]["password"] == password:
            print(f"{username} found")
            return redirect("about")
        
        return render(req, "login.html", {"error":"User not found"})
        

def about(req):
    quote = None
    if req.method == "POST":
        category = req.POST.get("category")
        if category in quotes:
            quote = random.choice(quotes[category])
    return render(req,"about.html", {"quotes":quote})

def contact(req):
    return render(req, "contact.html")