from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('Index.html')  

# @app.route('/javascript')                           
# def javascript():
#     return render_template('Javascript.html')  

# @app.route('/test')                           
# def testpage():
#     return render_template('test.html')  

if __name__=="__main__":
    app.run(debug=True)     