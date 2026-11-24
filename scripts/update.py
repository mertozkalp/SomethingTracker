import datetime, json, os, pathlib, urllib.request, urllib.error
root = pathlib.Path(__file__).resolve().parents[1]
projects = json.loads((root / "data/projects.json").read_text())
assert len({p["repo"] for p in projects}) == len(projects)
lines = ["# Repository activity snapshot", "", "Generated: " + datetime.datetime.now(datetime.timezone.utc).isoformat(), "", "Metadata only; not proof of gameplay.", "", "| Project | Group | Last push | Stars | Open issues/PRs | State |", "| --- | --- | --- | --- | --- | --- |"]
for p in projects:
    name = p["repo"]
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "SomethingTracker"}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    try:
        with urllib.request.urlopen(urllib.request.Request("https://api.github.com/repos/" + name, headers=headers), timeout=20) as response:
            d = json.load(response)
        values = [d.get("pushed_at"), d.get("stargazers_count"), d.get("open_issues_count"), "Archived" if d.get("archived") else "Fork" if d.get("fork") else "Accessible"]
    except (OSError, ValueError) as e:
        values = ["?", "?", "?", "HTTP " + str(e.code) if isinstance(e, urllib.error.HTTPError) else "Request failed"]
    lines.append("| " + " | ".join([f"[{name}](https://github.com/{name})", p["category"]] + list(map(str, values))) + " |")
(root / "STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
