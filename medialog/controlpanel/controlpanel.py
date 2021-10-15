from zope.i18nmessageid import MessageFactory
from plone.app.registry.browser import controlpanel
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from medialog.controlpanel.interfaces import IMedialogControlpanelSettings
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.dottedname.resolve import resolve
from zope.interface import alsoProvides

_ = MessageFactory('medialog.controlpanel')


class ContextProxy(object):

    def __init__(self, interfaces):
        self.__interfaces = interfaces
        alsoProvides(self, *interfaces)

    def __setattr__(self, name, value):
        if name.startswith('__') or name.startswith('_ContextProxy__'):
            return object.__setattr__(self, name, value)

        registry = getUtility(IRegistry)
        for interface in self.__interfaces:
            proxy = registry.forInterface(interface)
            try:
                getattr(proxy, name)
            except AttributeError:
                pass
            else:
                return setattr(proxy, name, value)
        raise AttributeError(name)

    def __getattr__(self, name):
        if name.startswith('__') or name.startswith('_ContextProxy__'):
            return object.__getattr__(self, name)

        registry = getUtility(IRegistry)
        for interface in self.__interfaces:
            proxy = registry.forInterface(interface)
            try:
                return getattr(proxy, name)
            except AttributeError:
                pass

        raise AttributeError(name)


class MedialogControlpanelSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IMedialogControlpanelSettings
    label = _(u"Add-ons Controlpanel")
    description = _(u"")

    def getContent(self):
        interfaces = [self.schema]
        interfaces.extend(self.additionalSchemata)
        return ContextProxy(interfaces)

    @property
    def additionalSchemata(self):
        registry = getUtility(IRegistry)
        interface_names = set(record.interfaceName for record
                              in registry.records.values())

        for name in interface_names:

            if not name:
                continue

            #if not name.startswith('medialog'):
            #    continue

            interface = resolve(name)
            if IMedialogControlpanelSettingsProvider.providedBy(interface):
                yield interface


    def updateFields(self):
        super(MedialogControlpanelSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(MedialogControlpanelSettingsEditForm, self).updateWidgets()


class MedialogControlPanel(controlpanel.ControlPanelFormWrapper):
    form = MedialogControlpanelSettingsEditForm
