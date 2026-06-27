from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import Response, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

my_name = "Bartlomiej"
msg = "Hello World!"


REQUEST_COUNT = Counter(
    "printer_app_http_requests_total",
    "Total number of HTTP requests handled by the printer app.",
    ["method", "endpoint", "http_status"],
)

REQUEST_LATENCY = Histogram(
    "printer_app_http_request_duration_seconds",
    "HTTP request latency for the printer app.",
    ["endpoint"],
)


@app.after_request
def record_request_metrics(response):
    endpoint = request.endpoint or "unknown"
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        http_status=response.status_code,
    ).inc()
    return response


@app.route('/')
def index():
    with REQUEST_LATENCY.labels(endpoint="index").time():
        output = request.args.get('output')
        if not output:
            output = PLAIN
        return get_formatted(msg, my_name, output.lower())


@app.route('/outputs')
def supported_output():
    with REQUEST_LATENCY.labels(endpoint="supported_output").time():
        return ", ".join(SUPPORTED)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

