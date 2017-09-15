from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client, RequestFactory
from myauth.models import MyUser
from myauth.views import validate_email
from django.core.urlresolvers import reverse
import uuid
from django.contrib.sessions.middleware import SessionMiddleware

class MyUserAuthTest(TestCase):
    def setUp(self):
        """Create only a simple user
        """
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
            email='test@test.com', password='1234qwer')

    def test_hash_true_return(self):
        """Test if the page, with data ok, redirects to the right page
        """
        client = Client()
        response = client.get(
            reverse('myauth:validate_email',
            kwargs={'id': self.user.id, 'hash': self.user.confirmation_key})
        )
        expected_url = reverse('home:home')
        self.assertRedirects(
            response,
            expected_url,
            status_code=302,
            target_status_code=200,
            msg_prefix='',
            fetch_redirect_response=True
        )

    def test_hash_false_return(self):
        """Test if the page, with wrong data, redirects to the right page
        """
        client = Client()
        response = client.get(
            reverse('myauth:validate_email',
            kwargs={'id': self.user.id, 'hash': uuid.uuid4()})
        )
        expected_url = reverse('myauth:send_confirmation')
        self.assertRedirects(
            response,
            expected_url,
            status_code=302,
            target_status_code=200,
            msg_prefix='',
            fetch_redirect_response=True
        )

    def test_id_false_return(self):
        """Test if the page, with wrong data, redirects to the right page
        """
        client = Client()
        response = client.get(
            reverse('myauth:validate_email',
            kwargs={'id': self.user.id+10, 'hash': self.user.confirmation_key})
        )
        expected_url = reverse('myauth:send_confirmation')
        self.assertRedirects(
            response,
            expected_url,
            status_code=302,
            target_status_code=200,
            msg_prefix='',
            fetch_redirect_response=True
        )

    def test_hash_true(self):
        """Test if the user's email will be confirmed by the proper id and hash
        """
        request = self.factory.get(reverse('myauth:validate_email',
            kwargs={'id': self.user.id, 'hash': self.user.confirmation_key}))
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        response = validate_email(request, self.user.id,
                                    self.user.confirmation_key_str())
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_confirmed)

    def test_hash_false(self):
        """Test if the site rejects wrong hash to the proper id of the user
        """
        request = self.factory.get(reverse('myauth:validate_email',
            kwargs={'id': self.user.id, 'hash': uuid.uuid4()}))
        response = validate_email(request, self.user.id, uuid.uuid4())
        self.assertFalse(self.user.is_confirmed)

    def test_send_confirmation_get_200(self):
        """Test if the get is returning status 200
        """
        client = Client()
        response = client.get(reverse('myauth:send_confirmation'))
        self.assertEqual(response.status_code, 200)

    def test_send_confirmation_post_200(self):
        """Test if the get is returning status 200
        """
        client = Client()
        response = client.post(reverse('myauth:send_confirmation'),
                                {'email': self.user.email})
        self.assertEqual(response.status_code, 200)

