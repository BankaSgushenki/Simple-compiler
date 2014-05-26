#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import lexer
import parser
import compiler

ROOT_PATH = os.path.dirname(__file__) + "/source.txt"

lexer = lexer.Lexer(ROOT_PATH)
lexer.parse()

parser = parser.Parser(lexer)

interpreter = compiler.Interpreter(parser.parse())
interpreter.interpretate()