from flask import Flask, request, jsonify, render_template_string
from codes_testing import find_sums

app = Flask(__name__)

# HTML шаблон для веб-интерфейса
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test find_sums Function</title>
    <style>
        body { font-family: Arial; margin: 50px; }
        .container { max-width: 600px; }
        input, button { padding: 10px; margin: 5px; }
        .result { margin-top: 20px; padding: 15px; border: 1px solid #ccc; }
        .success { background-color: #d4edda; }
        .error { background-color: #f8d7da; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧪 Test find_sums Function</h1>
        
        <h3>Введите данные:</h3>
        <form id="testForm">
            <p>
                <label>Массив (через запятую):</label><br>
                <input type="text" id="array" placeholder="2,7,11,15" style="width: 300px;">
            </p>
            <p>
                <label>Целевая сумма:</label><br>
                <input type="number" id="target" placeholder="9">
            </p>
            <button type="submit">🚀 Тест!</button>
        </form>

        <div id="result"></div>

        <h3>📋 Готовые тесты:</h3>
        <button onclick="runTest([2,7,11,15], 9)">Тест 1: [2,7,11,15], target=9</button><br>
        <button onclick="runTest([1,2,3,4], 8)">Тест 2: [1,2,3,4], target=8</button><br>
        <button onclick="runTest([0,0,0,0], 0)">Тест 3: [0,0,0,0], target=0</button><br>
    </div>

    <script>
        document.getElementById('testForm').onsubmit = function(e) {
            e.preventDefault();
            const arrayStr = document.getElementById('array').value;
            const target = parseInt(document.getElementById('target').value);
            
            try {
                const array = arrayStr.split(',').map(x => parseInt(x.trim()));
                runTest(array, target);
            } catch(err) {
                showResult('Ошибка в формате данных!', false);
            }
        };

        function runTest(array, target) {
            fetch('/test', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({array: array, target: target})
            })
            .then(response => response.json())
            .then(data => {
                showResult(`
                    <strong>Массив:</strong> [${array.join(', ')}]<br>
                    <strong>Цель:</strong> ${target}<br>
                    <strong>Результат:</strong> ${data.result}<br>
                    <strong>Объяснение:</strong> ${data.explanation}
                `, data.success);
            });
        }

        function showResult(html, success) {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = html;
            resultDiv.className = 'result ' + (success ? 'success' : 'error');
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/test', methods=['POST'])
def test_function():
    data = request.get_json()
    array = data['array']
    target = data['target']
    
    result = find_sums(array, target)
    
    if result is None:
        explanation = "Нет пары чисел, дающих нужную сумму"
        success = True  # Это нормальный результат
    else:
        idx1, idx2 = result
        explanation = f"array[{idx1}] + array[{idx2}] = {array[idx1]} + {array[idx2]} = {array[idx1] + array[idx2]}"
        success = True
    
    return jsonify({
        'result': str(result),
        'explanation': explanation,
        'success': success
    })

if __name__ == '__main__':
    print("🌐 Открой браузер: http://localhost:5000")
    app.run(debug=True, port=5000)