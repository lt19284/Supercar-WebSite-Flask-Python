from flask import Flask, render_template # dòng import flask và render từ template

app=Flask(__name__) # dòng khởi tạo Flask app

@app.route('/') 
def home(): 
    return render_template('index.html') # dong trả về template index.html
@app.route('/team')
def team():
    return render_template('team.html') # dong trả về template team.html

# chạy flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)