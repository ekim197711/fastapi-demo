from behave import *


@given(u'person is in dark forrest with {device}')
def step_impl(context, device):
    context.firestarter = device
    context.lightlevel = 0
    print("Oh no Im in a dark forrest with " + device + " is in dark forrest")


@when('we start a fire')
def step_impl(context):
    print("swip swip click click we use the {}".format(context.firestarter))
    context.lightlevel = 5


@when('we drop the firestarter')
def step_impl(context):
    print("Wopsi I dropped the {}".format(context.firestarter))
    context.firestarter = None


@then("it is less dark")
def step_impl(context):
    print("Wow my date half is pretty {}".format(context.lightlevel))
    assert context.lightlevel > 2


@then('we still have the {device}')
def step_impl_then_second(context, device):
    print("Check if I still have the {}".format(device))
    assert context.firestarter == device


@step('we pick up {tool} and eat some {food}')
def step_impl(context, tool, food):
    context.firestarter = tool
    context.lasteaten = food
