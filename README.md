mezzanine_resume
================

Simple resume app for Mezzanine CMS. Experimental.

##Installation

1. Clone this repo
2. ```./manage.py migrate mezzanine_resume``` if you're using south otherwise just ```./manage.py syncdb```
3. Add ```python ("^", include("mezzanine_resume.urls")), ``` in ``` urls.py```, above ```python ("^", include("mezzanine.urls")), ```

Create a resume and check ``` /resume/<username> ```

Has not been extensively tested, be warned.
