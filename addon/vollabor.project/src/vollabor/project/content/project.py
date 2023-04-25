from plone import schema
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class IProject(model.Schema):
    """Dexterity-Schema for Talks"""

    # directives.widget(type_of_talk=RadioFieldWidget)
    # type_of_talk = schema.Choice(
    #     title='Type of talk',
    #     values=['Talk', 'Training', 'Keynote'],
    #     required=True,
    # )

    # details = RichText(
    #     title='Details',
    #     description='Description of the talk (max. 2000 characters)',
    #     max_length=2000,
    #     required=True,
    # )

    # directives.widget(audience=CheckBoxFieldWidget)
    # audience = schema.Set(
    #     title='Audience',
    #     value_type=schema.Choice(
    #         values=['Beginner', 'Advanced', 'Professional'],
    #     ),
    #     required=False,
    # )

    image = NamedBlobImage(
        title='Image',
        description='Portrait of the speaker',
        required=False,
    )

    supervisor = schema.TextLine(
        title='Supervisor',
        description='Name (or names) of the supervisor',
        required=True,
    )

    fund = schema.TextLine(
        title='Fund',
        required=True,
    )

    skills = schema.TextLine(
        title='Skills',
        required=True,
    )

    requirments = schema.TextLine(
        title='Requirments',
        required=True,
    )

    desc = RichText(
        title='Description',
        description='Description of the talk (max. 2000 characters)',
        max_length=2000,
        required=True,
    )

    # email = Email(
    #     title='Email',
    #     description='Email adress of the speaker',
    #     required=False,
    # )

    # website = schema.TextLine(
    #     title='Website',
    #     required=False,
    # )

    # twitter = schema.TextLine(
    #     title='Twitter name',
    #     required=False,
    # )

    # github = schema.TextLine(
    #     title='Github username',
    #     required=False,
    # )

    # image = NamedBlobImage(
    #     title='Image',
    #     description='Portrait of the speaker',
    #     required=False,
    # )

    # speaker_biography = RichText(
    #     title='Speaker Biography (max. 1000 characters)',
    #     max_length=1000,
    #     required=False,
    # )


@implementer(IProject)
class Project(Container):
    """Talk instance class"""

