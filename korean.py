# -*- coding: utf8 -*-
import time
import os
import lucene

def get_word_list(text, is_list=False, field_name = 'fieldname'):
    if is_list:
        new_text = ""
        for i in text:
            new_text += i + "\n"
        text = new_text

    lucene.initVM(lucene.CLASSPATH)
    analyzer = lucene.KoreanAnalyzer();

    #directory = lucene.FSDirectory.open("/tmp/testindex");
    directory = lucene.RAMDirectory()

    # writer
    writer = lucene.IndexWriter(directory, analyzer)
    doc = lucene.Document()

    doc.add(lucene.Field(field_name, text, lucene.Field.Store.YES, lucene.Field.Index.ANALYZED));
    writer.addDocument(doc);
    writer.close();

    # get all terms from all index
    ireader = lucene.IndexReader.open(directory, False)
    term = lucene.Term(field_name, '')
    termenum = ireader.terms(term)
    term = termenum.term()
    i = 0

    word_list = []

    while term and term.field() == field_name:
        i += 1
        termDocs = ireader.termDocs(term)
        termDocs.next()
        #print "[%04d]===> <%s> " % (i, term.text())
        #print term.text() + " : " + str(termDocs.freq())
        word_list.append({'text': term.text(), 'freq': termDocs.freq()})
        term = termenum.next() and termenum.term()

    ireader.close();
    directory.close();

    return word_list
