from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import alsoProvides
from plone.directives import form
#from z3c.form.browser.checkbox import CheckBoxFieldWidget


_ = MessageFactory('medialog.controlpanel')



class IMedialogControlpanelSettingsProvider(Interface):
    """A marker interface for plone.registry configuration interfaces
    """


class IMedialogControlpanelSettings(form.Schema):
    """MedialogControlpanel controlpanel schema.
    """

    test_field= schema.ASCIILine(
        title=_(u"label_admin_email", default=u'Test field'),
       description=_(u"help_admin_email",
                      default=u'No typos please....'),
        required=True,
        default="")

    