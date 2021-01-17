{% if cookiecutter.molecule_driver == 'docker' %}
********************************
Docker driver installation guide
********************************

Requirements
============

* Docker Engine

Install
=======

Please refer to the `Virtual environment`_ documentation for installation best
practices. If not using a virtual environment, please consider passing the
widely recommended `'--user' flag`_ when invoking ``pip``.

.. _Virtual environment: https://virtualenv.pypa.io/en/latest/
.. _'--user' flag: https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site

.. code-block:: bash

    $ pip install 'molecule[docker]'
{% else %}
***********************************
Delegated driver installation guide
***********************************

Requirements
============

This driver is delegated to the developer.  Up to the developer to implement
requirements.

Install
=======

This driver is delegated to the developer.  Up to the developer to implement
requirements.
{% endif %}
