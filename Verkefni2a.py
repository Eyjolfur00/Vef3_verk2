from bottle import *
import os

@route('/')
def index():
    return """
        <title>Verkefni2a</title>
        <meta charset="utf-8">
        <h1>Sidur</h1>
        <a href="/1">Sída 1</a>
        <a href="/2">Sída 2</a>
        <a href="/3">Sída 3</a>
            """
@route('/<nr>')
def index(nr):
    if nr=='1':
        return """
            <title>Verkefni2a</title>
            <meta charset="utf-8">
            <h1>Sida 1</h1>
            <a href="/1">Sída 1</a>
            <a href="/2">Sída 2</a>
            <a href="/3">Sída 3</a>
               """

    if nr=='2':
        return """
            <title>Verkefni2a</title>
            <meta charset="utf-8">
            <h1>Sida 2</h1>
            <a href="/1">Sída 1</a>
            <a href="/2">Sída 2</a>
            <a href="/3">Sída 3</a>
               """
    if nr=='3':
        return """
            <title>Verkefni2a</title>
            <meta charset="utf-8">
            <h1>Sida 3</h1>
            <a href="/1">Sída 1</a>
            <a href="/2">Sída 2</a>
            <a href="/3">Sída 3</a>
               """


run(host="0.0.0.0", port=os.environ.get("PORT"))
