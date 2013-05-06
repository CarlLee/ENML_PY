ENML_PY
=======

This is a python library for converting ENML (Evernote Markup Language, http://dev.evernote.com/start/core/enml.php) to/from HTML.

Dependencies
=======
- [BeautifulSoup 4 (a.k.a. bs4)](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [Evernote SDK for python](http://dev.evernote.com/start/guides/python.php)

Usage
=======
Convert with prettifying
-----
```python
>>> import ENML_PY as enml
>>> note = "<en-note>hello world</en-note>"
>>> html = enml.ENMLToHTML(note)
>>> print html
<html>
 <body>
   hello world
 </body>
</html>
```

Convert without prettifying
-----

```python
>>> import ENML_PY as enml
>>> note = "<en-note>hello world</en-note>"
>>> html = enml.ENMLToHTML(note, pretty=False)
>>> print html
<html><body>hello world</body></html>
```

Convert with saving resources
-----

```python
>>> client = EvernoteClient(token=dev_token)
>>> noteStore = client.get_note_store()
>>> mediaStore = enml.FileMediaStore(noteStore, note.guid, 'resources/')
>>> content = noteStore.getNoteContent(note.guid)
>>> html = enml.ENMLToHTML(content, False, media_store=mediaStore)
```

This will convert ENML to HTML, and save all the resource files related to the note in 'resources/' path, and replace all media inserted in ENML with according HTML tags with link pointing to the resource with 'file://' protocol.

Write your own MediaStore
-----

``` python
from ENML_PY import MediaStore, MIME_TO_EXTENSION_MAPPING
class MyMediaStore(MediaStore):
    def __init__ (self, note_store, note_guid):
        super(MyMediaStore, self).__init__(note_store, note_guid)

    def save(self, hash_str, mime_type):
        # hash_str is the hash digest string of the resource file
        # mime_type is the mime_type of the resource that is about to be saved
        # you can get the mime type to file extension mapping by accessing the dict MIME_TO_EXTENSION_MAPPING

        # retrieve the binary data
        data = self._get_resource_by_hash(hash_str)
        # some saving operation
        ...
        # return the URL of the resource that has just been saved
        return some_url
```

TODO
======
- Map other media types to the corresponding HTML tags (Only Image tag currently)
- Convert from HTML to ENML
