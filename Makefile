# Local development tasks. Run `make help` for the list.
#
# Postgres runs in Docker; the backend and frontend run on the host because
# the backend reads models/*.joblib from the repo root, which the backend
# image does not contain. Backend settings default to local development
# values (see backend/src/crate_backend/core/config.py).

.DEFAULT_GOAL := help
.PHONY: help dev check-docker db migrate backend frontend install stop

help: ## List the available tasks
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

dev: db migrate ## Start Postgres, then backend and frontend together (Ctrl+C stops both)
	$(MAKE) -j2 backend frontend

check-docker: ## Fail with a reminder if Docker Desktop is not running
	@perl -e '$$p = fork; exec @ARGV unless $$p; $$SIG{ALRM} = sub { kill 9, $$p; exit 1 }; alarm 5; waitpid $$p, 0; exit($$? ? 1 : 0)' docker info >/dev/null 2>&1 || { \
		echo "Docker is not running. Open Docker Desktop, wait for it to say it is running, then re-run make. (A hung check also means Docker is still starting or stuck.)"; \
		exit 1; }

db: check-docker ## Start Postgres and wait until it is healthy
	docker compose up -d --wait db

migrate: ## Apply database migrations
	cd backend && uv run alembic upgrade head

backend: ## Start the API on http://localhost:8000
	cd backend && uv run uvicorn crate_backend.main:app --reload --port 8000

frontend: ## Start the web app (run `make install` once first)
	cd frontend && npm run dev

install: ## Install backend and frontend dependencies
	cd backend && uv sync
	cd frontend && npm install

stop: check-docker ## Stop Postgres (data is kept)
	docker compose stop db
