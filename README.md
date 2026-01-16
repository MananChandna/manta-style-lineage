
</head>
<body>

<h1>MANTA-Style Column-Level Data Lineage PoC</h1>

<h2>Overview</h2>
<p>
This project demonstrates a <strong>static, column-level data lineage engine</strong>
inspired by how <strong>MANTA Data Lineage</strong> operates internally.
</p>

<h2>Objective</h2>
<ul>
  <li>Replicate MANTA’s static lineage philosophy</li>
  <li>Parse SQL without execution</li>
  <li>Generate column-level lineage</li>
  <li>Produce impact-analysis-ready artifacts</li>
</ul>

<h2>Architecture</h2>
<pre>
SQL Code
  ↓
Abstract Syntax Tree (AST)
  ↓
Alias & Table Resolution
  ↓
Column-Level Mapping
  ↓
Lineage Graph + CSV
</pre>

<h2>Data Flow</h2>
<ul>
  <li><strong>orders</strong> → staging</li>
  <li><strong>stg_orders</strong> → aggregation</li>
  <li><strong>agg_sales</strong> → reporting</li>
</ul>

<h2>Key Features</h2>
<ul>
  <li>Static SQL parsing (no query execution)</li>
  <li>Alias & JOIN resolution</li>
  <li>Aggregation detection (SUM)</li>
  <li>Multi-hop lineage</li>
  <li>Visual and tabular outputs</li>
</ul>

<h2>Outputs</h2>
<ul>
  <li><code>column_lineage.csv</code> – column-level mappings</li>
  <li><code>lineage.png</code> – visual lineage graph</li>
</ul>

<h2>Proof of Execution</h2>
<p>
See the <code>proof/</code> folder for execution screenshots, lineage outputs,
and project structure evidence.
</p>

<h2>Limitations</h2>
<ul>
  <li>No runtime or row-level lineage</li>
  <li>No stored procedure parsing</li>
  <li>CTEs and nested queries can be added as Phase 2</li>
</ul>

<h2>Ethical Positioning</h2>
<p>
This project does <strong>not</strong> use licensed MANTA software.
It demonstrates understanding of MANTA’s <strong>core lineage principles</strong>
using open-source tools.
</p>

<h2>Author</h2>
<p>
Built as an interview-ready Proof of Concept for enterprise data lineage roles.
</p>

</body>
</html>
