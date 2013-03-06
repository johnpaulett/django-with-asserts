django-with-asserts - Test HTML with Context Managers
=====================================================

Make your Django HTML tests more explicit and concise.

Turn this::

    self.assertContains(
        resp,
        '<input id="id_email" type="text" name="email" maxlength="75" value="bob@example.com>',
        html=True
    )

Into this::

    with self.assertHTML(resp, 'input[name="email"]') as (elem,):
        self.assertEqual(elem.value, 'bob@example.com')


Links
------

 * Documentation: https://django-with-asserts.readthedocs.org
 * Code: https://github.com/johnpaulett/django-with-asserts


