from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculateur IMC</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: 50px auto; padding: 20px; }
        input, button { padding: 8px; margin: 5px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; }
        .result { background: #e8f4f8; padding: 15px; margin-top: 20px; text-align: center; }
    </style>
</head>
<body>
    <h1>Calculateur IMC</h1>
    <form method="POST">
        <label>Poids (kg) :</label>
        <input type="number" name="weight" step="0.1" required><br>
        <label>Taille (m) :</label>
        <input type="number" name="height" step="0.01" required><br>
        <button type="submit">Calculer</button>
    </form>
    {% if imc %}
    <div class="result">
        <h2>Résultat :</h2>
        <p>Votre IMC : <strong>{{ imc }}</strong></p>
        <p>Catégorie : <strong>{{ category }}</strong></p>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        imc = weight / (height * height)
        
        if imc < 18.5:
            category = "Maigreur"
        elif imc < 25:
            category = "Normal"
        elif imc < 30:
            category = "Surpoids"
        else:
            category = "Obésité"
            
        return render_template_string(HTML_TEMPLATE, imc=round(imc, 1), category=category)
    
    return render_template_string(HTML_TEMPLATE, imc=None, category=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
