from django.test import TestCase
from .test_objects.TestAuthor import TestAuthor
from .test_objects.TestBook import TestBook
from .test_objects.TestUser import TestUser
from django.urls import reverse

class BookManagerViews(TestCase):
    def setUp(self):
        self.testUser = TestUser()
        self.testAuthor = TestAuthor()
        self.testBook = TestBook()

    def login_user(self):
        self.client.login(username=self.testUser.username, password=self.testUser.password)

    def check_template_use_base(self, response):
        self.assertTemplateUsed(response, 'base.html')

    def test_loggin_view(self):
        response = self.client.get(reverse('login'))