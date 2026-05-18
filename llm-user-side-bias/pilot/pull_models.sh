#!/bin/bash
# Pull all six models for local-deployment probe.
# Continues on individual failures; logs each result.

set -u
LOG="$(dirname "$0")/pull_models.log"
: > "$LOG"  # truncate

MODELS=(
  "deepseek-r1:8b"
  "qwen3:8b"
  "glm4:9b"
  "huihui_ai/deepseek-r1-abliterated:8b"
  "huihui_ai/qwen3-abliterated:8b"
  "huihui_ai/glm-4-9b-chat-abliterated"
)

echo "=== pull_models.sh started at $(date -Iseconds) ===" | tee -a "$LOG"
echo "Total models: ${#MODELS[@]}" | tee -a "$LOG"
echo "" | tee -a "$LOG"

success=0
failure=0
failed_models=()

for model in "${MODELS[@]}"; do
  echo "--- pulling: $model  ($(date -Iseconds)) ---" | tee -a "$LOG"
  if ollama pull "$model" 2>&1 | tee -a "$LOG"; then
    echo "✓ ok: $model" | tee -a "$LOG"
    success=$((success+1))
  else
    echo "✗ FAILED: $model" | tee -a "$LOG"
    failure=$((failure+1))
    failed_models+=("$model")
  fi
  echo "" | tee -a "$LOG"
done

echo "=== done at $(date -Iseconds) ===" | tee -a "$LOG"
echo "success: $success / ${#MODELS[@]}" | tee -a "$LOG"
echo "failure: $failure" | tee -a "$LOG"
if [ ${#failed_models[@]} -gt 0 ]; then
  echo "failed models:" | tee -a "$LOG"
  for m in "${failed_models[@]}"; do
    echo "  - $m" | tee -a "$LOG"
  done
fi

echo "" | tee -a "$LOG"
echo "--- final model list ---" | tee -a "$LOG"
ollama list 2>&1 | tee -a "$LOG"
