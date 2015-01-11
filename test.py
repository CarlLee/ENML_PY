#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from evernote.api.client import EvernoteClient, NoteStore, UserStore
import __init__ as enml

class MediaStoreStub(object):
    def save(self, hash_str, mime_type):
        return hash_str

class FileMediaStoreTest(unittest.TestCase):
    def setUp(self):
        self.dev_token = 'S=s1:U=677e1:E=145b2a35937:C=13e5af22d3a:P=1cd:A=en-devtoken:V=2:H=c45724de45678421495b2b93bfac8033'
        self.client = EvernoteClient(token=dev_token)
        self.noteStore = client.get_note_store()
        self.notebooks = noteStore.listNotebooks()

    def test_file_media_store(self):
        for notebook in notebooks:
            print "Notebook: %s" % notebook.name
            nfilter = NoteStore.NoteFilter(notebookGuid=notebook.guid)
            notes = noteStore.findNotes(nfilter, 0, 200)
            for note in notes.notes:
                print "└─%s" % note.title
                print "guid:%s"  % note.guid
                mediaStore = enml.FileMediaStore(noteStore, note.guid, 'resources/')
                content = noteStore.getNoteContent(note.guid)
                print content
                html = enml.ENMLToHTML(content, False, media_store=mediaStore)
                f = open(note.title + '.html', 'w')
                f.write(html)
                f.flush()
                f.close()


class MediaFilter(unittest.TestCase):
    def test_filter(self):
        enml_note = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
Header text
<div>
<en-note style="background: #e6e6e6;font-family: 'Helvetica Neue',  Helvetica, Arial, 'Liberation Sans', FreeSans, sans-serif;color: #585957;font-size: 14px;line-height: 1.3;">
<en-media alt="Evernote Peek" type="image/png" hash="950bf3517b1e7f23bc40066853a23f7e" style="position:absolute;top:0;left:0;border-color:transparent;"></en-media>
<en-media alt="Evernote Peek" type="application/pdf" hash="SHOULD BE FILTERED" style="position:absolute;top:0;left:0;border-color:transparent;"></en-media>
Footer text
</div>
</en-note>
"""
        expected_html = """<html><body style="background: #e6e6e6;font-family: 'Helvetica Neue',  Helvetica, Arial, 'Liberation Sans', FreeSans, sans-serif;color: #585957;font-size: 14px;line-height: 1.3;">
<img src="950bf3517b1e7f23bc40066853a23f7e"/>

Footer text
</body></html>"""
        html_note = enml.ENMLToHTML(
            enml_note,
            False,
            media_store=MediaStoreStub(),
            media_filter=enml.images_media_filter
        )
        self.assertEqual(expected_html, html_note)

if __name__ == '__main__':
    unittest.main()
