import os
import csv
import sqlglot
from sqlglot import parse_one, exp
import networkx as nx

SQL_FILES = {
    "stg_orders": "sql/stg_orders.sql",
    "agg_sales": "sql/agg_sales.sql",
    "customer_revenue": "sql/customer_revenue.sql"
}

OUTPUT_DOT = "output/lineage.dot"
OUTPUT_CSV = "output/column_lineage.csv"

def extract_table_aliases(tree):
    alias_map = {}
    for table in tree.find_all(exp.Table):
        alias = table.alias
        table_name = table.name
        if alias:
            alias_map[alias] = table_name
        else:
            alias_map[table_name] = table_name
    return alias_map

def qualify_column(col, alias_map):
    table = col.table
    if table and table in alias_map:
        return f"{alias_map[table]}.{col.name}"
    if table:
        return f"{table}.{col.name}"
    if len(alias_map) == 1:
        return f"{list(alias_map.values())[0]}.{col.name}"
    return f"UNKNOWN_TABLE.{col.name}"

def extract_column_lineage(sql_text, target_object):
    tree = parse_one(sql_text)
    alias_map = extract_table_aliases(tree)
    lineage = []

    for select in tree.find_all(exp.Select):
        for proj in select.expressions:
            if isinstance(proj, exp.Alias):
                target_col = proj.alias
                expr = proj.this

                if isinstance(expr, exp.Func):
                    for col in expr.find_all(exp.Column):
                        lineage.append(
                            (qualify_column(col, alias_map),
                             f"{target_object}.{target_col}",
                             expr.name.upper())
                        )
                elif isinstance(expr, exp.Column):
                    lineage.append(
                        (qualify_column(expr, alias_map),
                         f"{target_object}.{target_col}",
                         "passthrough")
                    )

            elif isinstance(proj, exp.Column):
                lineage.append(
                    (qualify_column(proj, alias_map),
                     f"{target_object}.{proj.name}",
                     "passthrough")
                )

    return lineage

def main():
    os.makedirs("output", exist_ok=True)
    graph = nx.DiGraph()
    rows = []

    for target, path in SQL_FILES.items():
        sql_text = open(path).read()
        for src, tgt, logic in extract_column_lineage(sql_text, target):
            graph.add_edge(src, tgt, transformation=logic)
            rows.append([src, tgt, logic])

    nx.drawing.nx_pydot.write_dot(graph, OUTPUT_DOT)

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source_column", "target_column", "transformation"])
        writer.writerows(rows)

    print("Column-level lineage extraction completed")

if __name__ == "__main__":
    main()
