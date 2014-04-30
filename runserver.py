from seedfoodstudywebservice import app
app.run(host=os.environ['OPENSHIFT_PYTHON_IP'],port=int(os.environ['OPENSHIFT_PYTHON_PORT']),debug='true')