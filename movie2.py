from flask import*
import requests
API_KEY='ec91ef94'
URL='http://www.omdbapi.com/?apikey=ec91ef94'
app=Flask(__name__)
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['movie_title']
        year=request.form['year']
        params={
            't':name,
            'y':year
        }
        response=requests.get(URL,params=params)
        if response.status_code==200:
            movie=response.json()
            return render_template('movieview2.html',movie=movie)
        else:
            return "<html><body><h1>Movie not found!</h1></body></html>"
    else:
        return render_template('movie2index.html')
if __name__=='__main__':
    app.run(debug=True)