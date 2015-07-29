"""Fortran operator definitions."""
from __future__ import (absolute_import, print_function)

from .registry import Registry
from . import types


#: Registry of operators:
REGISTRY = Registry()

OPTYPE_UNARY = 1
OPTYPE_BINARY= 2


class FortranOperator(object):
    """A Fortran operator."""

    def __init__(self, name, operator, return_type, kind):
        """Create a Fortran operator.
        
        **Arguments:**

        *name*
            The name of the operator, used to for function names.

        *operator*
            The string representation of the operator in Fortran.

        *return_type*
            A `FortranType` instance representing the return type of the
            operator.

        """
        self.name = name
        self.operator = operator
        self.return_type = return_type
        self.kind = kind

    def is_kind(self, kind):
        return self.kind & kind == kind


#: Addition operator.
RPE_OP_ADD = FortranOperator(
    'add',
    '+',
    types.RPE_VAR,
    OPTYPE_UNARY | OPTYPE_BINARY)
REGISTRY.register(RPE_OP_ADD)

#: Subtraction operator.
RPE_OP_SUB = FortranOperator(
    'sub',
    '-',
    types.RPE_VAR,
    OPTYPE_UNARY | OPTYPE_BINARY)
REGISTRY.register(RPE_OP_SUB)

#: Multiplication operator.
RPE_OP_MUL = FortranOperator(
    'mul',
    '*',
    types.RPE_VAR,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_MUL)

#: Division operator.
RPE_OP_DIV = FortranOperator(
    'div',
    '/',
    types.RPE_VAR,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_DIV)

#: Greater-than or equal-to operator.
RPE_OP_GE = FortranOperator(
    'ge',
    '.GE.',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_GE)

#: Less-than or equal-to operator.
RPE_OP_LE = FortranOperator(
    'le',
    '.LE.',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_LE)

#: Greater-than operator.
RPE_OP_GT = FortranOperator(
    'gt',
    '.GT.',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_GT)

#: Less-than operator.
RPE_OP_LT = FortranOperator(
    'lt',
    '.LT.',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_LT)

#: Equal-to operator.
RPE_OP_EQ = FortranOperator(
    'eq',
    '==',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_EQ)

#: Not-equal-to operator.
RPE_OP_NE = FortranOperator(
    'ne',
    '/=',
    types.LOGICAL,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_NE)

#: Exponentiation operator.
RPE_OP_POW = FortranOperator(
    'pow',
    '**',
    types.RPE_VAR,
    OPTYPE_BINARY)
REGISTRY.register(RPE_OP_POW)
