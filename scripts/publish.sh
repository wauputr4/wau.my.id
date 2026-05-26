#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: ./scripts/publish.sh [-m "commit message"] [--force-build] [--no-push]

Publish wau.my.id in one step:
- auto-detect whether content/blog changed
- rebuild blog only when needed
- git add, commit, and push

Options:
  -m, --message   Commit message to use (default: "Publish site update")
  --force-build    Always run the blog builder
  --no-push        Skip git push after commit
  -h, --help       Show this help
EOF
}

commit_message="Publish site update"
force_build=false
no_push=false

while (($#)); do
  case "$1" in
    -m|--message)
      if (($# < 2)); then
        echo "Missing value for $1" >&2
        exit 1
      fi
      commit_message="$2"
      shift 2
      ;;
    --force-build)
      force_build=true
      shift
      ;;
    --no-push)
      no_push=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

blog_changed=false
if [[ "$force_build" == true ]]; then
  blog_changed=true
elif [[ -n "$(git status --porcelain --untracked-files=all -- content/blog scripts/build_blog.py scripts/preflight_blog.py assets/blog assets/og)" ]]; then
  blog_changed=true
fi

if [[ "$blog_changed" == true ]]; then
  python3 scripts/build_blog.py --repo .
  python3 scripts/preflight_blog.py --repo .
fi

git add -A

if git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git commit -m "$commit_message"

if [[ "$no_push" == true ]]; then
  echo "Commit created; push skipped by request."
  exit 0
fi

git push
