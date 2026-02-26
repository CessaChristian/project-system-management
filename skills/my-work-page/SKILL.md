---
name: my-work-page
description: Build and maintain the My Work page for the internal SR system in this Flask project. Use when implementing or updating route /my-work, assigned-SR filtering by logged-in session, sidebar navigation to My Work, table-based UI in app/templates/pages/my_work.html, and matching styles in app/static/css/style.css.
---

# My Work Page

Implement and maintain the internal `My Work` page where logged-in users see SR items currently assigned to them.

## Workflow

1. Add or update `GET /my-work` route in `app/controllers/page_controller.py`.
2. Enforce login guard with `session.get("logged_in")`.
3. Filter data by current account using `session.get("nik")`.
4. Render `app/templates/pages/my_work.html` with:
   - `active_menu="my_work"`
   - `my_work_items` (filtered rows)
   - `my_work_total` (before search)
   - `search_query`
5. Ensure sidebar `My Work` link points to `url_for('page.my_work')`.
6. Keep UI professional and simple:
   - neutral background
   - single primary accent
   - minimal animation (hover only)
7. Keep table columns:
   - NO SR
   - STATUS
   - CREATED SR
   - UPDATED
   - ACTION

## Rendering Rules

- Show only rows where SR holder matches logged-in user NIK.
- Search should filter by SR number or title.
- Empty state must be explicit and readable.
- Status is rendered as badge with class-based styling.

## Style Rules

- Extend existing `app/static/css/style.css`; do not replace global layout styles.
- Match typography, radius, spacing, and border language used by Dashboard/Create SR.
- Preserve mobile behavior with responsive rules in existing breakpoints.

## References

- Read `references/status-badges.md` when updating status color mapping.
