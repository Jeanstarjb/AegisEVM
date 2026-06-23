from aegisevm.disassembler.disassembly import Disassembly
from aegisevm.laser.ethereum.instructions import Instruction
from aegisevm.laser.ethereum.state.environment import Environment
from aegisevm.laser.ethereum.state.global_state import GlobalState
from aegisevm.laser.ethereum.state.machine_state import MachineState
from aegisevm.laser.ethereum.state.world_state import WorldState
from aegisevm.laser.ethereum.transaction.transaction_models import MessageCallTransaction
from aegisevm.laser.smt import symbol_factory
from aegisevm.support.support_utils import get_code_hash

# Arrange
world_state = WorldState()
account = world_state.create_account(balance=10, address=101)
account.code = Disassembly("60606040")
world_state.create_account(balance=10, address=1000)
environment = Environment(account, None, None, None, None, None, None)
og_state = GlobalState(world_state, environment, None, MachineState(gas_limit=8000000))
og_state.transaction_stack.append(
    (MessageCallTransaction(world_state=WorldState(), gas_limit=8000000), None)
)

instruction = Instruction("extcodehash", dynamic_loader=None)


def test_extcodehash_no_account():
    # If account does not exist, return 0
    og_state.mstate.stack = [symbol_factory.BitVecVal(1, 256)]
    new_state = instruction.evaluate(og_state)[0]
    assert new_state.mstate.stack[-1] == 0


def test_extcodehash_no_code():
    # If account code does not exist, return hash of empty set.
    og_state.mstate.stack = [symbol_factory.BitVecVal(1000, 256)]
    new_state = instruction.evaluate(og_state)[0]
    assert hex(new_state.mstate.stack[-1].value) == get_code_hash("")


def test_extcodehash_return_hash():
    # If account code exists, return hash of the code.
    og_state.mstate.stack = [symbol_factory.BitVecVal(101, 256)]
    new_state = instruction.evaluate(og_state)[0]
    assert hex(new_state.mstate.stack[-1].value) == get_code_hash("60606040")
