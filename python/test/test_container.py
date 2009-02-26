# -*- coding: UTF-8 -*-
# Copyright (C) 2009 Itaapy, ArsAperta, Pierlis, Talend

# Import from the Standard Library
import unittest
from unittest import TestCase

# Import from itools
from itools.xml import XML_DECL, START_ELEMENT

# Import from lpod
from lpod.container import new_odf_container, get_odf_container
from lpod.container import ODF_EXTENSIONS


class NewContainerTestCase(TestCase):

    def test_no_parameters(self):
        self.assertRaises(ValueError, new_odf_container)


    def test_bad_class(self):
        self.assertRaises(ValueError, new_odf_container, odf_class='foobar')


    def test_all_parameters(self):
        self.assertRaises(ValueError, new_odf_container, odf_class='text',
                          template_uri='templates/text.ott')


    def test_text_template(self):
        new_odf_container(odf_class='text')


    def test_spreadsheet_template(self):
        new_odf_container(odf_class='spreadsheet')


    def test_presentation_template(self):
        new_odf_container(odf_class='presentation')


    def test_drawing_template(self):
        new_odf_container(odf_class='drawing')



class GetContainerTestCase(TestCase):

    def test_filesystem(self):
        path = 'samples/example.odt'
        container = get_odf_container(path)


    def test_odf_xml(self):
        path = 'samples/example.xml'
        container = get_odf_container(path)


    def test_http(self):
        uri = 'http://test.lpod-project.org/example.odt'
        container = get_odf_container(uri)


    def test_ftp(self):
        uri = 'ftp://test.lpod-project.org/example.odt'
        container = get_odf_container(uri)



class ContainerTestCase(TestCase):

    def test_clone(self):
        container = new_odf_container(odf_class='text')
        clone = container.clone()
        self.assertEqual(clone.uri, None)


    def test_get_part_xml(self):
        container = get_odf_container('samples/example.odt')
        content = container.get_part('content')
        xml_decl = '<?xml version="1.0" encoding="UTF-8"?>'
        self.assert_(content.startswith(xml_decl))


    def test_get_part_mimetype(self):
        container = get_odf_container('samples/example.odt')
        mimetype = container.get_part('mimetype')
        self.assertEqual(mimetype, ODF_EXTENSIONS['odt'])


    def test_odf_xml_bad_part(self):
        container = get_odf_container('samples/example.xml')
        self.assertRaises(ValueError, container.get_part, 'Pictures/a.jpg')


    def test_odf_xml_part_xml(self):
        container = get_odf_container('samples/example.xml')
        meta = container.get_part('meta')
        self.assert_(meta.startswith('<office:document-meta>'))
