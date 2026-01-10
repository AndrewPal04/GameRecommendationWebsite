#Game Recommendation Program Final project

#Game Options:
#1-Fortnite
#2-Roblox
#3-Minecraft
#4-Call of duty
#5-Valorant
#6-FNAF
#7-Subway Surfers
#8-Geometry Dash
#9-Super Smash Bros
#10-Mario Kart
#11-Spider-man
#12-Wii Sports
#13-Rocket League
#14-Halo
#15-Marvel Rivals
#16-Brawl Stars
#17-Granny
#18-Moto X3M
#19-Night City Driving
#20-Fall Guys

#Questions that determine the game they like

#What device do you often play on? (1. Tablet/Phone 2. Laptop/Computer/PC 3. Playstation 4. Nintendo 5. Other)
#What Genre do you prefer? (1. Horror 2. Fighting 3. Gun/combat 4. Sports 5. Racing 6. Obstacle 7. Running 8. Superheroes 9. Creativity/Education 10. Car/Vehicle)
#How old are you?
#How intense would you like your games? (Scale from 1-10)
#How well do you like your graphics?(1. Really good 2. Somewhat good 3. I dont care 4. Kind of bad 5. Really bad)
#Do you like games that requires WiFi?(1. Yes 2. No)
#Do you like single player or multiplayer games?(1. Singleplayer 2. Both 3. Mulitplayer)
#Do you like games that you can play with your friends?(1. Yes 2. Any 3. No)
#Do you prefer games that only require hand, arrow/WASD or mouse and WASD movement?(1. Hand 2. WASD/Arrows 3. WASD+Mouse)

#preferences
from sklearn import svm
from flask import Flask, request, render_template

app = Flask(__name__)

    
iData = [
    [1, 2, 11, 8, 1, 1, 3, 1, 1],  #brawlstars 1
    [4, 4, 10, 5, 3, 2, 2, 1, 1],  #wii sports 1
    [2, 9, 9, 4, 2, 1, 2, 1, 3],  #roblox 1
    [2, 1, 12, 10, 1, 2, 1, 3, 3],  #FNAF 1
    [4, 2, 10, 8, 2, 1, 2, 1, 1],  #Super Smash Bros 1
    [2, 3, 11, 9, 2, 1, 3, 2, 3],  #Fortnite 1
    [2, 3, 12, 10, 1, 1, 3, 1, 3],  #Valorant 1
    [1, 6, 9, 4, 3, 2, 1, 3, 1],  #Subway Surfers 1
    [2, 3, 13, 9, 1, 1, 3, 1, 3],  #COD 1
    [1, 9, 9, 3, 2, 2, 2, 2, 1],  #Minecraft 1
    [2, 1, 12, 10, 2, 2, 1, 3, 3],  #Granny 1
    [1, 6, 8, 5, 3, 2, 1, 3, 1],  #Geometry Dash 1
    [4, 5, 11, 8, 1, 1, 2, 2, 1],  #Mario Kart 1
    [3, 8, 12, 9, 1, 1, 1, 2, 1],  #Spider-Man 1
    [3, 4, 13, 7, 2, 1, 3, 1, 1],  #Rocket League 1
    [5, 3, 14, 8, 1, 1, 2, 1, 1],  #Halo 1
    [3, 8, 12, 8, 2, 1, 2, 1, 1],  #Marvel Rivals 1
    [2, 10, 11, 3, 3, 2, 1, 3, 2],  #Moto X3M 1
    [2, 5, 10, 5, 3, 2, 1, 3, 2],  #Night City Driving 1
    [3, 6, 12, 8, 2, 1, 2, 1, 1]  #Fall Guys 1
]
#games
oData = [16, 12, 2, 6, 9, 1, 5, 7, 4, 3, 17, 8, 10, 11, 13, 14, 15, 18, 19, 20]

model = svm.SVC()
model.fit(iData,oData)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    device = int(request.form["device"])
    genre = int(request.form["genre"])
    age=int(request.form["age"])
    intensity=int(request.form["intensity"])
    graphics=int(request.form["graphics"])
    wifi = int(request.form["WiFi"])
    player = int(request.form["player"])
    friends=int(request.form["friends"])
    gType=int(request.form["type"])
    
    
    userInput=[[device, genre, age, intensity, graphics, wifi, player, friends, gType]]
    recommendation = model.predict(userInput)[0]
    print(recommendation)
    if recommendation == 1:
        return render_template("fortnite.html")
    elif recommendation == 2:
        return render_template("roblox.html")
    elif recommendation == 3:
        return render_template("minecraft.html")
    elif recommendation == 4:
        return render_template("callofduty.html")
    elif recommendation == 5:
        return render_template("valorant.html")
    elif recommendation == 6:
        return render_template("fnaf.html")
    elif recommendation == 7:
        return render_template("subwaysurfers.html")
    elif recommendation == 8:
        return render_template("geometrydash.html")
    elif recommendation == 9:
        return render_template("supersmashbros.html")
    elif recommendation == 10:
        return render_template("mariokart.html")
    elif recommendation == 11:
        return render_template("spiderman.html")
    elif recommendation == 12:
        return render_template("wiisports.html")
    elif recommendation == 13:
        return render_template("rocketleague.html")
    elif recommendation == 14:
        return render_template("halo.html")
    elif recommendation == 15:
        return render_template("marvelrivals.html")
    elif recommendation == 16:
        return render_template("brawlstars.html")
    elif recommendation == 17:
        return render_template("granny.html")
    elif recommendation == 18:
        return render_template("motox3m.html")
    elif recommendation == 19:
        return render_template("nightcitydriving.html")
    elif recommendation == 20:
        return render_template("fallguys.html")

    return "<h1>still under development</h1>"

    
if __name__ == "__main__":
    app.run(debug = True)

