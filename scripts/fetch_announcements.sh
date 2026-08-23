#!/usr/bin/env bash
# GitHub Discussions의 Announcements category를 build-time data로 내려받는다.
# 출력: data/announcements.json (Hugo .Site.Data.announcements). 인증은 gh CLI(GITHUB_TOKEN/GH_TOKEN)를 따른다.
# 실패 시 빈 목록을 기록해 빌드를 막지 않는다. 공지 표시 여부는 layouts/home.html의 with 가드가 소유한다.
set -u
out="${1:-data/announcements.json}"
mkdir -p "$(dirname "$out")"
query='query($owner:String!,$name:String!){ repository(owner:$owner,name:$name){ discussions(first:20, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{ number title url createdAt category{ slug } } } } }'
if gh api graphql -F owner=kyungseo -F name=kyungseo.github.io -f query="$query" \
    --jq '[.data.repository.discussions.nodes[] | select(.category.slug=="announcements") | {number,title,url,createdAt}]' > "$out.tmp"; then
  mv "$out.tmp" "$out"
  echo "announcements: $(python3 -c 'import json,sys;print(len(json.load(open(sys.argv[1]))))' "$out") item(s) -> $out"
else
  rm -f "$out.tmp"
  echo '[]' > "$out"
  echo "announcements: fetch failed; wrote empty list -> $out" >&2
fi
