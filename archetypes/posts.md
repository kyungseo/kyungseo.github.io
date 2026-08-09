---
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
slug: '{{ .File.ContentBaseName }}'
date: '{{ .Date }}'
draft: true
format: essay        # essay | note
tags: []
series: []           # 시리즈 slug — 없으면 빈 배열
summary: ""
toc: false
# 재게시·개작일 때만 (`첫 게시` 대신 `게시`로 표시):
# original_date:
# original_url:
# edited: false
# 기본 안내 문구를 대체할 때만 (origin 여부와 무관하게 표시):
# provenance_note:
# 독자의 이해·판단에 영향을 주는 변경만 최신순으로 표시됨:
# updates:
#   - date: 2026-08-12T14:30:00+09:00
#     kind: update       # update | correction
#     summary: "무엇이 달라졌는지 한 문장으로 설명"
# 관련 자료가 독자에게 도움이 될 때만:
# related:
#   - type: threads      # threads | github | post | other
#     label: "Threads에서 이어진 메모"
#     url: "https://www.threads.com/..."
# migration compatibility only — 새 글은 related 사용:
# social_url:
---
