"""Update all TOC fields and indexes in a .docx via LibreOffice's UNO bridge.

Usage:
    PYTHONPATH=<libreoffice-program-dir> python update_toc.py <abs-path-to-docx> <port>

Expects soffice to be running with --accept="socket,host=localhost,port=<port>;urp".
"""

import sys
import time

import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.connection import NoConnectException


def make_prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def connect(port, timeout=20.0):
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    deadline = time.time() + timeout
    last_err = None
    while time.time() < deadline:
        try:
            return resolver.resolve(
                f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext"
            )
        except NoConnectException as e:
            last_err = e
            time.sleep(0.3)
    raise last_err


def main(path, port):
    ctx = connect(port)
    sm = ctx.ServiceManager
    desktop = sm.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    url = uno.systemPathToFileUrl(path)
    doc = desktop.loadComponentFromURL(
        url, "_blank", 0, (make_prop("Hidden", True),)
    )
    if doc is None:
        # Most common cause: a stale .~lock.<name>.docx# file next to the
        # target. The bash wrapper now wipes these before invoking us, so
        # this only fires for genuinely unreadable docs.
        print(
            f"LibreOffice could not load {path} (loadComponentFromURL returned None)",
            file=sys.stderr,
        )
        sys.exit(1)

    # Refresh dynamic fields (TOC instruction fields).
    try:
        doc.refresh()
    except Exception as e:
        print(f"warn: refresh failed: {e}", file=sys.stderr)

    # Update each native DocumentIndex (LO converts Word TOC fields into these on load).
    indexes = doc.DocumentIndexes
    print(f"DocumentIndexes count: {indexes.Count}", file=sys.stderr)
    for i in range(indexes.Count):
        idx = indexes.getByIndex(i)
        print(f"  updating index #{i}: {idx.Name}", file=sys.stderr)
        idx.update()

    # Belt and braces: dispatch the GUI command.
    try:
        dispatcher = sm.createInstanceWithContext(
            "com.sun.star.frame.DispatchHelper", ctx
        )
        frame = doc.CurrentController.Frame
        for cmd in (".uno:UpdateAllIndexes", ".uno:UpdateAll"):
            dispatcher.executeDispatch(frame, cmd, "", 0, ())
    except Exception as e:
        print(f"warn: dispatch failed: {e}", file=sys.stderr)

    doc.store()
    doc.close(True)
    # Don't call desktop.terminate() — it disposes the bridge mid-call and
    # leaves the Python interpreter blocked in atexit cleanup. The bash
    # cleanup_lo trap kills the soffice daemon via pkill instead.


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: update_toc.py <abs-path-to-docx> <port>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], int(sys.argv[2]))
