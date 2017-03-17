import webapp2

from webapp2_extras import i18n
import os

import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.install_gettext_translations(i18n)

class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        locale = self.request.GET.get('locale', 'en_US')
        i18n.get_i18n().set_locale(locale)
        print(locale)

        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', HelloWorldHandler),
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
