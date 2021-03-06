Pylint Plugin
=============

A plugin make Pylint more Django-Friendly.

NOTICE: Django 1.4+ has solved the i18n problem like "_ is not callable".

install
-------

python setup.py install

usage
-----

1. save as example.py

<pre><code>
from django.utils.translation import ugettext_lazy as _

print _('damn it!')
</code></pre>

2. run pure pylint

$ pylint -E example.py

<pre><code>
No config file found, using default configuration
************* Module example
E:  3,6: _ is not callable
</code></pre>

3. run pylint with plugin

$ pylint -E --load-plugins=PylintPlugin.astng_django example.py

<pre><code>
No config file found, using default configuration
</code></pre>
