# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from vollabor.app.testing import VOLLABOR_APP_FUNCTIONAL_TESTING
from vollabor.app.testing import VOLLABOR_APP_INTEGRATION_TESTING
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = VOLLABOR_APP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_my_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='my-view'
        )
        self.assertTrue(view.__name__ == 'my-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in my-view'
        # )

    def test_my_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='my-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = VOLLABOR_APP_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
