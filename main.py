from flask import Flask, jsonify
app=Flask(__name__)
data=[
    {
        "Name":"Audi R8"
    },{
        "Name":"Lamborghini Urus"
    }
]
@app.route("/")
def Hello():
    return "Hello user"
@app.route("/show")
def Showdata():
    return jsonify({"info":data})
@app.route("/create",methods=["POST"])
def Createdata():
    n3={"Name":"Mercedes-Benz Vision AVTR"}
    data.append(n3)
    return jsonify({"data":n3})
if __name__ =="__main__":
    app.run()