from app.events.bus import event_bus

from app.events.handlers.audit import on_program_created as audit

from app.events.handlers.planner import on_program_created as planner


def register_events():

    event_bus.subscribe(
        "program.created",
        planner,
    )

    event_bus.subscribe(
        "program.created",
        audit,
    )
