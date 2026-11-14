# LinkedIn AI Agent reviewer demo

A local Flask fixture for reviewing the start and log API. Use `python -m pip install -r requirements-reviewer.txt`, then `python app.py`.

Run `curl -X POST http://127.0.0.1:5000/start-agent` to exercise the start fixture.

## Deployment verification

```sh
docker build -t reviewer-smoke .
docker run --rm -p 127.0.0.1:5000:5000 reviewer-smoke
```

From another terminal, run `curl --fail http://127.0.0.1:5000/`. Expect HTTP 200. The Flask route simulates a start request and returns HTTP 200 with a JSON status of simulated. It posts nothing. The scheduler and integration scripts are historical experiments outside the tested demo.
