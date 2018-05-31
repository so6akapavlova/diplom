#!/bin/bash

while true; do
  out=()
  for (( i=0; i<5; i++ )); do
    read && out+=( "$REPLY" )
  done
  if (( ${#out[@]} > 0 )); then
    printf '%s ' "${out[@]}"
    echo
  fi
  if (( ${#out[@]} < 5 )); then break; fi
done <quantiles.txt >quantiles2.txt
