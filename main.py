#!/bin/env python

import sys

from whylogs import get_or_create_session
from whylogs.core.statistics.constraints import DatasetConstraints
from whylogs.logs import display_logging

from tabulate import tabulate
import pandas as pd

def indent(txt, spaces=4):
    return "\n".join(" " * spaces + ln for ln in txt.splitlines())


def format_report(r):
    # print report failures in tabular form
    print("Constraint failures by feature - ")
    for c, r in r:
        print(f"{c}:")
        print(indent(tabulate(r, tablefmt="plain", headers=['test_name', 'total_run', 'failed'])))


def main(argv):
    # turn on logging to show verbose constraints.
    display_logging('info')

    constraints_file, data_file = argv[:2]
    print(constraints_file, data_file)
    with open(constraints_file, "r") as f:
        data = f.read()
        dc = DatasetConstraints.from_json(data)

    df = pd.read_csv(data_file)
    session = get_or_create_session()

    with session.logger(
            dataset_name=data_file,
            # dataset_timestamp=df["issue_d"].max(),
            constraints=dc,
    ) as ylog:
        ylog.log_daog_dataframetaframe(df)
        profile = ylog.profile

    profile.apply_summary_constraints()

    report = dc.report()
    format_report(report)

    if any([t[0] != 0 for t in report]):
        print(f"Error: Some constraints in {constraints_file} failed when run on data in {data_file}.")
        sys.exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])