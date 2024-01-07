# used libraries
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

#definition of the program initial route
@app.route('/')
def index():
    #read the file and create the table in html
    excel_file = 'D:\Projetos de Programação\Planilha_Web\static\sheets\_tabela.xlsx' 
    df = pd.read_excel(excel_file)
    table_html = df.to_html(classes='table table-bordered', index=False)
    #rederiza the tamplate
    return render_template('index.html', table_html=table_html)

#start the server
if __name__ == '__main__':
    app.run(debug=True)
