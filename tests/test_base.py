from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        target_url = url_for('index')
        redirect_url = url_for('hello')

        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_hello_get(self):
        target_url = url_for('hello')
        response = self.client.get(target_url)
        self.assert200(response)

    def test_hello_post(self):
        target_url = url_for('hello')
        fake_form = {
            "username": 'fake',
            "password": "fake-password"
        }
        response = self.client.post(target_url, data=fake_form)
        self.assertRedirects(response, target_url)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        target_url = url_for('auth.login')
        response = self.client.get(target_url)
        self.assert200(response)
        
    def test_auth_login_template(self):
        target_url = url_for('auth.login')
        self.client.get(target_url)
        self.assertTemplateUsed('login.html')
