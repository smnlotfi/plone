# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import vollabor.project


class VollaborProjectLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=vollabor.project)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'vollabor.project:default')


VOLLABOR_PROJECT_FIXTURE = VollaborProjectLayer()


VOLLABOR_PROJECT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLLABOR_PROJECT_FIXTURE,),
    name='VollaborProjectLayer:IntegrationTesting',
)


VOLLABOR_PROJECT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLLABOR_PROJECT_FIXTURE,),
    name='VollaborProjectLayer:FunctionalTesting',
)


VOLLABOR_PROJECT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        VOLLABOR_PROJECT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='VollaborProjectLayer:AcceptanceTesting',
)
