from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮のデータベース
pc_data = []

# トップページをダッシュボードにリダイレクト
@app.route('/')
def index():
    return redirect(url_for('dashboard'))

# ダッシュボード
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', pc_data=pc_data)

# 新規登録
@app.route('/new_registration', methods=['GET', 'POST'])
def new_registration():
    if request.method == 'POST':
        project_name = request.form['project_name']
        lend_date = request.form['lend_date']
        return_date = request.form['return_date']
        pc_number = request.form['pc_number']
        pc_data.append({
            'project_name': project_name,
            'lend_date': lend_date,
            'return_date': return_date,
            'pc_number': pc_number,
            'status': '未着手'
        })
        return redirect(url_for('dashboard'))
    return render_template('new_registration.html')

# 編集・更新
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        pc_data[index]['project_name'] = request.form['project_name']
        pc_data[index]['lend_date'] = request.form['lend_date']
        pc_data[index]['return_date'] = request.form['return_date']
        pc_data[index]['status'] = request.form['status']
        return redirect(url_for('dashboard'))
    return render_template('edit.html', pc=pc_data[index])

if __name__ == '__main__':
    app.run(debug=True)
