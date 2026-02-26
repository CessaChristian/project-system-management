from flask import Blueprint, redirect, render_template, request, session, url_for

page_bp = Blueprint("page", __name__)


# Temporary in-memory "My Work" queue.
# A row is shown to the logged-in user when holder_nik == session["nik"].
MY_WORK_SAMPLE = [
    {
        "sr_no": "SR-2025-0001",
        "title": "Enhancement Approval Budget",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0002",
        "title": "Integrasi Vendor Master Data",
        "status_label": "QA ON PROGRESS",
        "status_class": "status-progress",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0003",
        "title": "Refactor Service Monitoring",
        "status_label": "CANCEL",
        "status_class": "status-cancel",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0004",
        "title": "Dashboard KPI Cabang",
        "status_label": "NEW SR",
        "status_class": "status-new",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0005",
        "title": "Perubahan Workflow Rekonsiliasi",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0006",
        "title": "Optimasi Notifikasi Email",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0007",
        "title": "Revisi SLA Approval",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0008",
        "title": "Automation Assignment Ticket",
        "status_label": "IN REVIEW",
        "status_class": "status-review",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0009",
        "title": "Pembaruan Hak Akses Modul SR",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0010",
        "title": "Integrasi Log Aktivitas User",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0011",
        "title": "Improvement Audit Trail",
        "status_label": "QA ON PROGRESS",
        "status_class": "status-progress",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0012",
        "title": "Validasi Data Import",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "1-Jan-25",
        "updated_at": "2-Feb-25",
        "holder_nik": "00000",
    },
    {
        "sr_no": "SR-2025-0013",
        "title": "Revamp Purchasing Workflow",
        "status_label": "BACKLOG QA",
        "status_class": "status-backlog",
        "created_at": "9-Jan-25",
        "updated_at": "12-Feb-25",
        "holder_nik": "10001",
    },
]


def _get_my_work_queue(current_nik: str, query: str):
    if not current_nik:
        return [], 0

    queue = [item for item in MY_WORK_SAMPLE if item["holder_nik"] == current_nik]
    total = len(queue)

    if query:
        lowered = query.lower()
        queue = [
            item
            for item in queue
            if lowered in item["sr_no"].lower() or lowered in item["title"].lower()
        ]

    return queue, total


@page_bp.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return redirect(url_for("page.dashboard"))


@page_bp.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("pages/dashboard.html", active_menu="dashboard")


@page_bp.route("/create-sr")
def create_sr():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("pages/create_sr.html", active_menu="create_sr")


@page_bp.route("/my-work")
def my_work():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))

    search_query = request.args.get("q", "").strip()
    current_nik = session.get("nik", "")
    my_work_items, my_work_total = _get_my_work_queue(current_nik, search_query)

    return render_template(
        "pages/my_work.html",
        active_menu="my_work",
        my_work_items=my_work_items,
        my_work_total=my_work_total,
        search_query=search_query,
    )
