# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from vollabor.project.testing import VOLLABOR_PROJECT_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class ProjectIntegrationTest(unittest.TestCase):

    layer = VOLLABOR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_project_schema(self):
        fti = queryUtility(IDexterityFTI, name='project')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('project')
        self.assertIn(schema_name.lstrip('plone_0_'), schema.getName())

    def test_ct_project_fti(self):
        fti = queryUtility(IDexterityFTI, name='project')
        self.assertTrue(fti)

    def test_ct_project_factory(self):
        fti = queryUtility(IDexterityFTI, name='project')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_project_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='project',
            id='project',
        )


        parent = obj.__parent__
        self.assertIn('project', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('project', parent.objectIds())

    def test_ct_project_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='project')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_project_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='project')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'project_id',
            title='project container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
