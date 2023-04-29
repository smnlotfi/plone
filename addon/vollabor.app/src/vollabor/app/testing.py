# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import vollabor.app


class VollaborAppLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=vollabor.app)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'vollabor.app:default')


VOLLABOR_APP_FIXTURE = VollaborAppLayer()


VOLLABOR_APP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLLABOR_APP_FIXTURE,),
    name='VollaborAppLayer:IntegrationTesting',
)


VOLLABOR_APP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLLABOR_APP_FIXTURE,),
    name='VollaborAppLayer:FunctionalTesting',
)


VOLLABOR_APP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        VOLLABOR_APP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='VollaborAppLayer:AcceptanceTesting',
)
