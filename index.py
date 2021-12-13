from flask import Flask
import urllib.request, json

from flask.templating import render_template

app = Flask(__name__)

@app.route('/home')
def image_gallery():

    extrnl_url = "https://api.unsplash.com/photos/?client_id=M39mWqoPe7zkn4chJ2h6SROKD9NwIBPEPcDWEbPMNBk"

    
    res = urllib.request.urlopen(extrnl_url)
    data = res.read()
    dic = json.loads(data)

    imgURL = []

    for img in dic:
        img = {
            "id": img["id"],
            "height": img["height"],
            "url":img["urls"]
        }
        imgURL.append(img)

    return render_template("data.html", uDatas = imgURL)

if __name__ == "__main__":
    app.run(debug=True)