from flask import Flask

app = Flask(__name__)


@app.route('/blog/<postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


if __name__ == '__main__':
    app.run()
