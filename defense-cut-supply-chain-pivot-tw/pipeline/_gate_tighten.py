"""Tighten cull: demote weak qs=3 academic accepts that fail 'material' test.

Strict rule: an academic accept must (a) name Taiwan AND (defense OR machine tool
OR cross-strait industrial relocation OR drone OR long-arm/Entity List), OR
(b) be a canonical direct-mechanism paper on US export controls / PRC counter-
sanctions even without Taiwan in the title.

Demote-to-reject if the only justification is 'analogue', 'scaffold', 'framing
for', 'baseline for'. Those phrases admit the record is adjacent, not material.
"""
import sys
sys.path.insert(0, '.')
# Re-import the decision table by exec'ing the original module's setup
import importlib.util, json
spec = importlib.util.spec_from_file_location("gr", "_gate_run.py")
# Don't execute — we'll just monkey-edit decisions and re-emit
