import htmls
from django.test import TestCase
from django.urls import reverse_lazy
from model_mommy import mommy

from csv_generator.models import User, Schema


class TestSchemasListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
            Create an instances for tests.
            The setUpTestData() allows the creation of initial data at the class level,
            once for the whole TestCase. This technique allows for faster tests as compared to using setUp()
        """
        cls.user = User.objects.create_user('Jhon', 'lennon@thebeatles.com', 'userpassword')
        cls.schemas = mommy.make('csv_generator.Schema', created_by=cls.user, _quantity=8)
        cls.scheme = Schema.objects.create(name='schema')

    def test_schemas_list_view_no_logged_in_user(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/?next=/")

    def test_schemas_list_view_logged_in_user(self):
        mommy.make('csv_generator.Schema', _quantity=20)  # schemas created by another users have not be listed
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schemas/schemas_list.html')
        self.assertEqual(len(response.context['object_list']), 8)

    def test_schemas_pagination_is_10(self):
        mommy.make('csv_generator.Schema', created_by=self.user,
                   _quantity=10)  # Create an instances more than 10 for pagination tests (18 instances)
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get(reverse_lazy('schemas_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['object_list']), 10)

    def test_schemas_pagination_second_page(self):
        mommy.make('csv_generator.Schema', created_by=self.user,
                   _quantity=10)  # Create an instances more than 10 for pagination tests (18 instances)
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get(reverse_lazy('schemas_list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['object_list']), 8)

    def test_new_schema_buttons(self):
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get(reverse_lazy('schemas_list'))
        selector = htmls.S(response.content)
        # selector.prettyprint()
        self.assertEqual(selector.one('.btn.btn-success').text_normalized, 'New schema')

    def test_schema_list_title(self):
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get(reverse_lazy('schemas_list'))
        selector = htmls.S(response.content)
        self.assertEqual(selector.one('.col-auto.mr-auto > h2').text_normalized, 'Data schemas')


    def test_schema_list_table(self):
        self.client.login(username='Jhon', password='userpassword')
        response = self.client.get(reverse_lazy('schemas_list'))
        selector = htmls.S(response.content)
        self.assertEqual(len(selector.list('tbody tr')), 8)
