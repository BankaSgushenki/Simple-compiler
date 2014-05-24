#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lexer
import parser
import compiler

lexer = lexer.Lexer()
lexer.parse()

compiler = compiler.Compiler()

parser = parser.Parser(lexer)
compiler.showTree(parser.parse())
