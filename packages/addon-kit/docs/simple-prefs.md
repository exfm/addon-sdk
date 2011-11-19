<!-- contributed by Erik Vold [erikvvold@gmail.com]  -->

The `simple-prefs` module lets you easily and persistently store preferences
across application restarts, using the Mozilla preferences system.  These
preferences will be configurable by the user in [about:addons](about:addons) and
in [about:config](about:config).

Introduction
------------

With the simple preferences module you can store booleans, integers, and string
values.


Inline Options & Default Values
-------------------------------

In order to have a `options.xul` (for inline options) generated, or a
`defaults/preferences/prefs.js` for default preferences, you will need to
define the preferences in your `package.json`, like so:

    {
        "preferences": {
            "prefName": {
                "title": "Some preference title",
                "type": "string",
                "value": "this is the default string value"
            }
        }
    }


<api name="prefs">
@property {object}
  A persistent object private to your add-on.  Properties with boolean,
  number, and string values will be persisted in the Mozilla preferences system.
</api>
