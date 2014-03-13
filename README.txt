Project Description
===================

This product is a pluggable control panel.

The idea behind it is the following.

- You want a control panel for your settings.
- You don't want to make new control panels all the time.
- You want all your settings to be in the same control panel
- You want tabs in your control panel.



How to use it
--------------

- install medialog.controlpanel (or add it as a dependecy in your product)
- then do the following in your own product

In a py-file (interfaces.py maybe):

------------------------------------

from z3c.form import interfaces
from zope import schema
#from zope.interface import Interface
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('your.product')
                                  
class IMyProductSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'myproductname',
        label=_(u'name of My Settings'),
        fields=[
            'my_field',
            ],
        )

    my_field = schema.TextLine(
        title=_(u"label_my_field", default=u"My Field"),
        description=_(u"help_my_field",
                      default=u"My description")
        )

alsoProvides(IMyProductSettings, IMedialogControlpanelSettingsProvider)

---------------------------------------------------------------------------

In your products profile:

Add a registry.xml field with the following content:

---------------------------------------------------------------------------

<?xml version="1.0"?>

<registry>
 <records interface="my.product.interfaces.IMyProductSettings">
      <value key="my_field"></value>
 </records>
</registry>


Of course, change MyProduct / my_field to your own names.

Author:
*******
Espen Moe-Nilssen [espenmn]

Some of the code is stolen (shamelessly) from Bluedynamics and Nathan van Gheem.

PS: zedr also wanted to be mentioned.