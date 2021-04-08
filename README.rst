======================
Django Profanity Check
======================

``django-profanity-check`` is a re-usable app adapted from ``profanity-filter`` python module.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_profanity_check',
    ]

2. Include the ``django-profanity-check`` Config in your project settings like this::

    ```
    TEMPLATES = [
        ...
        'OPTIONS': {
            'context_processors': [
            ],
            'libraries': {
                'profanity_check': 'django_profanity_check.profanity_tags.profanity_check',

            }
        }
    ]
    ```
    

3. Load the tag in the tag in your django templates using ``{% load profanity_check %}``. 

4. Use the tag to filter words from your models and user inputs like this::

    {{ "you profanity words" | word_filter }}
    
    Note that the above is filtering hard coded words
    The django-profanity-check can also fiter words from the models and user inputs as so::
    {{ context_word_from_views | word_filter }}

5. This filter is a great tool for filtering profane words automatically in articles, comments and other user influenced components in your app!

