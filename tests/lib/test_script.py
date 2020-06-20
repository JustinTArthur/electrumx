import pytest

from electrumx.lib.script import OpCode, is_unspendable_legacy, is_unspendable_genesis


@pytest.mark.parametrize("script, iug", (
    (bytes([OpCode.OP_RETURN]), False),
    (bytes([OpCode.OP_RETURN]) + bytes([2, 28, 50]), False),
    (bytes([OpCode.OP_0, OpCode.OP_RETURN]), True),
    (bytes([OpCode.OP_0, OpCode.OP_RETURN]) + bytes([2, 28, 50]), True)
))
def test_op_return_legacy(script, iug):
    assert is_unspendable_legacy(script)
    assert is_unspendable_genesis(script) is iug


@pytest.mark.parametrize("script", (
        bytes([]),
        bytes([OpCode.OP_1, OpCode.OP_RETURN]) + bytes([2, 28, 50]),
        bytes([OpCode.OP_0]),
        bytes([OpCode.OP_0, OpCode.OP_1]),
        bytes([OpCode.OP_HASH160]),
))
def test_not_op_return(script):
    assert not is_unspendable_legacy(script)
    assert not is_unspendable_genesis(script)
