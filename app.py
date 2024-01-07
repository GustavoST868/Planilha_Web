from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Ler os dados da planilha Excel
    excel_file = 'D:\Projetos de Programação\Planilha_Web\static\spreadsheets\produtos.xlsx'  
    df = pd.read_excel(excel_file)

    # Converter os dados para HTML
    table_html = df.to_html(classes='table table-bordered', index=False)

    return render_template('index.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
