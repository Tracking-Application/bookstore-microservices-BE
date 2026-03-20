#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${APP_DIR:-$HOME/bookstore-microservices-BE}"
BRANCH="${BRANCH:-main}"
USE_SUDO_DOCKER="${USE_SUDO_DOCKER:-false}"

if [ ! -d "$APP_DIR/.git" ]; then
  echo "ERROR: APP_DIR is not a git repository: $APP_DIR"
  exit 1
fi

cd "$APP_DIR"

echo "Deploying branch '$BRANCH' in $APP_DIR"
git fetch origin "$BRANCH"
git checkout "$BRANCH"
git pull --ff-only origin "$BRANCH"

if [ "$USE_SUDO_DOCKER" = "true" ]; then
  docker_cmd=(sudo docker)
else
  docker_cmd=(docker)
fi

compose() {
  if "${docker_cmd[@]}" compose version >/dev/null 2>&1; then
    "${docker_cmd[@]}" compose "$@"
  else
    if [ "$USE_SUDO_DOCKER" = "true" ]; then
      sudo docker-compose "$@"
    else
      docker-compose "$@"
    fi
  fi
}

compose -f docker-compose.yml up -d --build --remove-orphans

# Optional cleanup to control disk growth over time
if [ "$USE_SUDO_DOCKER" = "true" ]; then
  sudo docker image prune -f || true
else
  docker image prune -f || true
fi

echo "Deployment completed successfully."