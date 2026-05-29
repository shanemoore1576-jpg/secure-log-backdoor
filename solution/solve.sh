#!/bin/bash
# 1. Redact the sensitive token from the logs
sed -i 's/secret_live_token_abcd123/[REDACTED]/g' /var/log/app/debug.log

# 2. Toggle the systemic log masking config variable
sed -i 's/LOG_MASKING=FALSE/LOG_MASKING=TRUE/g' /app/config.env
