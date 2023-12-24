from flask import Flask, render_template, request, g, session
from flask_babel import Babel, gettext as _, refresh

app = Flask(__name__, template_folder='src/templates')
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'src/translations'
app.config['BABEL_DEFAULT_LOCALE'] = 'uk'
app.config['SECRET_KEY'] = 'dlfkhsdkfghskdjf387589354oiftgrkdfhgfiew'

def get_locale():
    return g.get('locale', app.config['BABEL_DEFAULT_LOCALE'])


babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_locale():
    return dict(get_locale=lambda: g.get('locale', 'uk'))


@app.before_request
def before_request():
    if 'lang' in request.args:
        session['locale'] = request.args.get('lang')
    g.locale = session.get('locale', app.config['BABEL_DEFAULT_LOCALE'])
    refresh()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/offend')
def offend_artist():
    return render_template('successful_offended.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')

