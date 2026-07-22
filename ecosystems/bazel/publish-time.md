# Ecosystem: Bazel (bzlmod)

## Publish time (quarantine)

BCR does not always expose upload times in `metadata.json`. When publish time is
unknown, treat candidate bumps as **wait** unless product policy defines another
source (release tags, etc.). Prefer conservative wait over inventing timestamps.
