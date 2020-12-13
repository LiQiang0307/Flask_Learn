from flask import Flask,redirect,render_template,request,jsonify,make_response
app=Flask(__name__)

@app.route('/index',methods=['GET','POST'])
def index():
    #请求相关
    # request.method
    # request.args
    # request.form
    # request.values
    # request.cookies
    # request.headers
    # request.path
    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host
    # request.files
    # obj=request.files['the_file_name']
    # obj.save('/var/wwww/uploads/'+secure_filename(f.filename))

    #响应相关
    return " "
    # return json.dumps({})
    # return jsonify({})
    # return render_template('index.html',nl=123)
    # return redirect('/index')

    # response=make_response(render_template('index.html'))
    # #response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key')
    # response.headers['X-something']='A value'
    # return response

if __name__ == '__main__':
    app.run()