from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
#from zope.interface import alsoProvides
#from plone.directives import form
from plone.supermodel import model
#from z3c.form.browser.checkbox import CheckBoxFieldWidget

_ = MessageFactory('medialog.controlpanel')

class IMedialogControlpanelSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """

class IMedialogControlpanelSettings(model.Schema):
    """Medialog Controlpanel schema.
    """


    