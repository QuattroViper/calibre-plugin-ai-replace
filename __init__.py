from calibre.customize import InterfaceActionBase


class AiReplacerPlugin(InterfaceActionBase):
    name = 'AI Context Replacer'
    description = 'Minimally removes or change exclamations while preserving formatting'
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Marno van Niekerk'
    version = (0, 3, 0)
    minimum_calibre_version = (6, 0, 0)

    actual_plugin = 'main:AiReplaceAction'
