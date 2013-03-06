from django.test import TestCase
from with_asserts.case import TestCase as HTMLTestCase
from with_asserts.mixin import AssertHTMLMixin

import lxml.html


class AssertHTMLMixinTest(TestCase, AssertHTMLMixin):
    def test_document(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp) as html:
            self.assertIsInstance(html, lxml.html.HtmlElement)
            self.assertEqual('Selector Test', html.find('head/title').text)

    def test_selector_class(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp, '.product') as elems:
            self.assertEqual(2, len(elems))
            self.assertEqual('Subpage 3', elems[0].text)
            self.assertEqual('Subpage 4', elems[1].text)

    def test_destructuring(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp, '.product') as (li1, li2):
            self.assertEqual('Subpage 3', li1.text)
            self.assertEqual('Subpage 4', li2.text)

    def test_selector_id(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp, '#example-div') as (elem,):
            self.assertIsInstance(elem, lxml.html.HtmlElement)

            self.assertEqual('Example Div By ID', elem.text)

    def test_selector_attribute(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp, 'input[name="email"]') as (elem,):
            self.assertEqual('test@example.com', elem.value)

    def test_selector_not_present(self):
        resp = self.client.get('/template/selectors/')

        with self.assertRaises(AssertionError) as cm:
            with self.assertHTML(resp, '.not-real'):
                # should not be executed
                raise Exception()

        self.assertEqual(
            'No selector matches found for .not-real',
            str(cm.exception)
        )

    def test_element_id(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp, element_id='example-div') as elem:
            self.assertEqual('Example Div By ID', elem.text)

    def test_element_id_not_present(self):
        resp = self.client.get('/template/selectors/')

        with self.assertRaises(AssertionError) as cm:
            with self.assertHTML(resp, element_id='not-real'):
                # should not be executed
                raise Exception()

        self.assertEqual(
            'Element with id, not-real, not present',
            str(cm.exception)
        )

    def test_404_not_found(self):
        resp = self.client.post('/404/')

        with self.assertRaises(AssertionError):
            # should through exception because of 404 status code
            with self.assertHTML(resp):
                # should not be executed (self.fail() would cause an
                # AssertionError, which would confuse what we are testing
                raise Exception()

    def test_404_status_code(self):
        resp = self.client.post('/404/')

        with self.assertHTML(resp, status_code=404):
            return

        # should have returned by now
        self.fail()

    # def test_expected_attrs(self):
    #     resp = self.client.get('/template/selectors/')

    #     self.assertHTML(resp, 'input[name="email"]', expected_attrs={
    #     })


class AssertNotHTMLTest(TestCase, AssertHTMLMixin):
    def test_not_present(self):
        resp = self.client.get('/template/selectors/')

        self.assertNotHTML(resp, '.not-real')

    def test_present(self):
        resp = self.client.get('/template/selectors/')

        with self.assertRaises(AssertionError):
            self.assertNotHTML(resp, '.product')

    def test_404_not_found(self):
        # still expect a valid status
        resp = self.client.post('/404/')

        with self.assertRaises(AssertionError) as cm:
            # should through exception because of 404 status code
            self.assertNotHTML(resp, '.product')

        self.assertEqual('404 != 200', str(cm.exception))


class HTMLTestCaseTest(HTMLTestCase):
    def test_django_subclass(self):
        resp = self.client.get('/template/selectors/')

        # would not be present if not Django
        self.assertContains(resp, 'Selector Test')

    def test_assert_not_html(self):
        resp = self.client.get('/template/selectors/')

        self.assertNotHTML(resp, '.not-real')

    def test_assert_html(self):
        resp = self.client.get('/template/selectors/')

        with self.assertHTML(resp) as html:
            self.assertIsInstance(html, lxml.html.HtmlElement)
            self.assertEqual('Selector Test', html.find('head/title').text)

# TODO:
# expected_tag
# expected_attrs
