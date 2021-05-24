#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author Mark Li(https://github.com/markbuild)
# Function:Create a basic HTML5 template file
import os
import xml.sax.saxutils
import colorprint

HTML_TEMPLATE= """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>

  <link rel="stylesheet" href="css/styles.css?v=1.0">

  <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
</head>
<link rel="shortcut icon" href="favicon.ico" />
<body>
<h1>{title}</h1>
  <script src="js/scripts.js"></script>
</body>
</html>
"""
def createhtml5():
    information=dict(title=None,filename=None,path=None)
    while True:
        try:
            colorprint.color_print("\n Begin to create a HTML5 file\n",'yellow')
            populate_information(information)
            _create_html_file(**information)
        except ValueError as err:
            colorprint.color_print("Task canceled: %s\n" % err, 'red')
        if(_get_string("\nCreate another one(y/n)?", default = "n").lower() not in {"y","yes"}):
            break

def populate_information(information):
    title = _get_string("Input the title",default="Default title")
    filename = _get_string("Input filename",default="default.html")
    if not filename.endswith((".htm",".html")):
        filename+=".html"
    path = _get_string("Input path",default="C:\\Users\\Mark\\Desktop\\")
    if not path.endswith(("\\")):
        path+="\\"
    if os.path.exists(path+filename):
        raise ValueError("Filename already exist")
            
    information.update(title=title,filename=filename,path=path)

def _create_html_file(title,filename,path):
    title=xml.sax.saxutils.escape(title)
    html=HTML_TEMPLATE.format(**locals())
    #begin to save
    fh=None
    try:
        fh=open(path+filename,"w",encoding="utf8")
        fh.write(html)
    except EnvironmentError as err:
        colorprint.color_print("Error：%s\n" % err,'red')
    else:
        colorprint.color_print("Save file%s\n" % filename,'skyblue')
    finally:
        if fh is not None:
            fh.close()

def _get_string(message,name="string",default=None,minimum_length=0,maximum_length=80):
    message+=":" if default is None else "[{0}]:".format(default)
    while True:
        try:
            line=input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length==0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not(minimum_length<=len(line)<=maximum_length):
                raise ValueError("{name} must have at least"
                                 "{minimum_length} and at most"
                                 "{maximum_length} chararcters".format(**locals()))
            return line
        except ValueError as err:
            colorprint.color_print("ERROR：%s\n" % err,'red')
            
if __name__ == '__main__':
    createhtml5()
