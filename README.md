# Speccer - Specification based test runner for Python

Speccer provides simple means to test individual modules. It uses a minimal, assert-free syntax. This syntax is compiled to actual code utilizing Python's unittest. Henceforth Speccer may be seen as an alternative to it in various situations.

Run "setup.py install" to start rocking. See "demo" folder for an actual example. Once you have installed the tool just invoke "run\_specs" at that directory. You should see some test results. Feel free to tweak the files to give it a proper go.

Note that speccer uses functionality provided by Python 2.7's unittest (new asserts). If you want to use it with an older version of Python, please install [unittest2](http://pypi.python.org/pypi/unittest2/) first.

You might also want to check out the [presentation](http://www.slideshare.net/bebraw/speccer).

## Basic Specification Syntax

A module specification could look something like this:

myclass.spec: (tests myclass.py)

    set up
        c = myclass.MyClass()

    adds two and two
        c.add(2,2) == 4

    adds negatives
        c.add(10, -10) == 0

    fails adding int and string
        c.add(10, 'foo') raises TypeError

It looks pretty much like any other test you may have seen before. The syntax may be a bit lighter, though. As a test author you can focus on the essential while writing the assertions. In addition it's a bit nicer to read this way.

Note that it's possible to mix regular Python code within the tests. This might not work in all cases, though, and should be reported.

"set up" is a predefined test method that is run before each specification. This way you can set up some objects that are available for each test.

Each specification contains a name and some actual code asserting something. I have listed available assertions below:

* ==, is equal
* !=, is not equal
* ~=, is almost equal
* !~=, is not almost equal
* \>, bigger than
* \>=, bigger than or equal
* <, smaller than
* <=, smaller than or equal
* x < y < z, multiple inequalities (mix with equality as you want)
* in
* not in

These assertions map directly to ones available in Python's unittest module. If some of those seem weird to you, see http://docs.python.org/library/unittest.html .

## Changelog

* 0.7.5 - Made it possible to define functions between test definitions and made the runner more robust altogether. Now it's possible to separate tests to another directory. In addition it's possible to run tests simply by passing this directory to the runner (ie. run_specs tests).

## License

Speccer is available under MIT license. See LICENSE for more details.

