from flask import Flask, render_template_string, request

app = Flask(__name__)

# 首页
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>问卷系统</title>
    </head>
    <body style="text-align:center; margin-top:50px;">
        <h1>欢迎使用在线问卷</h1>
        <a href="/form"><button style="padding:10px 20px;">填写问卷</button></a>
        <a href="/admin"><button style="padding:10px 20px;">查看结果</button></a>
    </body>
    </html>
    """

# 问卷表单
@app.route('/form')
def form():
    return render_template_string('''
        <h1>请填写问卷</h1>
        <form action="/submit" method="POST" style="max-width:300px; margin:auto;">
            姓名：<input name="name" required><br><br>
            年龄：<input name="age" required><br><br>
            满意度：
            <select name="satisfy">
                <option>非常满意</option>
                <option>满意</option>
                <option>一般</option>
            </select><br><br>
            <button type="submit">提交</button>
        </form>
    ''')

# 提交并保存数据
@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单数据
    name = request.form.get('name')
    age = request.form.get('age')
    satisfy = request.form.get('satisfy')

    # 保存到文件 data.txt
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(f'姓名：{name}，年龄：{age}，满意度：{satisfy}\n')

    return "<h1>提交成功！</h1><a href='/'>返回首页</a>"

# 后台查看所有数据
@app.route('/admin')
def admin():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            data = f.read().replace('\n', '<br>')
    except:
        data = "暂无数据"

    return f"<h1>问卷结果</h1><div>{data}</div><br><a href='/'>返回</a>"

if __name__ == '__main__':
    app.run(debug=True)