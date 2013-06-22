from logilab.astng import MANAGER
from logilab.astng.builder import ASTNGBuilder

def fake_i18n(module):

    if module.name == 'django.utils.translation':

        fake = ASTNGBuilder(MANAGER).string_build('''
def ugettext_lazy(value):
    return u''

def ugettext(value):
    return u''
'''
        )

        for hashfunc in ('ugettext_lazy', 'ugettext'):
            module.locals[hashfunc] = fake.locals[hashfunc]

def register(linter):
    MANAGER.register_transformer(fake_i18n)
