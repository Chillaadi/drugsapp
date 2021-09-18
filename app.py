import pickle 
from flask import Flask , render_template, request
 #global variables 
loadedModel = pickle.load(open("DRUGS CLASSIFICATION.pkl",'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/prediction', methods = ['POST'])
def prediction():
    Age = request.form['Age']
    Sex = request.form['Sex']
    BP =  request.form['BP']
    Cholesterol = request.form['Cholesterol']
    Na_to_K = request.form['Na_to_K']

    prediction= loadedModel.predict([[Age,Sex,BP,Cholesterol,Na_to_K ]])[0]
    If prediction == drugX:
        prediction = " Use Sodium polystyrene sulfonate (Kayexalate)"
    Elif prediction == drugY:
        prediction = " Use Sodium polystyrene sulfonate (e.g.Kayexalate) "
    Elif prediction == drugC:
        prediction = " use miscellaneous cardiovascular agents midodrine "
    Elif prediction == drugA:
        prediction = "ACE inhibitor or an angiotensin-2 receptor blocker (ARB)"
    Else : 
        prediction = "calcium channel blocker"
    return render_template('index.html', api_output=prediction)
   
#main Function
if __name__ == '__main__':
    app.run(debug=True)
