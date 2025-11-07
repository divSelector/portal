# portal.goeshard.org

[Enter the Portal](https://portal.goeshard.org)

> The philosophy of this site is based around how my favorite link sites tell me in their own words where they're sending me with a brief line of text. ... It's ... based around the idea that I think a lot of people today think a links page is about collecting buttons and showing off their collection, which there is nothing wrong with that. But... a proper links page for me is a list of links with a description of what it is. I can't speak for everyone, but I'm personally very unlikely to click on a link because of a button, but a written statement of what it is on the other side will make me interested. This is something of a new philosophy for me as I only recently came to this realization when browsing other peoples links pages and thinking, "This is how it should be done." I was inspired to do my own.

---

This is a django project that uses the plugin [django-distill](https://django-distill.com/) to output a static site.

## `core` folder

Very stripped down Django project folder. You can see that the [settings.py](src/core/settings.py) file is also stripped down and has almost nothing that a normal Django app would require because there is no backend. All the security concerns there are unnecessary to worry about for the same reason.

## `render` folder

This is [where the tree is generated from templates](src/render/templates/render) and the [simple static frontend](src/render/static/render) resides.

There are some templatetags that are used in [tree_extras.py](src/render/templatetags/tree_extras.py)

## `links` folder

I use the functions in [helpers.py](src/links/helpers.py) to get [the links data](src/links/data/__init__.py) into a nice dict format to pass to [the view](src/render/views.py) to pass to the render templates (see above).

If you look into the `links.data` module you'll find submodules which contain the actual link data. For example here is where the [music section](src/links/data/music.py) and its subsections are created.