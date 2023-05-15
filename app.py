from flask import Flask, render_template, request
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    archivos = glob.glob("*.sql") + glob.glob("*.txt")
    relacion_actual = "AND TRA.COD_ESTADO_FIRMA = 1"
    relacion_nueva = "AND TRA.COD_ESTADO_FIRMA IN (1,2)"
    relacion_actual = relacion_actual.replace("= ", "=")
    cambiar_relacion_archivos(archivos, relacion_actual, relacion_nueva)

    num_archivos = len(archivos)
    return render_template('result.html', num_archivos=num_archivos, archivos=archivos)

if __name__ == '__main__':
    app.run(debug=True)
