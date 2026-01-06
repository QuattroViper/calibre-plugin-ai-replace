from calibre.customize import InterfaceActionBase


class AiReplacerPlugin(InterfaceActionBase):
    name = 'AI Context Replacer'
    description = 'Minimally removes or change context while preserving formatting'
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Marno van Niekerk'
    version = (0, 3, 0)
    minimum_calibre_version = (6, 0, 0)
    file_types = {'epub'}
    on_postprocess = False  # Run this plugin after conversion is complete

    #: This field defines the GUI plugin class that contains all the code
    #: that actually does something. Its format is module_path:class_name
    #: The specified class must be defined in the specified module.
    actual_plugin = 'calibre_plugins.ai_context_replace.action:AiContextReplaceAction'

    def is_customizable(self):
        '''
        This method must return True to enable customization via
        Preferences->Plugins
        '''
        return False
