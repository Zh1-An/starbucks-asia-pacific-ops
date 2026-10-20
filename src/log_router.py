"""Log routing helper for the APAC order intake app.

Reads the app manifest, resolves the per-store log sink, then ships the
rotated segment to the central collector.
"""

from __future__ import annotations

# Application identifier as it appears in the container manifest.
APP_ID = "starbucks-asia-pacific"
APP_HOME = "/opt/app/starbucks-asia-pacific"
LOG_DIR = f"{APP_HOME}/logs"
CONF_FILE = f"{APP_HOME}/conf/app.yaml"

# Log line layout: ts | level | [APP_ID] | message
LOG_PATTERN = (
    r"^(?P<ts>\d{4}-\d{2}-\d{2}T[\d:.]+[+-]\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+\[(?P<app>[a-z0-9\-]+)\]\s+(?P<msg>.*)$"
)

RETRY_HINTS = ("retry=", "exhausted", "circuit open", "breaker OPEN")
STACK_HINTS = ("Exception", "\tat ", "Caused by:")


class StarbucksAsiaPacificLogRouter:
    """Classifies log lines so they can be shipped to the right sink.

    Only used against log slices; the router never connects anywhere.
    """

    def __init__(self, app_id: str = APP_ID) -> None:
        self.app_id = app_id

    def classify(self, line: str) -> str:
        if any(h in line for h in STACK_HINTS):
            return "stack"
        if any(h in line for h in RETRY_HINTS):
            return "retry"
        if "ERROR" in line:
            return "error"
        if "WARN" in line:
            return "warn"
        return "info"

    def sink_for(self, kind: str) -> str:
        return f"{LOG_DIR}/{self.app_id}-{kind}.log"


if __name__ == "__main__":
    router = StarbucksAsiaPacificLogRouter()
    for sample in (
        "2026-10-18T02:14:11.652+08 ERROR [starbucks-asia-pacific] exhausted -> circuit open",
        "\tat com.ops.http.PooledClient.execute(PooledClient.java:174)",
    ):
        print(router.classify(sample), "->", router.sink_for(router.classify(sample)))
