from flask import *
from peewee import *
from init_db import *

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return list()


@app.route('/list', methods=['GET'])
def list():
    return render_template('list.html', stories=Story.select())


@app.route('/story', methods=['GET'])
def add_form():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def add_story():
    Story.create(story_title=request.form["story_title"],
                 user_story=request.form["user_story"],
                 acceptance_criteria=request.form["criteria"],
                 business_value=request.form["business_value"],
                 estimation=request.form["estimation"],
                 status=request.form["status"])
    return redirect(url_for('index'))


@app.route('/story/<story_id>', methods=['GET'])
def load_existing_story(story_id):
    story = Story.select().where(story_id == Story.id).get()
    return render_template('form.html', story=story)


@app.route('/story/<story_id>', methods=['POST'])
def edit_existing_story(story_id):
    story = Story.select().where(story_id == Story.id).get()
    story.story_title = request.form["story_title"]
    story.user_story = request.form["user_story"]
    story.acceptance_criteria = request.form["criteria"]
    story.business_value = request.form["business_value"]
    story.estimation = request.form["estimation"]
    story.status = request.form["status"]
    story.save()
    return redirect(url_for('index'))


@app.route('/delete/<story_id>', methods=['GET'])
def delete(story_id):
    story = Story.select().where(story_id == Story.id).get()
    story.delete_instance()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)