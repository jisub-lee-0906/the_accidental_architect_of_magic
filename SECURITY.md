# Security boundaries

## Trusted local CLI configuration

This project may reference local development tooling. Explicit local CLI configuration is trusted operator input, not a public service interface. Do not route it through an internet-facing service without authentication, authorization, and review.

## Loopback services

Loopback addresses are local integration settings, not credentials and not remotely reachable by themselves. Preserve loopback binding for local tooling unless a deliberate authenticated deployment is reviewed.

## Private artifacts

Generated media, screenshots, contact sheets, asset metadata, and production evidence require release review. Inspect media visually and aurally before publication; do not infer safety solely from static metadata checks.

## Reporting

Report suspected credentials or unsafe publication artifacts privately. Do not include secret values in reports or issues.
