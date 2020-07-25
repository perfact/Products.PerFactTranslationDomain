Changelog
=========
2.1 (2020-07-25)
----------------
- Compatibility with Chameleon

  Chameleon tries to translate everything that is not a string or number or
  possesses a ``__html__`` attribute. To regain compatibility, we reject any
  message that is not a string.

  See `Zope#876 <https://github.com/zopefoundation/Zope/issues/876>`_

2.0 (2020-07-02)
----------------
- Compatibility with Zope 4

1.0 (2020-06-30)
----------------

- Initial packaged version
